
import argparse
import io

import torch
from flask import Flask, request,jsonify
from PIL import Image
from detector import nid_detector
from nidOcr import extractedData
import numpy as np

app = Flask(__name__)
models = {}

DETECTION_URL = '/api/v2/server/upload-image'
SERVER_STATUS_URL = '/api/v1/server/status'

@app.route(SERVER_STATUS_URL, methods=['GET'])
def server_health():
    return jsonify({'status': 'Service UP'}), 200


@app.route(DETECTION_URL, methods=['POST'])
def predict():
    if request.method != 'POST':
        return jsonify({"error": "Method not allowed"}), 405
    if "image" not in request.files:
        return jsonify({'status': 'No file part'}), 403    

    raw_image = request.files['image'].stream
    images = Image.open(raw_image)
    detect_image = nid_detector(images)
    if detect_image == False:
        return jsonify({'status': 'No detected image'}), 400
    else:
        nid = np.array(detect_image['nid'])
        dob = np.array(detect_image['dob'])
        ename = np.array(detect_image['nid'])
        nid_txt = extractedData(nid)
        dob_txt = extractedData(dob)
        ename_txt = extractedData(ename)
        return jsonify({
            'status': 'Success',
            "Name": ename_txt[0][1],
            "Date of birth": dob_txt[0][1],
            "NID Number": nid_txt[0][1],
        }), 200



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9898)