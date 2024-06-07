from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, crud
from app.api.deps import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.Post)
def create_post(post_in: schemas.PostCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    post = crud.post.create_with_owner(db=db, obj_in=post_in, owner_id=current_user.id)
    return post

@router.get("/", response_model=List[schemas.Post])
def read_posts(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    posts = crud.post.get_by_owner(db=db, owner_id=current_user.id)
    return posts

@router.delete("/{post_id}", response_model=schemas.Post)
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    post = crud.post.get(db=db, id=post_id)
    if not post or post.owner_id != current_user.id:
        raise HTTPException(status_code=400, detail="Invalid post or permissions")
    post = crud.post.remove(db=db, id=post_id)
    return post
