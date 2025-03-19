import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")  # Fallback for safety
    SESSION_TYPE = "filesystem"
    SESSION_PERMANENT = True
    SESSION_USE_SIGNER = True
    SESSION_KEY_PREFIX = "flask_session:"
    
    # Use absolute path for session storage
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
    SESSION_FILE_DIR = os.path.join(BASE_DIR, "flask_session_data")
    
    SESSION_COOKIE_NAME = "flask_session"
    SESSION_COOKIE_HTTPONLY = True  # Security: Prevent JS access
    SESSION_COOKIE_SECURE = os.getenv("SESSION_COOKIE_SECURE", "False") == "True"  # Enable for HTTPS
    SESSION_COOKIE_SAMESITE = os.getenv("SESSION_COOKIE_SAMESITE", "Lax")  # Cross-site handling
    
    DB_URL = os.getenv("DB_URL")

