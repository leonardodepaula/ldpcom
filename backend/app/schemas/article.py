from typing import Optional
from pydantic import BaseModel

from .user import User

class ArticleBase(BaseModel):
	title: str
	abstract: str
	content: str

class ArticleCreate(ArticleBase):
	pass

class ArticleUpdate(BaseModel):
	slug: Optional[str] = None
	title: Optional[str] = None
	abstract: Optional[str] = None
	content: Optional[str] = None

class ArticleInDBBase(ArticleBase):
	id: int
	slug: str
	author_id: int

	class Config:
		orm_mode = True
  
class Article(ArticleInDBBase):
	author: User
	pass

class ArticleInDB(ArticleInDBBase):
	pass