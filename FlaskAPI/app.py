import uuid
from flask import Flask, request
from flask_smorest import abort
from db import items, stores

app = Flask(__name__)


def get_request():
    return request.get_json()
    
@app.get('/')
def hello_app():
    return {"message":"Hello from app"}, 200

@app.get('/store')
def get_stores():
    return {"stores":list(stores.values())}, 200

@app.post('/store')
def create_store():
    store_data = get_request()
    if "name" not in store_data:
        abort(
            400,
            message="Bad request. some key information missing in JSON payload.")
    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(400, message=f"Store {store["name"]} already exists.")
    store_id = uuid.uuid4().hex
    store  = {**store_data,'id':store_id}
    stores[store_id] = store
    return store, 201

@app.post('/item')
def create_item():
    item_data = get_request()
    if(
        "price" not in item_data or
        "store_id" not in item_data or
        "name" not in item_data
    ):
        abort(
            400,
            message="Bad request. some key information missing in JSON payload.")
    for item in items.values():
        if(
            item_data["name"] == item["name"] and
            item_data["store_id"] == item["store_id"]
        ):
            abort(400, message=f"item {item["name"]} already exists.")
    
    if item_data["store_id"] not in stores:
        abort(404,message="Store not found.")
    item_id = uuid.uuid4().hex
    item = {**item_data, 'id':item_id}
    items[item_id] = item
    return item, 201

@app.get('/item')
def get_all_items():
    return {"items":list(items.values())}, 200

@app.get("/store/<string:store_id>")
def get_store(store_id):
    store = stores.get(store_id)
    if store:
            return store, 200
    abort(404, message="Store not found.")

@app.get("/item/<string:item_id>")
def get_item(item_id):
    item = items.get(item_id)
    if item:
        return item, 200
    abort(404, message="Item not found.")
    