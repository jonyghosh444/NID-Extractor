IMAGE = 'exp2/front.jpeg'

# Read image
with open(IMAGE, 'rb') as f:
    image_data = f.read()


print(image_data)