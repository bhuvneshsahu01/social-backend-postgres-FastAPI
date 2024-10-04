import sys

# Add the parent directory to sys.path
sys.path.append(r"C:\Users\Bhuvnesh's PC\PycharmProjects\pythonProject\FastAPI_project")

import schemas,utils,model
from sqlalchemy.orm import Session
from fastapi import status, Response, HTTPException, Depends,APIRouter
from database import get_db

router = APIRouter(prefix="/users", tags=["users"])


@router.post('/new_user',response_model=schemas.UserSchemaResponse,status_code=status.HTTP_201_CREATED)
def new_user(user_data: schemas.new_users_schema,db: Session = Depends(get_db)):
    hashed_password = utils.password_hash(user_data.password)
    user_data=user_data.dict()
    user_data['password']=hashed_password
    new_user = model.User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.delete('/{user_id}',status_code=status.HTTP_200_OK)
def delete_user(user_id:int, db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not found')
    db.delete(user)
    db.commit()