from uuid import uuid4
from re import search as regex_search
from shutil import copyfileobj

from app.core.config import settings

#####################
#### File Upload ####
#####################

def save_file(file):
    process_filename = regex_search('(.+)\.(.+)$', file.filename)
    
    if process_filename:
        filename = process_filename[1]
        fileformat = process_filename[2]

    file_uuid = str(uuid4().hex)
    final_filename = f'{filename}_{file_uuid}.{fileformat}'

    try:
        
        with open(f'{settings.STATIC_DIR}/{final_filename}', 'wb') as buffer:
            copyfileobj(file.file, buffer)
            return final_filename

    except:

        return None