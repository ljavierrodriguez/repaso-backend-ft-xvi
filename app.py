from crypt import methods
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models import db

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
Migrate(app, db)
CORS(app)

@app.route('/')
def main():
    return jsonify({ "msg": "API Rest Flask"}), 200

@app.route('/api/login', methods=['POST'])
def login():
    pass

@app.route('/api/register', methods=['POST'])
def register():
    pass

@app.route('/api/profile', methods=['GET'])
def get_profile():
    pass

@app.route('/api/profile', methods=['PUT'])
def update_profile():
    pass


if __name__ == '__main__':
    app.run()