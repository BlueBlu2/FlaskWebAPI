import uuid
from flask import Flask, request
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
    store_id = uuid.uuid4().hex
    store  = {**store_data,'id':store_id}
    stores[store_id] = store
    return store, 201

@app.post('/item')
def create_item():
    item_data = get_request()
    if item_data["store_id"] not in stores:
        return {"message":"Store not found"}, 404
    item_id = uuid.uuid4().hex
    item = {**item_data, 'id':item_id}
    return item, 201

@app.get('/item')
def get_all_items():
    return {"items":list(items.values())}

@app.get("/store/<string:store_id>")
def get_store(store_id):
    store = stores.get(store_id)
    if store:
            return store, 200
    return {"message":"Store not found"}, 404

@app.get("/item/<string:item_id>")
def get_item(item_id):
    item = items.get(item_id)
    if item:
        return item, 200
    return {"message":"Store not found"}, 404
    