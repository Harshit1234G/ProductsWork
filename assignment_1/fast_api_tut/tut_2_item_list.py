from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn


app = FastAPI()
items = []


class Item(BaseModel):
    text: str
    is_done: bool = False


@app.get('/')
def root() -> dict[str, str]:
    return {'Hello': 'World'}


@app.post('/items')
def create_item(item: Item) -> list[Item]:
    items.append(item)
    return items


@app.get('/items')
def list_items(limit: int = 10):
    return items[0:limit]


@app.get('/items/{index}')
def get_item(index: int) -> str:
    if index < len(items):
        return items[index]
    
    else:
        raise HTTPException(status_code= 404, detail= f'Item with index {index} not found.')


if __name__ == '__main__':
    uvicorn.run(app)
