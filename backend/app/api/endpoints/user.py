from typing import Any, List

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.core import dependencies

router = APIRouter()

@router.post("/", response_model=schemas.User)
def create_user(*, db: Session = Depends(dependencies.get_db), user_in: schemas.UserCreate) -> Any:
    """
    Create new user.
    """
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    return user

@router.get("/{user_id}", response_model=schemas.User)
def read_user_by_id(*, user_id: int, db: Session = Depends(dependencies.get_db)) -> Any:
    """
    Get a specific user by id.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    else:
        return user