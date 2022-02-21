from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel
from ipaddress import IPv4Address
from typing import Optional

class RequestBody(BaseModel):
    path: str
    params: Optional[dict] = None
    query: Optional[dict] = None

class ClientData(BaseModel):
	host: IPv4Address
	port: int

class RequestData(BaseModel):
	method: str
	headers: dict
	body: RequestBody
  
class Log(BaseModel):
	origin: str = 'backend'
	date: datetime
	client: ClientData
	request: RequestData



