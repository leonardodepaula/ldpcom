from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core import dependencies

router = APIRouter()

@router.post("/", response_model=schemas.Article)
def create_article(*, db: Session = Depends(dependencies.get_db), article_in: schemas.ArticleCreate, current_user: models.User = Depends(dependencies.get_current_active_user)) -> Any:
    """
    Create new article.
    """
    article = crud.article.create(db=db, obj_in=article_in, author_id=current_user.id)
    return article

@router.get('/{id}', response_model=schemas.Article)
def read_article_by_id(*, id: int, db: Session = Depends(dependencies.get_db), current_user: models.User = Depends(dependencies.get_current_active_user)) -> Any:
    '''
    Get a specific article by id.
    '''
    article = crud.article.get(db, id=id)
    if not article:
        raise HTTPException(status_code=404, detail='Article not found.')
    else:
        return article