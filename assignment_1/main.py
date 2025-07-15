import uvicorn
import pickle
from fastapi import FastAPI
from pydantic import BaseModel


class Flower(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


app = FastAPI()

with open('iris_classifier_dt.pkl', 'rb') as f:
    model = pickle.load(f)


@app.post('/predict')
def predict(data: Flower):
    test_data = [
        [
            data.sepal_length, 
            data.sepal_width, 
            data.petal_length, 
            data.petal_width
        ]
    ]

    class_idx = model.predict(test_data)[0]
    probas = list(model.predict_proba(test_data)[0])
    classes = ['Setosa', 'Versicolor', 'Virginica']
    
    return {'prediction': classes[class_idx], 'probas': probas}

if __name__ == '__main__':
    uvicorn.run(app)
