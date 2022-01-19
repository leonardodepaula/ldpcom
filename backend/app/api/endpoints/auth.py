from datetime import timedelta
from typing import Any, List

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core import dependencies, security
from app.core.config import settings

router = APIRouter()

@router.post('/get-access-token', response_model=schemas.Token)
def get_access_token(db: Session = Depends(dependencies.get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    '''
    OAuth2 compatible token login, get an access token for future requests
    '''
    user = crud.user.authenticate(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail='Incorrect email or password')
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail='Inactive user')
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        'access_token': security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        'token_type': 'bearer',
    }


@router.post('/test-access-token', response_model=schemas.User)
def test_access_token(current_user: models.User = Depends(dependencies.get_current_user)) -> Any:
    '''
    Test access token
    '''
    return current_user