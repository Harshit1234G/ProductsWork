# Importing FastAPI to create the web API and HTTPException to handle errors
from fastapi import FastAPI, HTTPException

# Importing BaseModel from pydantic for data validation and serialization
from pydantic import BaseModel

# Importing uvicorn for running the FastAPI app as an ASGI server
import uvicorn


# Creating an instance of the FastAPI class (our main app object)
app = FastAPI()

# An in-memory list to store all items (will be lost once server restarts)
items = []


# Defining the data model (schema) for an item using Pydantic
class Item(BaseModel):
    """
    Item schema:
    - text (str): Description or name of the task/item
    - is_done (bool): Status of the task; defaults to False
    """
    text: str
    is_done: bool = False


@app.get('/', response_model= dict[str, str])
def root():
    """
    Root endpoint of the API.
    Returns a simple greeting message as a JSON dictionary.

    Returns:
        dict[str, str]: A message like {"Hello": "World"}
    """
    return {'Hello': 'World'}


@app.post('/items', response_model= list[Item])
def create_item(item: Item):
    """
    Endpoint to create a new item.

    Args:
        item (Item): A JSON object with `text` and optional `is_done` field.

    Returns:
        list[Item]: A list of all items after appending the new one.
    """
    items.append(item)
    return items


@app.get('/items', response_model= list[Item])
def list_items(limit: int = 10):
    """
    Endpoint to retrieve a limited number of items.

    Query Parameters:
        limit (int): Maximum number of items to return. Default is 10.

    Returns:
        list[Item]: A list of up to `limit` items.
    """
    return items[0:limit]


@app.get('/items/{index}', response_model= Item)
def get_item(index: int):
    """
    Endpoint to get a single item by its index.

    Path Parameters:
        index (int): The index of the item in the list.

    Returns:
        Item: The item at the given index if it exists.

    Raises:
        HTTPException: If the index is out of range (item not found).
    """
    if index < len(items):
        return items[index]
    else:
        # Raise 404 error if index is invalid
        raise HTTPException(status_code= 404, detail= f'Item with index {index} not found.')


# Main entry point for running the app directly (useful for development)
if __name__ == '__main__':
    # Launch the app with Uvicorn server on default host (127.0.0.1) and port (8000)
    uvicorn.run(app)
