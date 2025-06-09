from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        'name':'My store',
        'items':[
            {
                'item_name':"Chair",
                'item_price':15.99
            }
        ]
    }
]

def get_request():
    return request.get_json()
    
@app.get('/')
def hello_app():
    return "Hello from app"

@app.get('/store')
def get_stores():
    return {"stores":stores}

@app.post('/store')
def create_store():
    request_data = request.get_json()
    new_store  = {'name': request_data['name'], 'items':[]}
    stores.append(new_store)
    return new_store, 201

@app.post('/store/<string:name>/item')
def create_item(name):
    data = get_request()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name":data['name'],
                "price":data['price']
            }
            store['items'].append(new_item)
            return new_item, 201
    return {"message":"Store not found"}, 404