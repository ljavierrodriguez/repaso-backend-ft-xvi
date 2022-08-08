from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'

CORS(app)

@app.route('/')
def main():
    return jsonify({ "msg": "API Rest Flask"}), 200

if __name__ == '__main__':
    app.run()