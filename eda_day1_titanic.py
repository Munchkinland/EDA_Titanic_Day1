# -*- coding: utf-8 -*-
"""EDA_Day1_Titanic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z52EskkpDQwc_exsah9SL-NYKV-Ahhrc

EDA 👉 Day 1 = Paso 1: Planteamiento del problema y recopilación de datos
"""

import pandas as pd

# Read the training, testing, and survival data
train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")
test_survived_data = pd.read_csv("gender_submission.csv")

# Add the "Survived" column to the test data
test_data["Survived"] = test_survived_data["Survived"]

# Concatenate the training and test data
total_data = pd.concat([train_data, test_data], ignore_index=True)

# Drop the "index" column (if it exists)
total_data.drop(columns=["index"], inplace=True, errors='ignore')

# Display the first few rows of the data
total_data.head()

# Show the shape (number of rows and columns) of the data
total_data.shape

# Display information about the data, such as column data types and missing values
total_data.info()

# Count duplicated rows (excluding the "PassengerId" column)
total_data.drop("PassengerId", axis=1).duplicated().sum()

# Remove duplicated rows (excluding the "PassengerId" column)
total_data = total_data.drop_duplicates(subset=total_data.columns.difference(['PassengerId']))
print(total_data.shape)

# Check and remove completely duplicated rows in the data
if total_data.duplicated().sum():
    total_data = total_data.drop_duplicates()
print(total_data.shape)

# Drop unnecessary columns ("PassengerId", "Name", "Ticket", "Cabin")
total_data.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1, inplace=True)

# Import the Matplotlib and Seaborn libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Create a figure with 2 rows and 3 columns
fig, axis = plt.subplots(2, 3, figsize=(10, 7))

# Create histograms for the categorical variables "Survived," "Sex," "Pclass," "Embarked," "SibSp," "Parch,"
# and make some customizations
sns.histplot(ax=axis[0, 0], data=total_data, x="Survived").set_xlim(-0.1, 1.1)
sns.histplot(ax=axis[0, 1], data=total_data, x="Sex").set(ylabel=None)
sns.histplot(ax=axis[0, 2], data=total_data, x="Pclass").set(ylabel=None)
sns.histplot(ax=axis[1, 0], data=total_data, x="Embarked")
sns.histplot(ax=axis[1, 1], data=total_data, x="SibSp").set(ylabel=None)
sns.histplot(ax=axis[1, 2], data=total_data, x="Parch").set(ylabel=None)

# Adjust the layout of the figure
plt.tight_layout()

# Show the plot
plt.show()

# Create a figure with 2 rows and 2 columns, with a custom height ratio
fig, axis = plt.subplots(2, 2, figsize=(10, 7), gridspec_kw={'height_ratios': [6, 1]})

# Create histograms and box plots for "Fare" and "Age"
sns.histplot(ax=axis[0, 0], data=total_data, x="Fare").set(xlabel=None)
sns.boxplot(ax=axis[1, 0], data=total_data, x="Fare")
sns.histplot(ax=axis[0, 1], data=total_data, x="Age").set(xlabel=None, ylabel=None)
sns.boxplot(ax=axis[1, 1], data=total_data, x="Age")

# Adjust the layout of the figure
plt.tight_layout()

# Show the plot
plt show()
