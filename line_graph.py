# -*- coding: utf-8 -*
import csv

import numpy as np

def ReadMyCsv(SaveList, fileName):

    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:  
        for i in range(len(row)):
            try:
                row[i] = float(row[i])
            except:
                pass

        SaveList.append(row)
    return

def StorFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return



if __name__ == "__main__":


    FeatureList=[]

    ReadMyCsv(FeatureList, "FeatureList.csv")

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








