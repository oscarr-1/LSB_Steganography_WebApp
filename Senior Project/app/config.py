import os
from flask import current_app
class Config:
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app/uploads')
    