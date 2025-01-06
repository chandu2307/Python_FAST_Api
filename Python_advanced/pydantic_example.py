"""
Source code : Pydantic models in python

Your goal is to create a social media post model using pydantic.
The model should have:
    An author, which is a string
    An optional co-author, which is a string
    A date, which is a string
    A title, which is a string
    The content, which is a string
    An ID, which is an integer
    Likes, which is a list of strings
    The post should also have a field for comments, which is a list of comment models. 
            The model should have:
                An author, which is a string
                The comment, which is a string
                Likes, which is an integer

Practice creating a social media post with whatever data you like, so long as it compiles.

"""
from typing import List , Optional
from pydantic import BaseModel

class Comment(BaseModel):
    """ Comment Model using pydantic"""
    author  :   str
    comment :   str
    Likes   :   int

class Post(BaseModel):
    """ Social Media Post Model using pydantic """
    author          : str
    co_author       : Optional[str] = None
    date            : str
    title           : str
    content         : str
    ID              : int
    Likes           : List[str]
    comment         : List[Comment]

comments = [
            Comment(
                    author="chandu" ,
                    comment="hai this is my comment" ,
                    Likes = 23
                    )
        ]
post = Post(
                author = "chandu",
                co_author= None,
                date = "23/07/2000",
                title="hello world",
                content = "Testing content",
                ID = 1,
                Likes = ["chandu","chandu"],
                comment= comments
        )
print(post)
