from fastapi import FastAPI
import uvicorn

# create a fast api application
app = FastAPI()

# defining a route ("/")
# Explanation: @app.get("/") tells FastAPI to handle HTTP GET requests sent to the root URL (/) by executing the function below it (read_root).
@app.get('/')
def read_root():
    return {'message': 'Hello, FastAPI!'}


@app.get('/welcome')
def welcome_user(name: str):
    return {'message': f'Welcome, {name}!'}


# Explanation: This code creates a POST endpoint /greet that takes a string name and returns a greeting message like "Hello, name!" as JSON.

# Similarly, we can perform different CRUD operations like PUT, PATCH and DELETE using FastAPI.

@app.post('/greet')
def greet_user(name: str):
    return {'message': f'Hello, {name}!'}



if __name__ == '__main__':
    uvicorn.run(app, host= '127.0.0.1', port= 8000)   
    # or can use the command uvicorn <file_name>:app -- reload
