from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core import dependencies

router = APIRouter()

@router.post("/", response_model=schemas.Article)
def create_item(*, db: Session = Depends(dependencies.get_db), article_in: schemas.ArticleCreate, current_user: models.User = Depends(dependencies.get_current_active_user)) -> Any:
    """
    Create new article.
    """
    article = crud.article.create(db=db, obj_in=article_in, author_id=current_user.id)
    return article