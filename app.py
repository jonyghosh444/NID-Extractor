from flask import Flask, request, jsonify
from detector import anpr_detector
from OcrANPRModel import updateModel
from PIL import Image
import numpy as np

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/v1/server/status', methods=['GET'])
def server_health():
    return jsonify({'status': 'Service UP'}), 200


# @app.route('/api/v1/server/upload-image', methods=['POST'])
# def upload_anpr():
#     if request.method == 'POST':
#         if "image_file" not in request.files:
#             return jsonify({'status': 'No file part'}), 403
#         raw_image = request.files['image_file'].stream
#         # if raw_image.filename == '':
#         #     return jsonify({'status': 'No selected file'}), 400
#         images = Image.open(raw_image)
#         detect_image = anpr_detector(images)
#         if detect_image == False:
#             return jsonify({'status': 'No detected image'}), 400
#         else:
#             convert_detect_image = np.asarray(detect_image)
#             ocr, result = mainModel(convert_detect_image)
#             join_ocr = ''.join(str(e) for e in ocr)
#             return jsonify({
#                 'status': 'Success',
#                 "metro": "dhaka metro-ga",
#                 "number": join_ocr
#             }), 200
#     else:
#         return jsonify({"error": "Method not allowed"}), 405


@app.route('/api/v2/server/upload-image', methods=['POST'])
def upload_anpr_v2():
    if request.method == 'POST':
        if "image_file" not in request.files:
            return jsonify({'status': 'No file part'}), 403
        raw_image = request.files['image_file'].stream
        # if raw_image.filename == '':
        #     return jsonify({'status': 'No selected file'}), 400
        images = Image.open(raw_image)
        detect_image = anpr_detector(images)
        if detect_image == False:
            return jsonify({'status': 'No detected image'}), 400
        else:
            convert_detect_image = np.asarray(detect_image)
            metro, metro_accracy, number, number_accracy = updateModel(
                convert_detect_image)
            return jsonify({
                'status': 'Success',
                "metro": metro,
                "metro_accracy": metro_accracy,
                "number": number,
                "number_accracy": number_accracy
            }), 200
    else:
        return jsonify({"error": "Method not allowed"}), 405


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9898)
