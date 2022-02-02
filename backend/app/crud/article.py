from typing import Any, Dict, Optional, Union, List, TypeVar

from sqlalchemy import extract
from sqlalchemy.orm import Session

from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.article import Article
from app.schemas.article import ArticleCreate, ArticleUpdate

from app.db.base_class import Base
ModelType = TypeVar('ModelType', bound=Base)

class CRUDArticle(CRUDBase[Article, ArticleCreate, ArticleUpdate]):

    def create(self, db: Session, *, obj_in: ArticleCreate, author_id: int, slug: str) -> Article:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = Article(**obj_in_data, author_id=author_id, slug=slug)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return db.query(self.model).order_by(self.model.published_at.desc()).offset(skip).limit(limit).all()
    
    def get_by_year_month_and_slug(self, db: Session, year: int, month: int, slug: str) -> Optional[ModelType]:
        return db.query(self.model).filter(extract('year', self.model.published_at) == year, extract('month', self.model.published_at) == month, self.model.slug == slug).first()
  
article = CRUDArticle(Article)