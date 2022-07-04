# -*- coding: utf-8 -*
import csv

import numpy as np





if __name__ == "__main__":


    FeatureList=[]

    ReadMyCsv(FeatureList, "FeatureList.csv")
    Label=[]

    ReadMyCsv(Label, "Label.csv")
    A=np.zeros((len(FeatureList),len(FeatureList)))
    A2 = np.zeros((len(FeatureList), len(FeatureList)))
    A3 = np.zeros((len(FeatureList), len(FeatureList)))
    for i in FeatureList:

        for j in FeatureList:




                if  i[1].lower()==j[1].lower():
                    A2[FeatureList.index(i)][FeatureList.index(j)] = 1
                    A2[FeatureList.index(j)][FeatureList.index(i)] = 1
                    A3[FeatureList.index(i)][FeatureList.index(j)] = 1
                    A3[FeatureList.index(j)][FeatureList.index(i)] = 1
                if  i[0].lower()==j[0].lower():
                    A[FeatureList.index(i)][FeatureList.index(j)] = 1
                    A[FeatureList.index(j)][FeatureList.index(i)] = 1
                    A3[FeatureList.index(i)][FeatureList.index(j)] = 1
                    A3[FeatureList.index(j)][FeatureList.index(i)] = 1




    StorFile(A, "A_RNA.csv")
    StorFile(A2, "A_disease.csv")
    StorFile(A3, "A_RNA+disease.csv")








