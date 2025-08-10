from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
users = {}

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the User Management API!"})

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET a specific user by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify({user_id: users[user_id]})
    return jsonify({"error": "User not found"}), 404

# POST - Add new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = str(len(users) + 1)  # Simple auto-increment ID
    users[user_id] = data
    return jsonify({"message": "User added", "user_id": user_id}), 201

# PUT - Update existing user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.get_json()
        users[user_id] = data
        return jsonify({"message": "User updated"})
    return jsonify({"error": "User not found"}), 404

# DELETE - Remove a user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
