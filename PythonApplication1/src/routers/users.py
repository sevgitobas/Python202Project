from fastapi import APIRouter
from src.models.user import User

router = APIRouter()

@router.get("/users")
def get_users():
    return [{"id": 1, "name": "Gökçe"}]

@router.post("/users")
def create_user(user: User):
    return {"message": f"Kullanýcý oluþturuldu: {user.name}"}
