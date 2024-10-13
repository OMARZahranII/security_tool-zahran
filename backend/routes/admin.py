
from fastapi import APIRouter, Depends, HTTPException
from backend.auth import admin_required

router = APIRouter()

# Example user storage (to be replaced with a database in production)
users_db = {
    "admin_user": {"username": "admin", "role": "admin"},
    "regular_user": {"username": "user", "role": "user"}
}

@router.get("/admin/users")
def get_all_users(token: str = Depends(admin_required)):
    '''Admin route to get all users.'''
    return users_db

@router.post("/admin/users/assign_role")
def assign_role(username: str, role: str, token: str = Depends(admin_required)):
    '''Admin route to assign roles to users.'''
    if username not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    if role not in ["admin", "user", "auditor"]:
        raise HTTPException(status_code=400, detail="Invalid role")
    
    users_db[username]['role'] = role
    return {"message": f"Role '{role}' assigned to user '{username}'."}
