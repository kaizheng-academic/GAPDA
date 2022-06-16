from __future__ import print_function

import os
import pickle as pkl
import sys
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
    ReadMyCsv(A, "A.csv")
    A=np.array(A).astype(float)
    adj=sparse.csr_matrix(A)

    feature = []
    ReadMyCsv(feature, "feature.csv")
    feature = np.array(feature).astype(float)
    features=sparse.csr_matrix(np.array(feature)).tolil()

    train0_label = []
    ReadMyCsv(train0_label, "train0_label.csv")
    test0_label = []
    ReadMyCsv(test0_label, "test0_label.csv")
    val_label = []
    ReadMyCsv(val_label, "val_label.csv")
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
