from datetime import datetime
from turtle import back

from sqlalchemy import Boolean, DateTime, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Project
from app.db.base_class import Base

class Article(Base):
    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(100), index=True)

    title = Column(String, nullable= False)
    abstract = Column(String, nullable= False)
    content = Column(String, nullable=False)
    published_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, nullable=False, default=True)
    
    author_id =  Column(Integer, ForeignKey('user.id'))
    author = relationship('User', back_populates='articles')