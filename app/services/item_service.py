from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate
from datetime import datetime

class ItemService:
    @staticmethod
    def create(db: Session, item_data: ItemCreate):
        db_item = Item(
            title=item_data.title,
            description=item_data.description,
            status=item_data.status
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    @staticmethod
    def get_by_id(db: Session, item_id: int):
        return db.query(Item).filter(
            Item.id == item_id,
            Item.deleted_at.is_(None)
        ).first()
    
    @staticmethod
    def get_all(db: Session, page: int = 1, limit: int = 10):
        offset = (page - 1) * limit
        query = db.query(Item).filter(Item.deleted_at.is_(None))
        total = query.count()
        items = query.offset(offset).limit(limit).all()
        total_pages = (total + limit - 1) // limit if limit > 0 else 1
        
        return {
            "data": items,
            "total": total,
            "page": page,
            "limit": limit,
            "total_pages": total_pages
        }
    
    @staticmethod
    def update(db: Session, item_id: int, item_data: ItemUpdate):
        db_item = ItemService.get_by_id(db, item_id)
        if not db_item:
            return None
        
        if item_data.title is not None:
            db_item.title = item_data.title
        if item_data.description is not None:
            db_item.description = item_data.description
        if item_data.status is not None:
            db_item.status = item_data.status
        
        db.commit()
        db.refresh(db_item)
        return db_item
    
    @staticmethod
    def delete(db: Session, item_id: int):
        db_item = ItemService.get_by_id(db, item_id)
        if not db_item:
            return False
        
        db_item.deleted_at = datetime.now()
        db.commit()
        return True