from skimage import io,transform
import  os

path = r"C:\Users\Administrator\dataset\m1.jpg"

img = io.imread(os.path.join(path))
img = transform.resize(img,(240,240))
io.imsave(os.path.join(r"C:\Users\Administrator\dataset",'new.jpg'),img)
