# ZeekData24 Model Training and Testing

Source code, Models, and Datasets used in the research paper entitled:
**Exploratory Data Analysis of UWF-ZeekData24 using Supervised Machine Learning and Deep Learning Techniques**.

by @aabaniel, @Disavowedd, and @jaybreezy

## Basic Introduction

This study presents an **exploratory data analysis (EDA) on the UWF-ZeekData24 dataset, for which there is limited empirical evidence, to evaluate its capabilities in detecting network intrusions and anomalies.** Several supervised machine learning and deep learning models will be built through training, validation and evaluation of the performance using metrics observed in existing machine learning based-IDS and NIDS such as accuracy, recall, precision, F1-Score, and false positive rate. The research will utilize **Support Vector Machines, Random Forests, Gradient Boosting Trees, and Convolutional Neural Networks** to analyze and classify network traffic data. Lastly, best performing models will be tested on unseen data followed by the performance evaluation using the same metrics mentioned.

Primary Reference: Elam, M., Mink, D., Bagui, S. S., Plenkers, R., & Bagui, S. C. (2025). Introducing UWF-ZeekData24: An Enterprise MITRE ATT&CK Labeled Network Attack Traffic Dataset for Machine Learning/AI. Data, 10(5), 59. https://doi.org/10.3390/data10050059

## Datasets

The Primary Dataset used was the accessible versions of UWF-ZeekData24 and supplementary datasets such as UWF-ZeekData24Fall and UWF-ZeekData22Fall

- The UWF-ZeekData24, UWF-ZeekData24Fall, and UWF-ZeekData22Fall datasets are available in: https://datasets.uwf.edu

### Dataset Iterations and Descriptions

1st Iteration: Datasets was made during the course of THES2, includes 15k MC, SMOTEN MC, Compiled Binary

2nd Iteration: Datasets was revised during the course of THES3 include the usage of different iterations of ZeekData24 which are ZeekData24Fall and ZeekData22Fall.

## Models

The Machine and Deep Learning Algorithms implemented in the project are as follows:

1. [Support Vector Machines (Linear Support Vector Classification)](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html)
1. [Random Forest (Random Forest Classifier)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
1. [Gradient Boosting Tree (Gradient Boosting Classifier)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html)
1. [Convolutional Neural Network](https://www.tensorflow.org/tutorials/images/cnn)

### Model Iterations and Descriptions

1st Iteration: Models were made during the course of THES2 including different hyperparameter tuning

2nd Iteration: Models were revised during the course of THES3 include readjustment of gridsearch parameters, standardization of matplt visualization results, and integration with google colab for faster training.

## Requirements

Libaries Included:

pandas, numpy, matplotlib, sklearn, imblearn, tensorflow, skopt, scikeras, keras

Tools Needed:

Anaconda _(Python, Jupyter Notebook)_

## Instruction Manual

Note: Deep Learning model CNN is coded to run with GPU, otherwise the Machine Learning(SVM,RF,GBT) models are coded to run with CPU.

All models were implemented within a Python-based Jupyter Notebook.

**To run, click on the 'run' button in the toolbar of the Jupyter Notebook UI**

## AI Usage Declaration

During the Pre-Training phase of this thesis, We utilized ChatGPT and Google Gemini to assist in program debugging and Google Collab setup.

