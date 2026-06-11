# app.py

from flask import Flask, jsonify, request
from inventory import inventory

app = Flask(__name__)

# GET all inventory items
@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200


# GET single inventory item
@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


# POST new inventory item
@app.route("/inventory", methods=["POST"])
def add_item():
    data = request.get_json()

    new_item = {
        "id": len(inventory) + 1,
        "name": data["name"],
        "brand": data["brand"],
        "price": data["price"],
        "stock": data["stock"],
        "barcode": data["barcode"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201


# PATCH inventory item
@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    data = request.get_json()

    for item in inventory:
        if item["id"] == item_id:

            item["name"] = data.get("name", item["name"])
            item["brand"] = data.get("brand", item["brand"])
            item["price"] = data.get("price", item["price"])
            item["stock"] = data.get("stock", item["stock"])
            item["barcode"] = data.get("barcode", item["barcode"])

            return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


# DELETE inventory item
@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):

    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return jsonify({"message": "Item deleted"}), 200

    return jsonify({"error": "Item not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)