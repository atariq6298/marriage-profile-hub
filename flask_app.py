from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__, static_folder='frontend', static_url_path='')
    app.config['SECRET_KEY'] = 'your-very-secure-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marriage_profiles.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your-very-secure-jwt-secret-key'
    
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    # Route to serve the frontend
    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    return app

app = create_app()  # <-- This is crucial for WSGI!
