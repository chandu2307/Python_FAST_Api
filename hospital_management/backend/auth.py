"""
    Source Code for Oauth2
"""
import logging
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError
from hospital_management.backend import models,database
from hospital_management.backend.utils import decode_access_token , verify_password

logging.basicConfig(level=logging.INFO)

def get_db():
    """
        Function to initialze db and also close db 
    """
    db = database.SessionLocal()
    try:
        logging.info("Connected to Database...")
        yield db
    finally:
        logging.info("Closing Database connection....")
        db.close()
        logging.info("Closed Database Connection successfully...")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_user(db : Session , username : str):
    """
        Function to fetch the user by username from the databse
    """
    result = db.query(models.User).filter(models.User.username == username).first()
    return result

def authenticate_user(db : Session , username : str , password : str):
    """
        Function to Authenticate the user
    """
    user = get_user(db,username)
    if not user or not verify_password(password,user.hashed_password):
        logging.info("Not a valid user...")
        return None
    logging.info("User authenticated successfully...")
    return user

async def get_current_user(
        token : str = Depends(oauth2_scheme),
        db : Session = Depends(get_db)
    ):
    """
        Function to Get the User 
    """    
    credentials_exception = HTTPException(
                                status_code= status.HTTP_401_UNAUTHORIZED,
                                detail="Invalid Credentials.",
                                headers= {
                                            "WWW-Authenticate" : "Bearer"
                                        }
                            )
    try:
        payload = decode_access_token(token)
        username = payload.get("sub")
        role = payload.get("role")
        if username is None or role is None:
            logging.error("Credentials Not Found/Valid...")
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = get_user(db,username)
    if user is None:
        logging.error("User Not Found...")
        raise credentials_exception
    logging.info("User Found...")
    return user

def require_role(required_role : str):
    """
        Function to validate the Role for the user
    """
    async def role_checker(user = Depends(get_current_user)):
        if user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insuffecient Previlages/Permissions"
            )
        return user
    return role_checker
