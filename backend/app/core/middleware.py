from fastapi import Request
from fastapi.encoders import jsonable_encoder
from starlette.middleware.base import BaseHTTPMiddleware

from app import schemas
from app.db.mongodb import mongodb_client

##############
#### Logs ####
##############

class RequestLogMiddleware(BaseHTTPMiddleware):
	
	async def dispatch(self, request, call_next):

		response = await call_next(request)

		if request.scope.get('path') != '/log/':

			request_body = schemas.RequestBody(path=str(request.base_url), params=request.path_params, query=request.query_params)
			client_data = schemas.ClientData(host=request.client.host, port=request.client.port)
			request_data = schemas.RequestData(method=request.method, headers=request.headers, body=request_body)
			response_data = schemas.ResponseData(headers=response.headers, status_code=response.status_code)
			log = schemas.Log(client=client_data, request=request_data, response=response_data)

			document = await mongodb_client.log.logs.insert_one(jsonable_encoder(log))

		return response