from fastapi import APIRouter
from app.dependencies import CurrentUserDep


router = APIRouter()


@router.get("/me")
def handle_me(current_user: CurrentUserDep):
    return {
        "text": f"User id: {current_user.user_id}"
    }