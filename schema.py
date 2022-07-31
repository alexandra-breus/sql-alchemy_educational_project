from datetime import datetime
from pydantic import BaseModel

class UserGet(BaseModel):

    id : int
    age : int
    city : str
    os : str
    country : str
    gender : int
    exp_group : int
    source : str

    class Config:
        orm_mode = True

class PostGet(BaseModel):

    id : int
    text : str
    topic : str

    class Config:
        orm_mode = True

class FeedGet(BaseModel):

    user_id : int
    user : UserGet
    post_id : int
    post : PostGet
    action : str
    time : datetime


    class Config:
        orm_mode = True
