from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "another test"}

@app.get("/posts")
def get_posts():
    return {"data": "This are your posts"}

@app.post("/createposts")
def create_posts(post: Post):
    print(post.rating)
    print(post.dict())
    return {"data": post}
