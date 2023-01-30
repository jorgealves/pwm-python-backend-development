from fastapi import APIRouter, status


router = APIRouter(prefix="/profile", tags=["Profile"])


@router.get("/{handle}", status_code=status.HTTP_200_OK)
def get_user_profile(handle: str):
    pass


@router.post("/{handle}", status_code=status.HTTP_202_ACCEPTED)
def follow_profile():
    pass


@router.get("/me", status_code=status.HTTP_200_OK)
def get_my_profile():
    pass


@router.patch("/me", status_code=status.HTTP_202_ACCEPTED)
def update_my_profile():
    pass
