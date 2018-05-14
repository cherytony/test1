from skimage import io,transform
import os

#将不规则的图像reshape(240,240)
# path = "F:\\Project\\Project\\YiTuClassify\\Picture\\JPG_Picture"
# path = "/home/yqw/Github/YiTuClassify/Picture_to_JPG_Nature"
# path = "F:\Project\Project\YiTuClassify\Picture_240\OK"
path = "F:\Project\Project\YiTuClassify\Picture_240"
list_dir = os.listdir(path)

count =1
for images in list_dir:

    image_dir = os.listdir(os.path.join(list_dir,images))
    for image in image_dir:

        #重命名
        newname = 'ok' + str(count) + '.bmp'
        os.rename(os.path.join(path, image), os.path.join(path, newname))
        count += 1




