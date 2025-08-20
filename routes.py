from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_app import db, bcrypt
from models import User, Profile

api_bp = Blueprint('api', __name__)

def admin_required(fn):
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user or not user.is_admin:
            return jsonify({"msg": "Admin access required"}), 403
        return fn(*args, **kwargs)
    wrapper.__name__ = fn.__name__
    return jwt_required()(wrapper)

@api_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get('username')).first()
    if user and bcrypt.check_password_hash(user.password_hash, data.get('password')):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    return jsonify(msg="Bad credentials"), 401

@api_bp.route('/users', methods=['POST'])
@admin_required
def add_user():
    data = request.json
    if User.query.filter_by(username=data['username']).first():
        return jsonify(msg="Username already exists"), 400
    password_hash = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password_hash=password_hash, is_admin=data.get('is_admin', False))
    db.session.add(new_user)
    db.session.commit()
    return jsonify(msg="User added"), 201

@api_bp.route('/users', methods=['GET'])
@admin_required
def list_users():
    users = User.query.all()
    result = [{"id": u.id, "username": u.username, "is_admin": u.is_admin} for u in users]
    return jsonify(result)

@api_bp.route('/users/<int:user_id>/make-admin', methods=['PATCH'])
@admin_required
def make_admin(user_id):
    user = User.query.get_or_404(user_id)
    user.is_admin = True
    db.session.commit()
    return jsonify(msg="User promoted to admin")

@api_bp.route('/profiles', methods=['POST'])
@admin_required
def create_profile():
    user_id = get_jwt_identity()
    data = request.json
    profile = Profile(**data, created_by=user_id)
    db.session.add(profile)
    db.session.commit()
    return jsonify(msg="Profile created", id=profile.id), 201

@api_bp.route('/profiles', methods=['GET'])
@jwt_required()
def get_profiles():
    query = Profile.query
    age = request.args.get("age")
    religion = request.args.get("religion")
    cast = request.args.get("cast")
    location = request.args.get("location")

    if age:
        query = query.filter_by(age=int(age))
    if religion:
        query = query.filter_by(religion=religion)
    if cast:
        query = query.filter_by(cast=cast)
    if location:
        query = query.filter_by(village=location)

    profiles = query.all()
    result = [{c.name: getattr(p, c.name) for c in Profile.__table__.columns} for p in profiles]
    return jsonify(result)

@api_bp.route('/profiles/<int:profile_id>', methods=['GET'])
@jwt_required()
def get_profile(profile_id):
    profile = Profile.query.get_or_404(profile_id)
    return jsonify({c.name: getattr(profile, c.name) for c in Profile.__table__.columns})

@api_bp.route('/profiles/<int:profile_id>', methods=['PUT'])
@admin_required
def update_profile(profile_id):
    profile = Profile.query.get_or_404(profile_id)
    data = request.json
    for key, value in data.items():
        setattr(profile, key, value)
    db.session.commit()
    return jsonify(msg="Profile updated")

@api_bp.route('/profiles/<int:profile_id>', methods=['DELETE'])
@admin_required
def delete_profile(profile_id):
    profile = Profile.query.get_or_404(profile_id)
    db.session.delete(profile)
    db.session.commit()
    return jsonify(msg="Profile deleted")
