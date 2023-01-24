from fastapi import APIRouter, status, Response
from src.models.api import MenuItemAPIModel
from src.controllers import menu

router = APIRouter(prefix="/menu", tags=["Menu"])


@router.get("")
async def get_menu():
    result: list = menu.get_all()
    if not result:
        return "No items"
    return result


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_menu_item(menu_item_api_model: MenuItemAPIModel, response:Response):
    try:
        menu.create_new_menu_item(menu_item_api_model=menu_item_api_model)
    except Exception as exc:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return str(exc)


@router.delete("")
def delete_menu_item(menu_item_name: str, response: Response):
    try:
        menu.delete_menu_item(menu_item_name=menu_item_name)
    except Exception as exc:
        response.status_code = status.HTTP_404_NOT_FOUND
        return str(exc)
