"""
    Source Code for HMS APIs
"""
from fastapi import (
    FastAPI ,
    Depends ,
    HTTPException , 
    status
)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from hospital_management.backend import (
    models,
    database,
    schemas
)
from hospital_management.backend.auth import (
    get_db,
    authenticate_user
)
from hospital_management.backend.utils import (
    create_access_token,
    hash_password
)
from hospital_management.backend.routes import admin

app = FastAPI(
        title="Hospital Management System",
        description="APIs for Hospital Management System",
        version="beta"
    )

#Register Routers
app.include_router(admin.router)

#create database table
models.Base.metadata.create_all(bind = database.engine)

@app.post("/singup",response_model=schemas.UserOut)
def signup(user:schemas.UserCreate , db : Session = Depends(get_db)):
    """
        Endpoint for User Singnup in HMS
    """
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username Already Exists"
        )
    new_user = models.User(
                        username = user.username,
                        fullname = user.full_name,
                        role = user.role,
                        hashed_password = hash_password(user.password)
                )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login" , response_model=schemas.Token)
def login(
    form_data : OAuth2PasswordRequestForm = Depends(),
    db : Session = Depends(get_db)
    ):
    """
        Endpoint for User Login in HMS
    """
    user = authenticate_user(db,form_data.username , form_data.password)
    if not user:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid Credentials"
        )
    token_data = {
                    "sub" : user.username , 
                    "role" : user.role
                }
    token = create_access_token(token_data)
    return {
            "access_token" : token,
            "token_type" : "bearer"
            }
# if __name__ == '__main__':
#     HOST = os.getenv("HOST")
#     PORT = int(os.getenv("PORT"))
#     uvicorn.run("hospital_management.backend.hospital_app:hospital_app", host=HOST, port=PORT, reload=True)
