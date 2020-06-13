from flask import Flask, request, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
import os

# Create the Flask Object
app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']

db = SQLAlchemy(app)

# The Model
class User(db.Model):
	_id = db.Column("id", db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	mail = db.Column(db.String(250))

	def json(self):
		return {
			"name": self.name,
			"mail": self.mail
		}

# Create the Endpoints
@app.route('/')
def index():
	return 'User Registration System'

@app.route('/user', methods=['POST'])
def user():
	name = request.json['name']
	mail = request.json['mail']

	usr = User(name=name, mail=mail)
	db.session.add(usr)
	db.session.commit()

	return jsonify({'message': 'record created'}), 201

@app.route('/users', methods=['GET'])
def get_users():
	users = []
	for user in User.query.all():
		users.append(user.json())
	return jsonify(users)

# Run the flask app
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=51)