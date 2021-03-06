# GAPDA
PIWI proteins and Piwi-Interacting RNAs (piRNAs) are commonly detected in human cancers, especially in germline and somatic tissues, and correlate with poorer clinical outcomes, suggesting that they play a functional role in cancer. As the problem of combinatorial explosions between ncRNA and disease exposes out gradually, new bioinformatics methods for large-scale identification and prioritization of potential associations are therefore of interest. However, in the real world, the network of interactions between molecules is enormously intricate and noisy, which poses a problem for efficient graph mining. Line graphs can extend many heterogeneous networks to replace dichotomous networks. In this study, we present a new graph neural network framework, line graph attention networks (LGAT). And we apply it to predict PiRNA disease association (GAPDA). In the experiment, GAPDA performs excellently in five-fold cross-validation with the AUC of 0.9038. Not only that, but it still has superior performance compared to methods based on collaborative filtering and attribute features. The experimental results show that GAPDA ensures the prospect of the graph neural network on such problems and can be an excellent supplement for future biomedical research.

# Requirements
* python = 3.6

# Installation
conda install keras=2.2.0 tensorflow=1.10.0

pip install networkx

Installation has been tested in a Windows platform.

# Dataset Description
* A_RNA: the line graph;
* feature0-4: the node features;


# Functions Description
* ```GAPDA.py```: this function can implement the GAPDA algorithm;


# Train and test folds



Constructing the line graph

```python line_graph.py```

Five-fold cross-validation

```python GAPDA.py``` 

All files of Data and Code should be stored in the same folder to run the model.


# easy-to-use model

The default here is to predict the score on the independent test set. If you want to predict other associations, you can add associations in GAPDA/easy-to-use/data/addList.csv and labels in GAPDA/easy-to-use/data/addLabel.csv. If the added association has no labels, then you need to add the same amount of 0 labels to addLabel.csv. If you want to test the independent validation set, you need to modify the sixth line to "isIndependent=True", otherwise modify it to "isIndependent=False". The default is "True".

run the easy-to-use model

```python easy-to-use.py```


