# -*- coding: utf-8 -*-
from typing import  List

from fastapi import FastAPI,Response,status,HTTPException, Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import engine, get_db
from app import models, schemas, utils
# from app.main import app
# models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)

@router.get('/sqlalchemy')
async def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


@router.get('/',response_model=List[schemas.Post])
async def root(db: Session = Depends((get_db))):
    posts = db.query(models.Post).all()
    return posts


@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
async def create_post(post: schemas.PostCreate, db: Session = Depends((get_db))):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get('/latest')
def latest_post():
    last: str = bd[-1]
    print(last)
    return last

@router.get('/{id}', response_model=schemas.Post)
def get_post(id: int, db: Session = Depends((get_db))):

    post = db.query(models.Post).filter(models.Post.id==id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id {id} was not found')
    return post

@router.delete('/posts/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends((get_db))):

     post = db.query(models.Post).filter(models.Post.id == id)
     print(post)
     if post.first() == None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post id={id} was not found')
     post.delete(synchronize_session=False)
     db.commit()

@router.put('/{id}',response_model=schemas.Post)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends((get_db))):
    query_post = db.query(models.Post).filter(models.Post.id == id)
    first_post = query_post.first()
    if first_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='this post was not found')
    query_post.update(post.dict(), synchronize_session=False)
    db.commit()
    return 'succsess'

