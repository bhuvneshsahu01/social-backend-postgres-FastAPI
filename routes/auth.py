import sys
import os

# Add the parent directory to sys.path
sys.path.append(r"C:\Users\Bhuvnesh's PC\PycharmProjects\pythonProject\FastAPI_project")

from fastapi import Depends, FastAPI, HTTPException, APIRouter,status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from database import get_db
import schemas,model,utils,oauth2
from sqlalchemy.orm import Session
from oauth2 import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login",response_model=schemas.UserToken)
def Auth(User_credentials: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.email == User_credentials.username).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail='Invalid Credentials')
    if not utils.verify_password(User_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')
    access_token=create_access_token(data = {'identity':user.email})
    return access_token
