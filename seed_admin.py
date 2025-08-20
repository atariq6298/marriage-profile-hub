from app import create_app, db, bcrypt
from models import User

app = create_app()
with app.app_context():
    # Change these values for your admin user
    username = "admin"
    password = "admin123"
    if not User.query.filter_by(username=username).first():
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        admin_user = User(username=username, password_hash=password_hash, is_admin=True)
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created.")
    else:
        print("Admin user already exists.")