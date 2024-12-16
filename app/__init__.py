from flask import Flask
from app.routes.home import home_bp
from app.routes.image import image_bp
from app.routes.audio import audio_bp
import os

def create_app():
    app = Flask(__name__)

    app.config['UPLOAD_FOLDER'] = 'app/uploads'

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    app.config.from_object('app.config.Config')

    app.register_blueprint(home_bp)

    app.register_blueprint(image_bp, url_prefix='/image')

    app.register_blueprint(audio_bp, url_prefix='/audio')

    return app