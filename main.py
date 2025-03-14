from fastapi import FastAPI, Depends
from controllers.auth_controller import signup_user, login_user
from controllers.post_controller import add_post, get_user_posts, delete_user_post
from database import get_db, init_db
from dependencies.auth_dependencies import authenticate_user
from schemas import UserSignup, UserLogin, PostCreate

init_db()
app = FastAPI()

@app.post("/signup")
def signup(user_data: UserSignup, db = Depends(get_db)):
    return signup_user(db, user_data)

@app.post("/login")
def login(user_data: UserLogin, db = Depends(get_db)):
    return login_user(db, user_data)

@app.post("/addpost")
def add_post_endpoint(post_data: PostCreate, user_id: int = Depends(authenticate_user), db = Depends(get_db)):
    return add_post(db, post_data, user_id)

@app.get("/getposts")
def get_posts_endpoint(user_id: int = Depends(authenticate_user), db = Depends(get_db)):
    return get_user_posts(db, user_id)

@app.delete("/deletepost/{post_id}")
def delete_post_endpoint(post_id: int, user_id: int = Depends(authenticate_user), db = Depends(get_db)):
    return delete_user_post(db, post_id, user_id)