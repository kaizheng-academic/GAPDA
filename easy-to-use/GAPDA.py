from __future__ import division

import numpy as np
from keras.callbacks import EarlyStopping, TensorBoard, ModelCheckpoint
from keras.layers import Input, Dropout
from keras.models import Model
from keras.optimizers import Adam
from keras.regularizers import l2

from keras_gat import GraphAttention
from keras_gat.utils import load_data, preprocess_features


def StorFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return



def GAPDA(isIndependent):


    #A is adj,X is feature, Y label, index bool-label
    A, X, Y_train, Y_val, Y_test, idx_train, idx_val, idx_test  = load_data()
   
  





    # Parameters
  
    N = X.shape[0]                # Number of nodes in the graph
    F = X.shape[1]                # Original feature dimension

    
    n_classes = Y_train.shape[1]  # Number of classes
    F_ = 8                        # Output size of first GraphAttention layer
    n_attn_heads = 8              # Number of attention heads in first GAT layer
    dropout_rate = 0.02           # Dropout rate (between and inside GAT layers)
    l2_reg = 5e-4/4               # Factor for l2 regularization
    learning_rate = 5e-2          # Learning rate for Adam
    epochs = 100                # Number of training epochs
    es_patience = 150

    # Preprocessing operations
    X = preprocess_features(X)
    A = A + np.eye(A.shape[0])  # Add self-loops

    # Model definition (as per Section 3.3 of the paper)
    X_in = Input(shape=(F,))
    A_in = Input(shape=(N,))

    dropout1 = Dropout(dropout_rate)(X_in)
    graph_attention_1 = GraphAttention(F_,
                                        attn_heads=n_attn_heads,
                                        attn_heads_reduction='concat',
                                        dropout_rate=dropout_rate,
                                        activation='elu',
                                        kernel_regularizer=l2(l2_reg),
                                        attn_kernel_regularizer=l2(l2_reg))([dropout1, A_in])
    dropout2 = Dropout(dropout_rate)(graph_attention_1)
    graph_attention_2 = GraphAttention(n_classes,
                                        attn_heads=1,
                                        attn_heads_reduction='average',
                                        dropout_rate=dropout_rate,
                                        activation='softmax',
                                        kernel_regularizer=l2(l2_reg),
                                        attn_kernel_regularizer=l2(l2_reg))([dropout2, A_in])

    # Build model
    model = Model(inputs=[X_in, A_in], outputs=graph_attention_2)
    optimizer = Adam(lr=learning_rate)
    model.compile(optimizer=optimizer,
                    loss='categorical_crossentropy',
                    weighted_metrics=['acc'])
    model.summary()

    # Callbacks
    es_callback = EarlyStopping(monitor='weighted_acc', patience=es_patience)
    tb_callback = TensorBoard(batch_size=N)
    mc_callback = ModelCheckpoint('./logs/best_model.h5',
                                    monitor='weighted_acc',
                                    save_best_only=True,
                                    save_weights_only=True)

    # Train model
    validation_data = ([X, A], Y_val, idx_val)
    model.fit([X, A],
                Y_train,
                sample_weight=idx_train,
                epochs=epochs,
                batch_size=N,
                validation_data=validation_data,
                shuffle=False,  # Shuffling data means shuffling the whole graph
                callbacks=[es_callback, tb_callback, mc_callback])

    # Load best model
    if isIndependent:
        model.load_weights('./logs/Independent.h5')
    else:
        model.load_weights('./logs/best_model.h5')
   



    y_pred = model.predict([X, A],batch_size=N,verbose=0)

   
    y_pred=y_pred[idx_test][:,1].round(decimals=0)




    return y_pred
