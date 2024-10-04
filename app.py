from database import engine
from fastapi import FastAPI, status, Response, HTTPException, Depends
import schemas,utils,model
from sqlalchemy.orm import Session
from database import get_db
from routes import users,posts,auth


model.Base.metadata.create_all(bind=engine)

app = FastAPI()


app = FastAPI()

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(auth.router)










