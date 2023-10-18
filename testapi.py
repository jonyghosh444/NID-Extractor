

import pprint

import requests

DETECTION_URL = 'http://localhost:9898/api/v2/server/upload-image'
IMAGE = 'exp2/front.jpeg'

# Read image
with open(IMAGE, 'rb') as f:
    image_data = f.read()

response = requests.post(DETECTION_URL, files={'image': image_data}).json()

pprint.pprint(response)