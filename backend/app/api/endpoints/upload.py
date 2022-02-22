from fastapi import APIRouter, UploadFile, File, Depends

from app.core import utils, dependencies
from app import models

router = APIRouter()

@router.post('/')
def upload_file(file: UploadFile = File(...), current_user: models.User = Depends(dependencies.get_current_active_user)):

    uploaded_file = utils.save_file(file)

    return {'filename': uploaded_file}