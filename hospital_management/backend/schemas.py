"""
    Source Code for Schemas
    How Data is Handled in FastAPI
"""

from pydantic import BaseModel

class UserCreate(BaseModel):
    """
        User Create Model
        params : 
                    username
                    password
                    full_name
    """
    username : str
    password : str
    full_name : str
    role : str

class UserLogin(BaseModel):
    """
        User Login Model
        params : 
                    username
                    password
    """
    username : str
    password : str

class UserOut(BaseModel):
    """
        User checks
        params : 
                    username
                    role
    """
    id : int
    username : str
    role : str
    class Config:
        """
            converts the databse objs to dics
        """
        #orm_mode = True -- deprecated
        from_attributes = True

class Token(BaseModel):
    """
        Token Validation
    """
    access_token : str
    token_type : str

class TokenData(BaseModel):
    """
        Token Data Validation
    """
    username : str
    role : str
