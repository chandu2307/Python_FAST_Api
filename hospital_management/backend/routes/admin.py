"""
    Source Code for Admin APIs
"""

from fastapi import APIRouter,Depends
from hospital_management.backend.auth import require_role

router = APIRouter(prefix='/admin', tags=["Admin"])

@router.get("/admin")
def admin(current_user = Depends(require_role("admin"))):
    """
        Admin Users
    """
    return {
                "message" : f"Welcome to Admin Page :: {current_user.full_name}"
            }
