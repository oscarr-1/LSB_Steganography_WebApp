from flask import Blueprint, request, current_app, send_file, jsonify, render_template
from app.services.image_hide import hide_text
from app.services.image_extract import extract_text
from werkzeug.utils import secure_filename
import os

image_bp = Blueprint('image', __name__)

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'bmp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@image_bp.route('/')
def image_page():
    return render_template('image_steg_page.html')


@image_bp.route('/hide_image_message', methods=['POST'])
def hide_image_message():
    try:
        if 'image' not in request.files or 'message' not in request.form:
            return jsonify({'error': 'Missing image or message'}), 400
        
        uploaded_file = request.files['image']
        secret_message = request.form['message']

        if not allowed_file(uploaded_file.filename):
            return jsonify({'error': 'Unsupported file type'}), 400

        filename = secure_filename(uploaded_file.filename)
        upload_folder = current_app.config['UPLOAD_FOLDER']
        input_path = os.path.join(upload_folder, filename)
        uploaded_file.save(input_path)

        output_path = os.path.join(upload_folder, f'hidden_{filename}')

        hide_text(input_path, secret_message, output_path)

        return send_file(output_path, mimetype='image/jpeg', as_attachment=True, download_name='modified_image.jpeg')
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@image_bp.route('/reveal_image_message', methods=['POST'])
def reveal_image_message():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'Missing image'}), 400
        
        uploaded_file = request.files['image']

        if not allowed_file(uploaded_file.filename):
            return jsonify({'error': 'Unsupported file type'}), 400

        filename = secure_filename(uploaded_file.filename)
        upload_folder = current_app.config['UPLOAD_FOLDER']
        input_path = os.path.join(upload_folder, filename)
        uploaded_file.save(input_path)
        
        message = extract_text(input_path)

        if not message:
            return jsonify({'error': 'No message found'}), 400
        
        return message
    except Exception as e:
        return jsonify({'error': str(e)}), 500