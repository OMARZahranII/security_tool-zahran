
import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

SECRET_KEY = "your-secret-key-here"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

refresh_tokens = {}

def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(seconds=3600)
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def create_refresh_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(days=30)
    refresh_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    refresh_tokens[refresh_token] = data['sub']
    return refresh_token

def verify_token(token: str):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def revoke_token(token: str):
    refresh_tokens.pop(token, None)

def admin_required(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    if user['role'] != 'admin':
        raise HTTPException(status_code=403, detail="Admin access required.")

@router.post("/refresh_token")
def refresh_access_token(refresh_token: str):
    if refresh_token not in refresh_tokens:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    new_token = create_token({"sub": refresh_tokens[refresh_token]})
    return {"access_token": new_token, "token_type": "bearer"}
