from typing import Tuple
import numpy as np
import cv2
# from model.NumberModel import NumberModel
import easyocr
from PIL import Image

def extractedData(img):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(img)
    return result




