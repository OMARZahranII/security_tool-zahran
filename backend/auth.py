
<<<<<<< HEAD
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
=======
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

# Role management
users_roles = {
    "admin": {"permissions": ["view_reports", "manage_users", "trigger_scans"]},
    "user": {"permissions": ["view_reports", "trigger_scans"]},
    "auditor": {"permissions": ["view_reports"]}
}

def get_current_user_role(token: str = Depends(oauth2_scheme)):
    '''Fetch the current user's role.'''
    user = verify_token(token)
    return user['role']

def check_permissions(token: str, required_permission: str):
    '''Check if the user has the required permission.'''
    user_role = get_current_user_role(token)
    permissions = users_roles.get(user_role, {}).get('permissions', [])
    if required_permission not in permissions:
        raise HTTPException(status_code=403, detail="Permission denied")

def admin_required(token: str = Depends(oauth2_scheme)):
    '''Require admin role to access certain routes.'''
    role = get_current_user_role(token)
    if role != 'admin':
        raise HTTPException(status_code=403, detail="Admin access required.")
>>>>>>> d9428ef (push)
