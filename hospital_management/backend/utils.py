"""
    Source Code for Generating JWT token
"""
import os
from typing import Dict,Any
from datetime import (
    datetime ,
    timedelta
)
import logging
from dotenv import load_dotenv
from passlib.context import CryptContext
from jose import (
    JWTError ,
    jwt
)

logging.basicConfig(level=logging.INFO)
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_TIME = int(os.getenv("ACCESS_TOKEN_EXPIRE_TIME"))

pwd_context = CryptContext(schemes=["bcrypt"] , deprecated="auto")

def hash_password(password : str) -> str:
    """
        Function to Hash the Password
        params : 
                    password : plain password
        returns : hashed password
    """
    return pwd_context.hash(password)

def verify_password(plain : str , hashed : str) -> bool:
    """
        Function to Verify password against the Hased string
        params : 
                    plain : plain password
                    hashed : hased password
        returns : True / False
    """
    return pwd_context.verify(plain,hashed)

def create_access_token(data : Dict[str,Any]) -> str:
    """
        Function to Create jwt access token
        params : 
                    data : containing username , role
        returns : jwt access token
    """
    try:
        to_encode = data.copy()
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME)
        to_encode.update(
                        {
                            "exp" : expire
                        }
                    )
        encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
        return encoded_jwt
    except:
        raise JWTError
def decode_access_token(token : str) -> Dict[str,Any]:
    """
        Function to Decode the jwt accees token and return the payload
        params :
                    token : jwt access token   
        returns : payload                    
    """
    try:
        return jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    except:
        raise JWTError
