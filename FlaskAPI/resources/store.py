import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores

blp = Blueprint("stores", __name__, description="Operations on stores")

@blp.route('/store')
class StoreList(MethodView):
    def get(self):
        return {"stores":list(stores.values())}, 200
    
    def post(self):
        store_data = request.get_json()
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
    
@blp.route('/store/<string:store_id>')
class Store(MethodView):
    def get(self, store_id):
        store = stores.get(store_id)
        if store:
            return store, 200
        abort(404, message="Store not found.")
    
    def delete(self, store_id):
        store = stores.pop(store_id, None)
        if store is None:
            return {"message": f"Store {store} deleted."}, 204
        abort(404, message= f"Store {store} not found.")
        