import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items,stores

blp = Blueprint("Items", __name__, description="Operations on items")

@blp.route('/item/<string:item_id>')
class Item(MethodView):
    def get(self, item_id):
        item = items.get(item_id)
        if item:
            return item, 200
        abort(404, message="Item not found.")
    
    def delete(self, item_id):
        item = items.pop(item_id, None)
        if item is None:
            return {"message": f"Item {item} deleted."}, 204
        abort(404, message= f"Item {item} not found.")
        
    def put(self, item_id):
        item_data = request.get_json()
        if "price" not in item_data or "name" not in item_data:
            abort(
                400,
                message="Bad request. Ensure 'price' and 'name' are included in the JSON payload"
            )
        item = items.get(item_id)
        if item:
            item |= item_data
            return item, 200
        abort(404, mesage="Item not found.")
        
@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return items.values(),200

    def post(self):
        item_data = request.get_json()
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
    
        # if item_data["store_id"] not in stores:
        #     abort(404,message="Store not found.")
        item_id = uuid.uuid4().hex
        item = {**item_data, 'id':item_id}
        items[item_id] = item
        return item, 201
