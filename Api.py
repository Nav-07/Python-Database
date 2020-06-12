from flask import Flask, request, jsonify

class Api:
    def __init__(self):
        self.flask_app = Flask(__name__)

        # Configure the Flask App
        self.flask_app.config['JSON_SORT_KEYS'] = False

    def run_api(self):
        self.flask_app.run(debug=True, host='0.0.0.0', port=51)