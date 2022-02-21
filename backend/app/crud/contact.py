from typing import Any, Dict, Optional, Union, List, TypeVar

from sqlalchemy import extract
from sqlalchemy.orm import Session

from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.contact import Contact
from app.schemas.contact import ContactBase

from app.db.base_class import Base
ModelType = TypeVar('ModelType', bound=Base)

class CRUDContact(CRUDBase[Contact, ContactBase, ContactBase]):
    pass
  
contact = CRUDContact(Contact)