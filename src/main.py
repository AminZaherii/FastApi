from fastapi import FastAPI
import controller
from models import Category

app = FastAPI()


@app.get('/')
def welcome():
    return 'Welcome to FastApi app'


@app.get('/categories')
def get_categories():
    return controller.get_categories()


@app.post('/categories/add')
async def add_category(category: Category):
    return controller.add_category(category)


@app.get('/categories/{category_id}')
def get_category_by_id(category_id):
    return controller.get_category_by_id(category_id)

# items = []
#
#
# @app.post('/items/<item>')
# def add_item(item):
#     items.append(item)
#     return items
#
#
# @app.get('/items/{item_id}')
# def get_item(item_id):
#     return items[int(item_id)]
