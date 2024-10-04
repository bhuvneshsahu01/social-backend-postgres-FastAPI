from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base,relationship

Base = declarative_base()


class Post(Base):
    __tablename__ = 'Posts'

    post_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'),nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    user = relationship("User", back_populates="posts")


class User(Base):
    __tablename__ = 'Users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    email = Column(String,nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    posts = relationship("Post", back_populates="user", cascade="all, delete-orphan")


