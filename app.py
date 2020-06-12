from Api import Api
from flask import Flask, jsonify, request
from User import User

# Create the API Objects
api = Api()

# Create the Endpoints
@api.flask_app.route('/')
def index():
    return jsonify({'message': 'welcome to user registration service'})

@api.flask_app.route('/user', methods=['POST'])
def user():
    if request.method == 'POST':
        mail = request.json['mail']

        user = User(mail)
        api.database.insert_user(user)

        return jsonify({'message': 'record created'}), 201

# Run the Flask App
if __name__ == '__main__':
    api.run_api()
