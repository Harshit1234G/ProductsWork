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
````

Clone the repo and run the app:

```bash
uvicorn main:app --reload
```


## 🔌 API Endpoint

### **POST /predict**

Send flower measurements in JSON format:

#### ✅ Sample Request:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

#### 📤 Sample Response:

```json
{
  "prediction": "Setosa",
  "probas": [0.97, 0.02, 0.01]
}
```

### 📚 Swagger Docs

Once the app is running, visit:

* [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) → Swagger UI
* [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) → ReDoc

## **📜 License**  
This project is licensed under the **Apache 2.0 License** – see the [LICENSE](https://github.com/Harshit1234G/ProductsWork/blob/master/LICENSE.txt) file for details.  
