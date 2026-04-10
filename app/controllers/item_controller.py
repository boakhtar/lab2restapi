from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.services.item_service import ItemService
from app.schemas.item import ItemCreate, ItemUpdate, ItemResponse
from app.schemas.pagination import PaginatedResponse

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("/", response_model=ItemResponse, status_code=201)
def create_item(item_data: ItemCreate, db: Session = Depends(get_db)):
    return ItemService.create(db, item_data)

@router.get("/", response_model=PaginatedResponse[ItemResponse])
def get_items(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return ItemService.get_all(db, page, limit)

@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = ItemService.get_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item_data: ItemUpdate, db: Session = Depends(get_db)):
    item = ItemService.update(db, item_id, item_data)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.patch("/{item_id}", response_model=ItemResponse)
def patch_item(item_id: int, item_data: ItemUpdate, db: Session = Depends(get_db)):
    item = ItemService.update(db, item_id, item_data)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    success = ItemService.delete(db, item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return None