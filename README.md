# Marriage Profile Hub

A Flask-based API for managing marriage profiles with admin-only modification privileges, featuring a simple JavaScript frontend dashboard.

## Features
- JWT authentication for users
- Only admins can add, edit, or delete profiles
- All authenticated users can view and filter profiles
- User management endpoints for admins
- **Simple JavaScript frontend dashboard for easy profile browsing**

## Quick Start

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Initialize the database:
   ```python
   from app import create_app, db
   app = create_app()
   with app.app_context():
       db.create_all()
   ```

3. Seed an admin user:
   ```
   python seed_admin.py
   ```

4. Run the server:
   ```
   python app.py
   ```

5. **Access the frontend at: http://localhost:5000**

6. See `DEPLOYMENT_STEPS.md` for deployment instructions.

## Frontend Dashboard

The frontend is located at `frontend/index.html` and provides:

- **Login Interface**: Secure authentication using JWT tokens
- **Profile Dashboard**: Browse all marriage profiles in a clean grid layout
- **Advanced Filtering**: Filter profiles by age, religion, cast, and location
- **Profile Details**: View detailed information in a modal popup
- **Responsive Design**: Works on desktop and mobile devices
- **Demo Credentials**: admin / admin123 (as shown on login page)

### Frontend Features:
- Pure JavaScript (no frameworks required)
- Real-time API integration with the Flask backend
- JWT token management with localStorage
- Responsive CSS design
- Error handling and loading states
- Filter functionality matching API capabilities

## Endpoints

- POST `/api/login` - User login, returns JWT
- POST `/api/users` - Admin: add user
- GET `/api/users` - Admin: list users
- PATCH `/api/users/<user_id>/make-admin` - Admin: promote user
- POST `/api/profiles` - Admin: create marriage profile
- GET `/api/profiles` - Authenticated: view/filter profiles
- GET `/api/profiles/<profile_id>` - Authenticated: view profile detail
- PUT `/api/profiles/<profile_id>` - Admin: update profile
- DELETE `/api/profiles/<profile_id>` - Admin: delete profile
