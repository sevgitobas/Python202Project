from fastapi import APIRouter
from src.models.user import User

router = APIRouter()

@router.get("/users")
def get_users():
    return [{"id": 1, "name": "G�k�e"}]

@router.post("/users")
def create_user(user: User):
    return {"message": f"Kullan�c� olu�turuldu: {user.name}"}
