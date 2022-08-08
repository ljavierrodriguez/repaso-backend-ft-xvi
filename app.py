from crypt import methods
import json
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models import db, User, Profile
from werkzeug.security import generate_password_hash, check_password_hash
import cloudinary
import cloudinary.uploader
import cloudinary.api

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

cloudinary.config(
    cloud_name = "", 
    api_key = "", 
    api_secret = "",
    secure = True
)

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
    
    username = request.form['username']
    password = request.form['password']
    is_active = request.form['is_active']
    picture = request.files['picture']
    
    response = cloudinary.uploader.upload(picture, folder="avatars")
    
    if not response: jsonify({ "msg": "error al subir imagen " })
    
    user = User()
    user.username = username
    user.password = generate_password_hash(password)
    user.is_active = True if is_active == 'true' else False
    user.avatar = response["secure_url"]
    
    profile = Profile()
    user.profile = profile
    
    user.save()
    
    return jsonify(user.serialize()), 201

@app.route('/api/profile', methods=['GET'])
def get_profile():
    pass

@app.route('/api/profile', methods=['PUT'])
def update_profile():
    pass

@app.route('/api/users', methods=['GET'])
def list_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    
    return jsonify(users), 200

if __name__ == '__main__':
    app.run()