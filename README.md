# 🌸 Iris Species Prediction API with FastAPI

This project demonstrates how to deploy a machine learning model using **FastAPI**. The model is trained on the classic **Iris dataset** and provides predictions based on sepal and petal dimensions.


## 📦 Features

- Trained **Decision Tree Classifier** using scikit-learn
- RESTful API built with **FastAPI**
- Input validation using **Pydantic**
- Prediction response includes both class name and class probabilities
- Swagger UI for easy API testing



## 📊 Dataset Overview

- 150 samples, 3 classes (Setosa, Versicolor, Virginica)
- 4 numerical features:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width

Dataset Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris)



## ⚙️ Installation

Make sure Python 3.7+ is installed.

```bash
pip install fastapi uvicorn pydantic scikit-learn
