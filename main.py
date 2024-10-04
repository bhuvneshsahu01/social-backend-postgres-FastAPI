from typing import Union, Optional
from fastapi.params import Body
from fastapi import FastAPI,status,Response,HTTPException
from pydantic import BaseModel
from typing import Union, Optional
from fastapi.params import Body
from fastapi import FastAPI, status, Response, HTTPException, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import sessionmaker

app = FastAPI()


class users_class(BaseModel):
    user_id: int
    title: str
    description: str
    published: bool = True
    rating: Optional[float] = None

my_posts = {'users': {'1': {'name': 'bhuvnesh', 'password': '<PASSWORD>', 'email': '<EMAIL>'},
                      "2": {'name': 'bhuvnesh', 'password': '<PASSWORD>', 'email': '<EMAIL>'}
                      },
            'posts': {'1': {'user_id': "1", 'title': 'fastapi', 'description': 'good', 'rating': 5}
                      }
            }


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/users")
def create_user(user_data: users_class):
    return user_data

@app.get("/items/{item_id}",status_code=status.HTTP_200_OK)
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/posts/{id}",status_code=status.HTTP_201_CREATED)
async def creat_post(posts: Item):
    print(posts)
    posts=posts.dict()
    my_posts['posts']['2']=posts
    return {"data": my_posts}

@app.get('/get_posts/{id}')
async def read_post(id: int,response: Response):
    if f'{id}' not in my_posts['posts'].keys():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} Not Found")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return
    data = my_posts['posts'][f'{id}']
    return {"data": data}

@app.put('/update_posts/{id}')
def update_post(id:str,data:Item):
    print(data)
    my_posts['posts'][f'{id}']=data.dict()
    print(my_posts['posts'])
    return {"data":data}


# # try:
# # # Connect to your PostgreSQL database
# #     conn = psycopg2.connect(
# #         dbname="FastAPI App1 ",
# #         user="postgres",
# #         password="bhuviSAHU@12",
# #         host="localhost",
# #         port="5432",
# #         cursor_factory=RealDictCursor
# #     )
# #
# #     # Create a cursor object
# #     cursor = conn.cursor()
# # except psycopg2.Error as e:
# #     print(f'Connection can not establish because {e}')
#
#
#
#
#
# @app.get("/")
# async def read_root():
#     return {"Hello": "World ji"}
#
# @app.post("/users")
# async def create_user(user_data: users_class,status_code=status.HTTP_201_CREATED):
#     cursor.execute('''INSERT INTO users (username,password_hash,full_name,email) VALUES (%s, %s, %s, %s) Returning * ''',
#                    (user_data.username,user_data.password_hash,user_data.name,user_data.email))
#     updated_data = cursor.fetchone()
#     conn.commit()
#     return {'Message': 'welcome', 'your details' : updated_data}
#
# @app.delete("/users/{user_id}")
# async def delete_user(user_id:int):
#     cursor.execute(
#         '''DELETE FROM users WHERE user_id=%s Returning *''',
#         (user_id,))
#     deleted_user = cursor.fetchone()
#     if not deleted_user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
#     conn.commit()
#     return
#
# @app.post("/posts/{user_id}",status_code=status.HTTP_201_CREATED)
# async def creat_post(user_id,post_data: post_class):
#     cursor.execute(
#         '''INSERT INTO posts (user_id,title,contents) VALUES (%s, %s, %s) Returning * ''',
#         (user_id, post_data.title, post_data.contents))
#     updated_post = cursor.fetchone()
#     conn.commit()
#     return {'Message': 'Your post is uploaded', 'post details': updated_post}
#
# @app.get('/get_posts/{post_id}')
# async def read_posts(post_id: int,response: Response):
#     cursor.execute('''SELECT u.full_name,p.user_id,p.title,p.contents FROM users u join posts p  on u.user_id = p.user_id where p.post_id = %s''',
#                    (post_id,))
#     post_content = cursor.fetchall()
#     if not post_content:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'Post with {post_id} not found')
#     # #     #response.status_code = status.HTTP_404_NOT_FOUND
#     return {'Message': 'Your post is found', 'post details': post_content}
#
# @app.put('/update_posts/{post_id}')
# def update_post(post_id:str,post_data:post_class):
#     cursor.execute(
#         '''UPDATE posts SET title = %s, contents = %s WHERE post_id = %s Returning *''',
#         (post_data.title, post_data.contents,post_id))
#     updated_post = cursor.fetchone()
#     conn.commit()
#     return {'Message': 'Your post is updated', 'post details': updated_post}