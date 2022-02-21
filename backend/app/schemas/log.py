from datetime import datetime, timezone
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

class ResponseData(BaseModel):
	headers: dict
	status_code: int
  
class Log(BaseModel):
	origin: str = 'backend'
	date: datetime = datetime.now(tz=timezone.utc)
	client: ClientData
	request: RequestData
	response: ResponseData



