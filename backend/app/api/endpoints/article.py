from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core import dependencies

from slugify import slugify

router = APIRouter()

@router.get('/', response_model=List[schemas.Article])
def get_articles(db: Session = Depends(dependencies.get_db), skip: int = 0, limit: int = 100) -> Any:
    '''
    Retrieve a list of articles.
    '''
    articles = crud.article.get_multi(db, skip=skip, limit=limit)
    return articles

@router.post("/", response_model=schemas.Article)
def create_article(*, db: Session = Depends(dependencies.get_db), article_in: schemas.ArticleCreate, current_user: models.User = Depends(dependencies.get_current_active_user)) -> Any:
    """
    Create new article.
    """
    slug = slugify(article_in.title, max_length=100)
    article = crud.article.create(db=db, obj_in=article_in, author_id=current_user.id, slug=slug)
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