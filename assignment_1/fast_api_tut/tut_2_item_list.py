from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn


app = FastAPI()
items = []


class Item(BaseModel):
    text: str
    is_done: bool = False


@app.get('/', response_model= dict[str, str])
def root():
    return {'Hello': 'World'}


@app.post('/items', response_model= list[Item])
def create_item(item: Item):
    items.append(item)
    return items


@app.get('/items', response_model= list[Item])
def list_items(limit: int = 10):
    return items[0:limit]


@app.get('/items/{index}', response_model= Item)
def get_item(index: int):
    if index < len(items):
        return items[index]
    
    else:
        raise HTTPException(status_code= 404, detail= f'Item with index {index} not found.')


if __name__ == '__main__':
    uvicorn.run(app)
