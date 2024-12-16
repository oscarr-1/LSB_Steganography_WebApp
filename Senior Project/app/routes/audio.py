from flask import Blueprint, request, current_app, send_file, jsonify, render_template
from app.services.audio_hide import hide_message
from app.services.audio_extract import extract_message
from werkzeug.utils import secure_filename
import os

audio_bp = Blueprint('audio', __name__)

ALLOWED_EXTENSIONS = {'wav'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@audio_bp.route('/')
def audio_page():
    return render_template('audio_steg_page.html')

@audio_bp.route('/hide_audio_message', methods=['POST'])
def hide_audio_message():
    try:
        if 'audio' not in request.files or 'message' not in request.form:
            return jsonify({'error': 'Missing audio file or message'}), 400
        
        uploaded_file = request.files['audio']
        secret_message = request.form['message']

        if not allowed_file(uploaded_file.filename):
            return jsonify({'error': 'Unsupported file type'}), 400
        
        filename = secure_filename(uploaded_file.filename)
        upload_folder = current_app.config['UPLOAD_FOLDER']
        input_path = os.path.join(upload_folder, filename)
        uploaded_file.save(input_path)

        output_filename = f'hidden_{filename}'
        output_path = os.path.join(upload_folder, output_filename)

        hide_message(input_path, secret_message, output_path)

        return send_file(output_path, mimetype='audio/wav', as_attachment=True, download_name=output_filename)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@audio_bp.route('/reveal_audio_message', methods=['POST'])
def reveal_audio_message():
    try:
        if 'audio' not in request.files:
            return jsonify({'error': 'Missing audio file'}), 400
        
        uploaded_file = request.files['audio']

        if not allowed_file(uploaded_file.filename):
            return jsonify({'error': 'Unsupported file type'}), 400

        filename = secure_filename(uploaded_file.filename)
        upload_folder = current_app.config['UPLOAD_FOLDER']
        input_path = os.path.join(upload_folder, filename)
        uploaded_file.save(input_path)
        
        message = extract_message(input_path)

        if not message:
            return jsonify({'error': 'No message found'}), 400
        
        return jsonify({'message': message}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500