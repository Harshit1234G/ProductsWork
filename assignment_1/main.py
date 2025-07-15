import uvicorn
import pickle
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# for input
class Flower(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# for output
class PredictionResponse(BaseModel):
    prediction: str
    probas: list[float]


app = FastAPI()

# Load the trained model from a pickle file during app startup
with open('iris_classifier_dt.pkl', 'rb') as f:
    model = pickle.load(f)      # This is a decision tree classifier trained on the Iris dataset


@app.post('/predict', response_model= PredictionResponse)
def predict(data: Flower):
    """
    Predict the Iris flower species based on input features.

    Args:
        data (Flower): A JSON body with sepal and petal measurements.

    Returns:
        PredictionResponse: Contains predicted class name and probability list.
    """
    # Raising Internal Server Error if model is not loaded
    if model is None:
        raise HTTPException(status_code= 500, detail= 'Model not loaded')
    
    # Prepare test data in the expected 2D format for the model
    test_data = [
        [
            data.sepal_length, 
            data.sepal_width, 
            data.petal_length, 
            data.petal_width
        ]
    ]

    try: 
        # Get the index of the predicted class
        class_idx = model.predict(test_data)[0]

        # Get prediction probabilities for all classes
        probas = list(model.predict_proba(test_data)[0])

    except Exception as e:
        # Bad Request error: The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).
        raise HTTPException(status_code= 400, detail= f'Prediction failed: {e}')

    # Map index to actual class name
    classes = ['Setosa', 'Versicolor', 'Virginica']
    
    # Return prediction and associated probabilities
    return {'prediction': classes[class_idx], 'probas': probas}


if __name__ == '__main__':
    # Run the app using Uvicorn if this script is executed directly
    uvicorn.run(app)
