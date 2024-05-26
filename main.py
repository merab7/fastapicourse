from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
import random
app = FastAPI()

POSTS = [{"post1_title": "aaaaa", "post1_content": "bbbbbbb", "post1_author":"ccccccc", "id":2}]

class Post(BaseModel):
    title: str
    content: str
    author: str
    published: bool = True
    rating : Optional[int] = None

#path operation
@app.get("/")
def root():
    return {"message": "Hello World i am merab"}

@app.get("/posts")
def get_posts():
    return{"data": POSTS}


@app.post("/posts", status_code=status.HTTP_201_CREATED)#changing default 200 status code to right 201 status code witch is for creation
def create_post(post:Post):
    post_dict = post.dict()
    post_dict["id"] = random.randrange(1, 10000000000)
    POSTS.append(post_dict)
    return{"new post": post_dict}   


@app.get("/posts/{id}")
#value validation happens in function
def get_post(id:int):
    requested_post = [x for x in POSTS if x["id"] == int(id)]
    if not requested_post:
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return{"message": f"post with id: {id} was not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return{"post details": f"here is your {requested_post}"}

#path parameter is always returned as a string

#put when you serve update and all data with it
#patch when you serve specific filed form the data for to be updated
#ORDER MATTERS