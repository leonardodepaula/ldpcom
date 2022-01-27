from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.article import Article
from app.schemas.article import ArticleCreate, ArticleUpdate

class CRUDArticle(CRUDBase[Article, ArticleCreate, ArticleUpdate]):
    def create(self, db: Session, *, obj_in: ArticleCreate, author_id: int) -> Article:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = Article(**obj_in_data, author_id=author_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
  
article = CRUDArticle(Article)