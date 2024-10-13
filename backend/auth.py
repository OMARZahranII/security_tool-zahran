# backend/auth.py

import jwt
from fastapi import HTTPException, Request
from fastapi import Depends
from datetime import datetime, timedelta
from backend.config import config


SECRET_KEY = config.SECRET_KEY

def create_token(data: dict):
    """Create a JWT token."""
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(seconds=config.TOKEN_EXPIRATION)
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(token: str):
    """Verify the provided JWT token."""
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def admin_required(token: str = Depends(verify_token)):
    """Require admin role for specific routes."""
    user = verify_token(token)
    if user['role'] != 'admin':
        raise HTTPException(status_code=403, detail="Admin access required.")