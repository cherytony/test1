from PIL import Image
import os

PATH = r'D:\picture\2018092902'
SAVE_PATH = r'D:\save_picture'

image_fold = os.listdir(PATH)

# for image_dir in image_fold:
#     images = os.listdir(os.path.join(PATH, image_dir))
#     for image in images:
#         img = Image.open(os.path.join(PATH, image_dir, image))
#         w, h = img.size
#         img = img.resize((624, 832)).save(os.path.join(PATH, image_dir, image))

img = Image.open("20180929_155901.jpg")
w, h = img.size
print(w, h)
img.resize((w // 4, h // 4)).save('1.jpg', 'JPEG')
