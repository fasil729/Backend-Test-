from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.api.deps import get_db, get_current_user
from app.utils.cache import cache

router = APIRouter()

@router.post("/", response_model=schemas.Post)
async def create_post(request: Request, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if request.headers.get("content-length"):
        content_length = int(request.headers.get("content-length"))
        if content_length > 1 * 1024 * 1024:
            raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="Payload too large")
    
    post_in = await request.json()
    post_in = schemas.PostCreate(**post_in)
    post = crud.post.create_with_owner(db=db, obj_in=post_in, owner_id=current_user.id)
    return post

@router.get("/", response_model=List[schemas.Post])
def read_posts(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if current_user.id in cache:
        return cache[current_user.id]
    
    posts = crud.post.get_by_owner(db=db, owner_id=current_user.id)
    cache[current_user.id] = posts
    return posts
