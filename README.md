# Tiger Population Estimation
This project is a part of ISI DataFest Integration 2023, which aims to predict the number of tigers in a given dataset using machine learning algorithms. The dataset contains information about different tiger sightings, including the location, soil type, and other environmental factors.

To predict the number of tigers, the project uses two main techniques: Supervised K-Nearest Neighbor (KNN) clustering and feature selection using the Logit function. Supervised KNN is a clustering algorithm that is useful when labeled data is expensive or impossible to obtain. It can achieve high accuracy in a wide variety of prediction-type problems. The Logit function, on the other hand, is a useful technique for predicting binary outcomes, such as whether a tiger is unique or not.

The project first loads the training dataset, which contains labeled data, and splits it into training and testing sets. It then trains the KNN model on the training set and tests its accuracy on the testing set. Once the model is trained, it is used to predict the number of tigers in a new dataset using the KNN algorithm.

To further improve the accuracy of the prediction, the project uses feature selection techniques to identify the most useful features in the dataset. Specifically, it applies the Logit function to the dataset and examines the regression summary to determine which features have the most significant impact on the outcome variable (i.e., whether a tiger is unique or not). These features are then used to refine the KNN model and improve its accuracy.

Overall, this project demonstrates how machine learning algorithms can be used to predict the number of tigers in a given dataset. By combining KNN clustering and feature selection techniques, it achieves high accuracy in predicting the number of unique tigers in the dataset.

## Getting Started

To get started with this project, you will need to clone the repository to your local machine and install the required libraries using pip. Download the dataset from the kaggle page [here](https://www.kaggle.com/competitions/im-hard-to-spot/data) or alternatively, using the kaggle API* use:
```
kaggle competitions download -c im-hard-to-spot
```
*You can follow the instructions in [this](https://github.com/Kaggle/kaggle-api) repo to set up the API.

## Prerequisites

You will need the following libraries:
  - pandas 
  - sklearn 
  - statsmodels
  - matplotlib
  - seaborn

You can install them using pip:
```
pip install pandas sklearn statsmodels matplotlib seaborn
```
Alternatively use the below command after cloning the repo:
```
pip install -r requirements.txt
```

## Installing

To install this project, simply clone the repository to your local machine:
```
git clone https://github.com/your-username/your-repository.git
```

## License

This project is licensed under the [MIT](LICENSE) license.
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Arg-10/Tiger-Population-Estimation/blob/main/LICENSE)

## Acknowledgments

  - ISI DataFest Integration 2023
