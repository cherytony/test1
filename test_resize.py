from PIL import Image
import os
image = Image.open("mifeng.png")
image_1 = image.resize((624,832),Image.BILINEAR)
image_1.save("mifeng1.png")
