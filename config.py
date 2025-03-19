import os
from dotenv import load_dotenv
from redis import Redis

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Session Configuration
    SESSION_TYPE = os.getenv('SESSION_TYPE', 'redis')  # Default to Redis
    SESSION_PERMANENT = True
    SESSION_USE_SIGNER = True
    SESSION_KEY_PREFIX = 'flask_session:'
    SESSION_COOKIE_NAME = 'flask_session'
    
    # Secure Cookies
    IS_PRODUCTION = os.getenv('FLASK_ENV') == 'production'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'  # Use "None" if cross-origin
    SESSION_COOKIE_SECURE = IS_PRODUCTION  # Secure only in production

    # Session Storage
    if SESSION_TYPE == 'filesystem':
        SESSION_FILE_DIR = './flask_session_data'
    elif SESSION_TYPE == 'redis':
        SESSION_REDIS = Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=int(os.getenv('REDIS_PORT', 6379)))

    # Database
    DB_URL = os.getenv('DB_URL')
