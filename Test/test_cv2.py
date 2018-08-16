from PIL import Image
from pylab import *

pil_im = Image.open("mifeng.png")
im = array(pil_im)
print(im.shape, im.dtype)
imshow(im)
show()

out = pil_im.rotate(45)
im_out = array(out)
print(im.shape, im.dtype)
imshow(im_out)

show()
