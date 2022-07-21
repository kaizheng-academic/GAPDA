# GAPDA
PIWI proteins and Piwi-Interacting RNAs (piRNAs) are commonly detected in human cancers, especially in germline and somatic tissues, and correlate with poorer clinical outcomes, suggesting that they play a functional role in cancer. As the problem of combinatorial explosions between ncRNA and disease exposes out gradually, new bioinformatics methods for large-scale identification and prioritization of potential associations are therefore of interest. However, in the real world, the network of interactions between molecules is enormously intricate and noisy, which poses a problem for efficient graph mining. This study aims to make preliminary attempts on bionetwork- based graph mining. In this study, we present a method based on graph attention network to identify potential and biologically significant piRNA-disease associations (PDAs), called GAPDA. The attention mechanism can calculate a hidden representation of an association in the network based on neighbor nodes and assign weights to the input to make decisions. In particular, we introduce the attention-based Graph Neural Networks to the field of piRNA-association prediction for the first time. In the experiment, GAPDA performes excellently in five-fold cross-validation with the AUC of 0.9038. Not only that, but it still has superior performance compared to methods based on collaborative filtering and attribute features. The experimental results show that GAPDA ensures the prospect of the graph neural network on such problems and can be an excellent supplement for future biomedical research.

# Requirements
* python = 3.6

# Installation
pip install -r requirements.txt

GAPDA can be downloaded by
```
git clone https://github.com/kaizheng-academic/GAPDA
```
Installation has been tested in a Windows platform.

# Dataset Description
* A: the line graph;
* feature: the node features;


# Functions Description
* ```gat.py```: this function can implement the GAPDA algorithm;






