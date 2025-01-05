from fastapi import APIRouter

router = APIRouter()

from app.schemas import Item

@router.get("/{item_id}")
async def get_item(item_name: str) -> Item:
    return Item(
        name="soup",
        price=5.5
    )

@router.post("/")
async def create_item(item: Item) -> Item:
    return item