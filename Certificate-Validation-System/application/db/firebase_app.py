import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# Initialize Firebase Admin SDK
cred = credentials.Certificate("/home/pawan/Downloads/Certificate-Validation-System/application/db/hackathon-de0e7-99c08a23258c.json")
firebase_admin.initialize_app(cred)

# Authentication
def register(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        return "success"
    except Exception as e:
        print(f"Error: {e}")
        return "failure"

def login(email, password):
    try:
        user = auth.get_user_by_email(email)
        return "success"
    except Exception as e:
        print(f"Error: {e}")
        return "failure"
