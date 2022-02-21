from datetime import datetime

from sqlalchemy import DateTime, Column, Integer, String

# Project
from app.db.base_class import Base

class Contact(Base):
    id = Column(Integer, primary_key=True, index=True)

    date = Column(DateTime, default=datetime.utcnow)
    email = Column(String, nullable=False)
    subject = Column(String, nullable=True)
    content = Column(String, nullable=False)
