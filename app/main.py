from fastapi import FastAPI
from . import models
from .database import engine
from app.routers import post, user, auth, vote
from app.config import settings

# # при каждом запуске будут отслеживатся все изменения в models и автоматически запускать изменения в бд
# # но тк у нас есть  alembic,то мы закоментируем это
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


