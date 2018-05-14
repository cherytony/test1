from skimage import io
import os

# 将bmp文件转换成jpg文件
# path = "F:\\Test\\TestA"
# list_dir = os.listdir(path)
#
# for image in list_dir:
#     print(image)
#     img = io.imread(os.path.join(path,image))
#     img_jpg = io.imsave(image[:-4]+'.jpg',img)


# 图片在单个文件夹时，将bmp文件转换成jpg文件
# path = "F:\\Test\\TestA"
# list_dir = os.listdir(path)
#
# for image in list_dir:
#     print(image)
#
#     img = io.imread(os.path.join(path, image))
#     img_jpg = io.imsave(os.path.join(path, image[:-4] + '.jpg'), img)


# 图片在分层文件夹时，将bmp文件转换成jpg文件
# images_dir = "F:\\Project\\Project\\YiTuClassify\\Picture\\Picture"
images_dir = 'F:\\Project\\Project\\YiTuClassify\\Picture\\Picture0426'

#分类文件夹
image_classes = os.listdir(images_dir)

for classes in image_classes:

    images = os.listdir(os.path.join(images_dir,classes))
    count =1
    for image in images:

        img = io.imread(os.path.join(images_dir,classes,image))
        img_jpg = io.imsave(os.path.join(images_dir,classes,classes+str(count))+'.jpg',img)
        count +=1
        os.remove(os.path.join(images_dir,classes,image))

