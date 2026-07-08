# ZeekData24 Model Training and Testing
Source code, Models, and Datasets used in the research paper entitled:
**Exploratory Data Analysis of UWF-ZeekData24 using Supervised Machine Learning and Deep Learning Techniques**

# Basic Introduction

This study presents an **exploratory data analysis (EDA) on the UWF-ZeekData24 dataset, for which there is limited empirical evidence, to evaluate its capabilities in detecting network intrusions and anomalies.** Several supervised machine learning and deep learning models will be built through training, validation and evaluation of the performance using metrics observed in existing machine learning based-IDS and NIDS such as accuracy, recall, precision, F1-Score, and false positive rate. The research will utilize **Support Vector Machines, Random Forests, Gradient Boosting Trees, and Convolutional Neural Networks** to analyze and classify network traffic data. Lastly, best performing models will be tested on unseen data followed by the performance evaluation using the same metrics mentioned.

# Datasets
1st_Iteration: Datasets was made during the course of THES2, includes 15k MC, SMOTEN MC, Compiled Binary

2st_Iteration: Datasets was revised during the course of THES3 include the usage of different iterations of ZeekData24 which are ZeekData24Fall and ZeekData22Fall.  

# Models
CTTHES2: Models were made during the course of THES2 including different hyperparameter tuning

CTTHES3: Models were revised during the course of THES3 include readjustment of gridsearch parameters, standardization of matplt visualization results, and integration with google colab for faster training.


# Requirements

# Instruction Manual

Note: Deep Learning model CNN is coded to run with GPU, otherwise the Machine Learning(SVM,RF,GBT) models are coded to run with CPU.

