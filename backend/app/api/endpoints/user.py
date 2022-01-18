from typing import Any, List

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.core import dependencies

router = APIRouter()

@router.get("/", response_model=List[schemas.User])
def read_users(db: Session = Depends(dependencies.get_db), skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve a list of users.
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users

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

@router.get("/{id}", response_model=schemas.User)
def read_user_by_id(*, id: int, db: Session = Depends(dependencies.get_db)) -> Any:
    """
    Get a specific user by id.
    """
    user = crud.user.get(db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    else:
        return user

@router.delete('/{id}', response_model=schemas.User)
def delete_user(*, db: Session = Depends(dependencies.get_db), id: int) -> Any:
    """
    Delete a specific user by id.
    """
    user = crud.user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        user = crud.user.remove(db=db, id=id)
        return user