from fastapi import APIRouter, Depends
from backend.auth import admin_required

router = APIRouter()

@router.get("/admin/dashboard")
def admin_dashboard(token: str = Depends(admin_required)):
    """Admin-only dashboard."""
    return {"message": "Welcome, Admin!"}
