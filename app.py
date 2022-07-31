from typing import List
from schema import FeedGet, UserGet, PostGet, FeedGet
from database import SessionLocal
from table_feed import Feed
from table_user import User
from table_post import Post

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func


def get_db():
    with SessionLocal() as db:
        return db

app = FastAPI()

@app.get('/user/{id}', response_model=UserGet)
def get_user(id : int, db : Session = Depends(get_db)):
    
        result =  db.query(User).filter(User.id == id).one_or_none()
        if result:
            return result
        else:
            raise HTTPException(status_code=404, detail="user not found")

@app.get('/post/{id}', response_model=PostGet)
def get_post(id : int, db : Session = Depends(get_db)):
    
        result =  db.query(Post).filter(Post.id == id).one_or_none()

        if result:
            return result
        else:
            raise HTTPException(status_code=404, detail="post not found")


@app.get('/post/{id}/feed', response_model=List[FeedGet])
def get_feed_by_post(id: int, limit : int = 10, db : Session = Depends(get_db)):

    return db.query(Feed).filter(Feed.post_id == id).order_by(Feed.time.desc()).limit(limit).all()

@app.get('/post/recommendations/', response_model=List[PostGet])
def recommendation(id : int, limit : int=10, db : Session = Depends(get_db)):

    return db.query(Post.id, Post.text, Post.topic) \
    .join(Feed) \
    .filter(Feed.action == 'like') \
    .group_by(Post.id, Post.text, Post.topic) \
    .order_by(func.count(Feed.post_id).desc()) \
    .limit(limit) \
    .all()