from datetime import datetime
from datetime import timezone

from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder

from app.db.mongodb import mongodb_client
from app import schemas

router = APIRouter()

@router.post('/', response_model=schemas.Log)
async def create_log(request: Request, request_body: schemas.RequestBody):

  client_data = schemas.ClientData(host=request.client.host, port=request.client.port)
  request_data = schemas.RequestData(method='GET', headers=request.headers, body=request_body)
  log = schemas.Log(origin='frontend', client=client_data, request=request_data)

  document = await mongodb_client.log.logs.insert_one(jsonable_encoder(log))

  return log