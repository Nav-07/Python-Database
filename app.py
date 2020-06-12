from Api import Api
from flask import Flask, jsonify, request

# Create the API Objects
api = Api()

# Create the Endpoints
@api.flask_app.route('/')
def index():
    return jsonify({'message': 'welcome to user registration service'})

# Run the Flask App
if __name__ == '__main__':
    api.run_api()
