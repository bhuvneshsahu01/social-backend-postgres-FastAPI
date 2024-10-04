import sys

# Add the parent directory to sys.path
sys.path.append(r"C:\Users\Bhuvnesh's PC\PycharmProjects\pythonProject\FastAPI_project")

from fastapi import FastAPI, status, Response, HTTPException, Depends, APIRouter
import schemas,model,oauth2
from sqlalchemy.orm import Session
from database import get_db


router = APIRouter(prefix="/posts", tags=["posts"])

@router.put('/{post_id}',response_model=schemas.post_schema,status_code=status.HTTP_200_OK)
def update_post(post_id:int, post_data: schemas.post_schema, db: Session = Depends(get_db),user: str = Depends(oauth2.get_user)):
    post_query = (db.query(model.Post).filter(model.Post.post_id == post_id))
    post=post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')

    post_query.update(post_data.dict())
    db.commit()
    return post

@router.post('/new_post/{user_id}',response_model=schemas.post_schema,status_code=status.HTTP_201_CREATED)
def new_post(user_id:int, post_data: schemas.post_schema, db: Session = Depends(get_db),user: str = Depends(oauth2.get_user)):
    post_data=post_data.dict()
    post_data['user_id']=user_id
    new_post = model.Post(**post_data)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get('/{id}', response_model=schemas.post_schema,status_code=status.HTTP_200_OK)
async def posts_route(id:int, db: Session = Depends(get_db)):
    post = db.query(model.Post).filter(model.Post.post_id == id).first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')

    return post

@router.delete('/{id}',status_code=status.HTTP_200_OK)
def delete_post(id:int, db: Session = Depends(get_db),user: str = Depends(oauth2.get_user)):
    post = db.query(model.Post).filter(model.Post.post_id == id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')
    db.delete(post)
    db.commit()