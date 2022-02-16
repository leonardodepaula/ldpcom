from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core import dependencies, utils
from app.core.config import settings

from slugify import slugify

router = APIRouter()

@router.get('/', response_model=List[schemas.Article])
def read_articles(db: Session = Depends(dependencies.get_db), skip: int = 0, limit: int = 100) -> Any:
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

@router.get('/{year}/{month}/{slug}', response_model=schemas.Article)
def read_article_by_year_month_and_slug(*, year: int, month: int, slug: str, db: Session = Depends(dependencies.get_db)) -> Any:
    '''
    Get a specific article by year, month and slug.
    '''
    article = crud.article.get_by_year_month_and_slug(db, year=year, month=month, slug=slug)
    if not article:
        raise HTTPException(status_code=404, detail='Artigo não encontrado.')
    else:
        return article

@router.post('/uploadfile/')
def upload_file(file: UploadFile = File(...)):

    uploaded_file = utils.save_file(file)

    return {'filename': uploaded_file}