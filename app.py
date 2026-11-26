from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database simulation
items = [
    {"id": 1, "name": "菠蘿油", "price": 20},
    {"id": 2, "name": "西多士", "price": 20},
    {"id": 3, "name": "蛋牛治", "price": 20},
    {"id": 4, "name": "火腿通粉", "price": 138},
    {"id": 5, "name": "乾炒牛河", "price": 60},
]

# GET Request - Fetch all items
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# GET Request - Fetch a specific item by ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200

# POST Request - Create a new item
@app.route('/api/items', methods=['POST'])
def create_item():
    # Verify the request payload is JSON
    if not request.is_json:
        return jsonify({"error": "Request body must be JSON"}), 400

    data = request.get_json()

    # Simple data validation
    if "name" not in data or "price" not in data:
        return jsonify({"error": "Missing required fields: name, price"}), 400

    new_item = {
        "method": len(items) + 1,
        "name": data["name"],
        "price": data["price"]
    }
    items.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    # Runs the local development server
    app.run(debug=True, port=5000)
