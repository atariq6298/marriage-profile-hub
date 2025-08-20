# Deployment Steps for marriage-profile-hub (Flask App)

## 1. Prepare Your Code
- Ensure your app has these files: `app.py`, `models.py`, `routes.py`, `requirements.txt`, etc.
- Set a secure `SECRET_KEY` and `JWT_SECRET_KEY` in `app.py` (never use default values in production!).

## 2. Push to GitHub
- Commit all changes and push your code to your GitHub repository.

## 3. Create a PythonAnywhere Account
- Sign up at https://www.pythonanywhere.com/ and start a free or paid account.

## 4. Start a New Web App
- Go to the "Web" tab on PythonAnywhere dashboard.
- Click "Add a new web app".
- Choose Flask as the framework.
- Select Python version (match your local version, e.g., 3.9).

## 5. Clone Your Repo to PythonAnywhere
- Open a Bash console on PythonAnywhere.
- Run:
  ```bash
  git clone https://github.com/atariq6298/marriage-profile-hub.git
  cd marriage-profile-hub
  ```

## 6. Set Up Virtual Environment and Install Requirements
- In your app folder, run:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

## 7. Configure