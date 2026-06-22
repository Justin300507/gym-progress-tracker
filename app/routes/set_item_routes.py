from fastapi import APIRouter, Depends, HTTPException, Query, Path, Response, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.set_item import SetItem
from app.schemas.set_item import SetItemCreate, SetItemUpdate, SetItemRead

set_item_router = APIRouter()

@set_item_router.get("/set_items", response_model=List[SetItemRead])
def list_set_items(
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
) -> List[SetItemRead]:
    items = db.query(SetItem).offset(offset).limit(limit).all()
    return items

@set_item_router.get("/set_items/{item_id}", response_model=SetItemRead)
def get_set_item(
    item_id: int = Path(..., ge=1),
    db: Session = Depends(get_db)
) -> SetItemRead:
    item = db.query(SetItem).filter(SetItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="SetItem not found")
    return item

@set_item_router.post("/set_items", response_model=SetItemRead, status_code=status.HTTP_201_CREATED)
def create_set_item(
    item_in: SetItemCreate,
    db: Session = Depends(get_db)
) -> SetItemRead:
    item = SetItem(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@set_item_router.put("/set_items/{item_id}", response_model=SetItemRead)
def update_set_item(
    item_in: SetItemUpdate,
    item_id: int = Path(..., ge=1),
    db: Session = Depends(get_db)
) -> SetItemRead:
    item = db.query(SetItem).filter(SetItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="SetItem not found")
    update_data = item_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(item, field, value)
    db.commit()
    db.refresh(item)
    return item

@set_item_router.delete("/set_items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_set_item(
    item_id: int = Path(..., ge=1),
    db: Session = Depends(get_db)
) -> Response:
    item = db.query(SetItem).filter(SetItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="SetItem not found")
    db.delete(item)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
