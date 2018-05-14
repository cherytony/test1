import os
from skimage import io

# path = "F:\\Project\\Project\\YiTuClassify\\Picture\\Picture"
path = "F:\Project\YiTuClassify\ok"

file_dir = os.listdir(path)

for classes in file_dir:


    #files_dir = os.listdir(os.path.join(path, classes))
    #for image in files_dir:
    img = io.imread(os.path.join(path, classes))
    img_jpg = io.imsave(classes[:-4] + '.jpg', img)

