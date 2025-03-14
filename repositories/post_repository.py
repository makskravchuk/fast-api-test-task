from sqlalchemy.orm import Session
from models import Post

def create_post(db: Session, post_data: dict):
    db_post = Post(**post_data)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts_by_user(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()

def delete_post(db: Session, post_id: int, user_id: int):
    db.query(Post).filter(Post.id == post_id, Post.user_id == user_id).delete()
    db.commit()