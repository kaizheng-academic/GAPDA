from __future__ import print_function

import os
import pickle as pkl
import sys
from tkinter import Label
from scipy import sparse
import networkx as nx
import numpy as np
import scipy.sparse as sp
def ReadMyCsv(SaveList, fileName):
    import csv
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:  # 把每个rna疾病对加入OriginalData，注意表头
        SaveList.append(row)
    return

def StorFile(data, fileName):
    import csv
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerows(data)
    return

def parse_index_file(filename):
    """Parse index file."""
    index = []
    for line in open(filename):
        index.append(int(line.strip()))
    return index


def sample_mask(idx, l):
    """Create mask."""
    mask = np.zeros(l)
    mask[idx] = 1
    test = []



    return np.array(mask, dtype=np.bool)


def load_data():
    """Load data."""

    A = []
    ReadMyCsv(A, "./data/A.csv")
    A=np.array(A).astype(float)
    adj=sparse.csr_matrix(A)

    feature = []
    ReadMyCsv(feature, "./data/feature_new.csv")
    feature = np.array(feature).astype(float)
    features=sparse.csr_matrix(np.array(feature)).tolil()

    train0_label = []
    ReadMyCsv(train0_label, "./data/train_label.csv")
    test0_label = []
    ReadMyCsv(test0_label, "./data/test_label.csv")
    val_label = []
    ReadMyCsv(val_label, "./data/val_label.csv")
    train_mask=[]
    val_mask = []
    test_mask = []
    for i in range(len(train0_label)):


        if train0_label[i]==val_label[0]:
            train_mask.append(False)
        else:
            train_mask.append(True)
        if val_label[i]==val_label[0]:
            val_mask.append(False)
        if test0_label[i]==val_label[0]:
            test_mask.append(False)
        else:
            test_mask.append(True)
    y_train=np.array(train0_label).astype(float)
    y_test = np.array(test0_label).astype(float)
    y_val = np.array(val_label).astype(float)
    train_mask=np.array(train_mask)
    test_mask=np.array(test_mask)
    val_mask=np.array(val_mask)


    return adj, features, y_train, y_val, y_test, train_mask, val_mask, test_mask


def preprocess_features(features):
    """Row-normalize feature matrix and convert to tuple representation"""
    rowsum = np.array(features.sum(1))
    r_inv = np.power(rowsum, -1).flatten()
    r_inv[np.isinf(r_inv)] = 0.
    r_mat_inv = sp.diags(r_inv)
    features = r_mat_inv.dot(features)
    return features.todense()

def feature():
    List=[]
    ReadMyCsv(List, './data/piRNA_feature.csv')
    piRNA_feature=List

    List=[]
    ReadMyCsv(List, './data/disease_feature.csv')
    disease_feature=List


    List=[]
    ReadMyCsv(List, './data/feature.csv')
    feature=List

    List=[]
    ReadMyCsv(List, './data/FeatureList.csv')
    FeatureList=List

    List=[]
    ReadMyCsv(List, './data/Label.csv')
    Label=[i[0] for i in List]



    List=[]
    ReadMyCsv(List, './data/piRNA.csv')
    piRNAList=[i[0] for i in List]

    List=[]
    ReadMyCsv(List, './data/disease.csv')
    diseaseList=[i[0] for i in List]

    List=[]
    ReadMyCsv(List, './data/addList.csv')
    addList= List

    List=[]
    ReadMyCsv(List, './data/addLabel.csv')
    addLabel=[i[0] for i in List]

    newfeature=[]
    
    for i in addList:
        tmp=[]
        tmp.extend(piRNA_feature[piRNAList.index(i[0])])
        tmp.extend(disease_feature[diseaseList.index(i[1])])
        feature.append(tmp)
        

    
    FeatureList.extend(addList)

    train_label=[]
    for i in Label:
        if i=='1.0':
            train_label.append([0,1])
        else:
            train_label.append([1,0])
    
    test_label=[[0,0] for i in range(len(train_label))]
    train_label.extend([[0,0] for i in range(len(addList))]) 
    val_label=[[0,0] for i in range(len(train_label))]


    
    for i in addLabel:
        if i=='0':
            test_label.append([1,0])
        else:
            test_label.append([0,1])
    

    StorFile(val_label, './data/val_label.csv')
    StorFile(test_label, './data/test_label.csv')
    StorFile(train_label, './data/train_label.csv')
    StorFile(feature, './data/feature_new.csv')
    StorFile(FeatureList, './data/FeatureList_new.csv')
    linegraph()


def linegraph():
    List=[]
    ReadMyCsv(List, './data/FeatureList_new.csv')
    FeatureList=List

    A=np.zeros((len(FeatureList),len(FeatureList)))

    for i in FeatureList:

        for j in FeatureList:




            
                if  i[0].lower()==j[0].lower():
                    A[FeatureList.index(i)][FeatureList.index(j)] = 1
                    A[FeatureList.index(j)][FeatureList.index(i)] = 1
                    




    StorFile(A, "./data/A.csv")