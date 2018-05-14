import os
import shutil

from skimage import io
# path = "F:\\Project\\Project\\YiTuClassify\\Picture\\Picture"
#
# file_dir = os.listdir(path)
#
# for file in file_dir:
#
#     files_dir = os.listdir(os.path.join(path,file))
#
#     for image in files_dir:
#         newname = image +'.bmp'
#         os.rename(os.path.join(path,file,image),os.path.join(path,file,newname))

#将bmp文件改成jpg格式
# img = io.imread('Damage2.bmp')
# img_jpg = io.imsave('Damage2.jpg',img)

#显示一张图片
# img_2 = io.imread('Damage2.jpg')
# io.imshow(img_2)
# io.show()

#改格式的同时改名字
# str = 'Damage2.bmp'
# img = io.imread(str)
# img_jpg = io.imsave(str[:-4]+'.jpg',img)

# 获取文件夹名字
# PATH_TO_TEST_IMAGES_DIR = 'K:\\YiTuClassify0409\\training20180423\\scratches\\scratches'
# print(os.path.split(PATH_TO_TEST_IMAGES_DIR)[-1])

# 复制图像到另一个文件夹
file_dir = 'F:\\Test\\TestA'
name = 'class'

file_list = os.listdir(file_dir)
# print(file_list)

for image in file_list:
    if image == "B.png":
        if os.path.exists(os.path.join(file_dir,'class_name')):
            shutil.copy(os.path.join(file_dir,image), os.path.join(file_dir, 'class_name'))
        else:
            os.makedirs(os.path.join(file_dir,'class_name'))
            shutil.copy(os.path.join(file_dir, image), os.path.join(file_dir, 'class_name'))



