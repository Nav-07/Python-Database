from Api import Api
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy 

# Create the API Objects
api = Api()

# Create the Database
database = SQLAlchemy(api.flask_app) 

class User(database.Model):
	_id = database.Column("id", database.Integer, primary_key=True)
	name = database.Column(database.String(100))
	mail = database.Column(database.String(250))

	def __init__(self, name, mail):
		self.name = name
		self.mail = mail

# Create the Endpoints
@api.flask_app.route('/')
def index():
    return jsonify({'message': 'welcome to user registration service'})

@api.flask_app.route('/user', methods=['POST'])
def user():
    name = request.json['name']
    mail = request.json['mail']

    user = User(name, mail)
    return jsonify({'message': 'record created'}), 201

# Run the Flask App
if __name__ == '__main__':
    api.run_api()
