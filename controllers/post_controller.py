from fastapi import HTTPException, status
from repositories.post_repository import create_post, get_posts_by_user, delete_post
from schemas import PostCreate, PostResponse
from utils.cache import cache_response, get_cached_response

def add_post(db, post_data: PostCreate, user_id: int):
    post = create_post(db, {"text": post_data.text, "user_id": user_id})
    return {"post_id": post.id}

def get_user_posts(db, user_id: int):
    cached_posts = get_cached_response(user_id)
    if cached_posts:
        return cached_posts
    posts = get_posts_by_user(db, user_id)
    cache_response(user_id, posts)
    return posts

def delete_user_post(db, post_id: int, user_id: int):
    delete_post(db, post_id, user_id)
    return {"message": "Post deleted"}