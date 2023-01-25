from fastapi import APIRouter
from src.models.api import CreateOrderAPIModel
from src.controllers import orders

router = APIRouter(prefix='/orders', tags=['orders'])


@router.post("")
async def create_order(create_order_api_model:CreateOrderAPIModel):
    orders.create_order(create_order_api_model=create_order_api_model)    


@router.get("")
def list_orders():
    pass
