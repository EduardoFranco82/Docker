from fastapi import FastAPI
from app.settings import settings
from app.database import Session
from app.models import User
from pydantic import BaseModel


class UserSchema(BaseModel):
  name: str
  email: str


app = FastAPI()


@app.get('/')
def index():
  return {'msg': 'hello'}

@app.get('/hello')
def hello():
  return f'hello, {settings.app_name}'


@app.post('/users')
def create_users(user: UserSchema):
  db = Session()
  model = User(**user.dict())
  db.add(model)
  db.commit()
  db.refresh(model)
  db.close()

  

  return model

@app.get('/users')
def list_users():
  db = Session()
  users = db.query(User).all()
  db.close()

  return users