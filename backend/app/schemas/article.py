from typing import Optional
from pydantic import BaseModel

class ArticleBase(BaseModel):
	slug: str
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
	author_id: int

	class Config:
		orm_mode = True
  
class Article(ArticleInDBBase):
	pass

class ArticleInDB(ArticleInDBBase):
	pass