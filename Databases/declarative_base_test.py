from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declerative import declerative_base

Base = declerative_base()


class Mustang(Base):
        __tablename__ = 'mustang'
        id = Column(Integer, primary_key=True)
        year = Column(Integer)
        name = Column(String(50))
