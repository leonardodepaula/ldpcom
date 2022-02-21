from datetime import datetime
from datetime import timezone
from typing import Any

from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core import dependencies

router = APIRouter()

@router.post('/', response_model=schemas.ContactBase)
async def create_contact(*, db: Session = Depends(dependencies.get_db), obj_in: schemas.ContactBase) -> Any:

	contact = crud.contact.create(db=db, obj_in=obj_in)

	return obj_in