from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Mock database
inventory = [
    {
        "id": 1,
        "status": 1,
        "product": {
            "product_name": "Organic Almond Milk",
            "brands": "Silk",
            "ingredients_text": "Filtered water, almonds, cane sugar",
            "price": 350,
            "stock": 12
        }
    }
]

# Find item by ID
def find_item(item_id):
    return next((item for item in inventory if item["id"] == item_id), None)


# External API call
def fetch_openfoodfacts(search):
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={search}&search_simple=1&action=process&json=1"
    response = requests.get(url, timeout=10)
    
    if response.status_code != 200:
        return None
    
    data = response.json()

    if data.get("products"):
        product = data["products"][0]
        return {
            "product_name": product.get("product_name", "Unknown"),
            "brands": product.get("brands", "Unknown"),
            "ingredients_text": product.get("ingredients_text", "Not available")
        }
    return None


# GET all
@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)


# GET one
@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = find_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)


# POST create
@app.route('/inventory', methods=['POST'])
def add_item():
    data = request.json

    new_item = {
        "id": inventory[-1]["id"] + 1 if inventory else 1,
        "status": 1,
        "product": data
    }

    inventory.append(new_item)
    return jsonify(new_item), 201


# PATCH update
@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    item = find_item(item_id)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.json
    item["product"].update(data)

    return jsonify(item)


# DELETE
@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = find_item(item_id)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    inventory.remove(item)
    return jsonify({"message": "Deleted successfully"})


# External API search
@app.route('/search/<string:name>', methods=['GET'])
def search_api(name):
    product = fetch_openfoodfacts(name)

    if not product:
        return jsonify({"error": "No product found"}), 404

    return jsonify(product)


# IMPORT from API into database (IMPORTANT FOR EXCELLED)
@app.route('/import/<string:name>', methods=['POST'])
def import_product(name):
    product = fetch_openfoodfacts(name)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    new_item = {
        "id": inventory[-1]["id"] + 1 if inventory else 1,
        "status": 1,
        "product": {
            **product,
            "price": 0,
            "stock": 0
        }
    }

    inventory.append(new_item)
    return jsonify(new_item), 201


if __name__ == '__main__':
    app.run(debug=True)