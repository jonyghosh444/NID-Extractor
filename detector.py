import torch
from PIL import Image
from flask import jsonify

model = torch.hub.load('mod',
                       'custom',
                       path='mod/det_best.pt',
                       source='local')  # local repo
model.conf = 0.65  # confidence threshold (0-1)


def nid_detector(image_pillow_object):
    try:
        results = model(image_pillow_object, size=1088)
        results = results.pandas().xyxy[0]
        crop_images_dict = {}
        # crop_images = []
        for i in range(len(results)):
            xmin, ymin, xmax, ymax = results['xmin'][i], results['ymin'][i], results['xmax'][i], results['ymax'][i]
            if results['name'][i] == "ename" or results['name'][i] == "nid" or results['name'][i] == "dob":
                width = (results['xmax'][i] - results['xmin'][i])
                height = (results['ymax'][i] - results['ymin'][i])

                if(height>width):
                    print("if")
                    crop_img = image_pillow_object.crop((xmin, ymin, xmax, ymax))
                    crop_img = crop_img.transpose(Image.ROTATE_90)
                    crop_images_dict[results['name'][i]]= crop_img
                    # crop_images.append(crop_img)

                    # crop_img.show()
                else:
                    print("else")
                    crop_img = image_pillow_object.crop((xmin, ymin, xmax, ymax))
                    print(f"img: {crop_img}")
                    crop_images_dict[results['name'][i]]= crop_img
                    # crop_images.append(crop_img)
                    # crop_img.show()     
        return crop_images_dict
    except:
        return False


#testing6

# from PIL import Image

# anpr = nid_detector(
#     Image.open(
#         "exp2/front.jpeg"))

# print(anpr)

# from nidOcr import extractedData
# import numpy as np

# nid = np.array(anpr['nid'])
# dob = np.array(anpr['dob'])
# ename = np.array(anpr['nid'])
# nid_txt = extractedData(nid)
# dob_txt = extractedData(dob)
# ename_txt = extractedData(ename)
# txt ={
#             'status': 'Success',
#             "Name": ename_txt[0][1],
#             "Date of birth": dob_txt[0][1],
#             "NID Number": nid_txt[0][1],
#      }
    
# print(txt)


    
    


