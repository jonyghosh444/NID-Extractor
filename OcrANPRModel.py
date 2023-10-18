from typing import Tuple
import numpy as np
import cv2
# from model.NumberModel import NumberModel
import easyocr

reader = easyocr.Reader(["bn"])


# def mainModel(image):

#     model = NumberModel.numberModel()
#     model.load_weights('model/weight2.h5')
#     img = image
#     img2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     box_cor = []
#     number = []
#     accuracy = []

#     cvNet = cv2.dnn.readNetFromTensorflow('model/number.pb',
#                                           'model/number.pbtxt')
#     rows = img.shape[0]
#     cols = img.shape[1]
#     cvNet.setInput(
#         cv2.dnn.blobFromImage(img, size=(400, 400), swapRB=True, crop=False))
#     cvOut = cvNet.forward()

#     for detection in cvOut[0, 0, :, :]:
#         score = float(detection[2])
#         if score > 0.3:
#             # left = int( detection[3] * cols )
#             # top = int( detection[4] * rows )
#             # right = int( detection[5] * cols )
#             # bottom = int( detection[6] * rows )
#             # cv2.rectangle( img, (int( left ), int( top )), (int( right ), int( bottom )), (23, 230, 210),
#             #               thickness=1 )
#             # cv2.imwrite("sfter.jpg",img)
#             box_cor.append(detection)
#     # cv2.imshow( "plateDetection", img )
#     # cv2.waitKey()
#     # cv2.destroyAllWindows()

#     box_cor = sorted(box_cor, key=lambda a_entry: a_entry[3])

#     for i in box_cor:
#         _, _, _, left, top, right, bottom = i
#         left = int(left * cols)
#         top = int(top * rows)
#         right = int(right * cols)
#         bottom = int(bottom * rows)
#         temp = img2[top:bottom, left:right]
#         temp = cv2.resize(temp, (32, 32))
#         temp = np.expand_dims(temp, axis=0)
#         temp = np.expand_dims(temp, axis=3)
#         # model._make_predict_function()
#         p = model.predict(temp)
#         accuracy.append(p[0, np.argmax(p)])
#         number.append(np.argmax(p))
#     # number = str(number)
#     # accuracy = str(accuracy)
#     # print(number)
#     return number, accuracy


def updateModel(image: np.ndarray) -> Tuple[str, int, str, int]:
    '''
    Update the model with the new image.
    :param image: Image to update the model with.
    :return: The number, accuracy, and the confidence of the model.
    '''
    result = reader.readtext(image)
    # print(result)
    metro, metro_accracy, number, number_accracy = "", 0, "", 0
    if len(result) == 2:
        metro = result[0][1]
        metro_accracy = result[0][2]
        number = result[1][1]
        number_accracy = result[1][2]
    return metro, metro_accracy, number, number_accracy
