from datetime import datetime, timedelta
from database import get_db
from sqlalchemy.orm import Session
import model
from fastapi import HTTPException, Depends,status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

import schemas
from jose import jwt,JWTError

SECRET_KEY= '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
    data['exp'] = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt.encode(data, SECRET_KEY, ALGORITHM)
    return {'ACCESS_TOKEN':access_token, 'token_type':'bearer'}

def verify_token(token:str,credential_exceptions):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload['identity']

        if user_id is None:
            raise credential_exceptions
        token_data = schemas.TokenData(email=user_id)
        return token_data
    except JWTError:
        raise credential_exceptions



def get_user(token: str = Depends(oauth2_scheme),db:Session = Depends(get_db)):
    credentials_exceptions = HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,headers={'WWW-Authenticate':'Bearer'})
    token_data = verify_token(token,credentials_exceptions)
    user=db.query(model.User).filter(model.User.email==token).one_or_none()
    
    return user