from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String
from app.database import Base


class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(10))
  email = Column(String(100))