from fastapi import FastAPI
import uvicorn


app = FastAPI()
items = []


@app.get('/')
def root() -> dict[str, str]:
    return {'Hello': 'World'}


@app.post('/items')
def create_item(item: str) -> list[str]:
    items.append(item)
    return items


@app.get('/items/{item_id}')
def get_item(item_id: int) -> str:
    item = items[item_id]
    return item


if __name__ == '__main__':
    uvicorn.run(app)
