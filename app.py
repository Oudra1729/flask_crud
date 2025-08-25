from flask import Flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return "Connection between Flask and PostgreSQL successful"
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append({"id": user.id, "name": user.name})
    return jsonify(result)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully!"})

@app.route('/update_user/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    user.name = data['name']
    db.session.commit()

    return jsonify({"message": "User updated successfully!"})

@app.route('/delete_user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully!"})


if __name__ == '__main__':
    app.run(debug=True)
