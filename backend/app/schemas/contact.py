from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

class ContactBase(BaseModel):
	date: datetime = datetime.utcnow()
	email: EmailStr
	subject: Optional[str] = None
	content: str

class ContactInDBBase(ContactBase):
	id: int

	class Config:
		orm_mode = True

class Contact(ContactInDBBase):
	pass