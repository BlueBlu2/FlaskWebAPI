from flask import Flask

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
@app.get('/')
def hello_app():
    return "Hello from app"

@app.get('/store')
def get_stores():
    return {"stores":stores}