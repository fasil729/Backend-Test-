from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate

def get(db: Session, id: int):
    return db.query(Post).filter(Post.id == id).first()

def create_with_owner(db: Session, obj_in: PostCreate, owner_id: int):
    db_obj = Post(
        text=obj_in.text,
        owner_id=owner_id
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_by_owner(db: Session, owner_id: int):
    return db.query(Post).filter(Post.owner_id == owner_id).all()

def remove(db: Session, id: int):
    obj = db.query(Post).get(id)
    db.delete(obj)
    db.commit()
    return obj
