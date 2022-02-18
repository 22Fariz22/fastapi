# import random
import time
# from typing import Optional, List
from fastapi import FastAPI,Response,status,HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
# from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
# from sqlalchemy.orm import Session
from app import models, schemas, utils
from .database import engine, get_db
from app.routers import post, user,auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
                                password='55555', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Database connection was sucsessful')
        break
    except Exception as error:
        print(f'Connecting was failed')
        print(f'error: {error}')
        time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get('/')
async def root():
    return {'message':'Hello world'}

