from pydantic import BaseModel, EmailStr, Field

class UserSignup(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=255)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostCreate(BaseModel):
    text: str = Field(max_length=1000000)  # 1 MB limit

class PostResponse(BaseModel):
    id: int
    text: str
    user_id: int