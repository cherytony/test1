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
# file_dir = 'F:\\Test\\TestA'
# name = 'class'
#
# file_list = os.listdir(file_dir)
# # print(file_list)
#
# for image in file_list:
#     if image == "B.png":
#         if os.path.exists(os.path.join(file_dir,'class_name')):
#             shutil.copy(os.path.join(file_dir,image), os.path.join(file_dir, 'class_name'))
#         else:
#             os.makedirs(os.path.join(file_dir,'class_name'))
#             shutil.copy(os.path.join(file_dir, image), os.path.join(file_dir, 'class_name'))

# 文件夹
# PATH_TO_TEST_IMAGES_DIR = '/home/yqw/YiTuClassify0409/Picture/training20180428'
# class_names = os.listdir(PATH_TO_TEST_IMAGES_DIR)
# print(class_names)
#
# for class_name in class_names:
#
#     class_name_path = os.path.join(PATH_TO_TEST_IMAGES_DIR,class_name)
#     images = os.listdir(class_name_path)
#     for image in images:
#         print(image)


# 统计数据脚本
path = '/home/yqw/YiTuClassify0409/Picture/training20180428'

def statics(path):

    result = {}

    class_names = os.listdir(path)

    for class_name in class_names:
        print("class_name:",class_name)
        images = os.listdir(os.path.join(path,class_name))
        print("images:",images)
        result[class_name] = {}
        for image in images:
            num =0
            print("image: ",image)
            if os.path.isdir(os.path.join(path,class_name,image)):
                num = dir_statics(os.path.join(path,class_name,image))
                print("num: ",num)

                result[class_name][image]=num


    print(result)

def dir_statics(dir_path):
    num_files=0

    for fn in os.listdir(dir_path):
        num_files +=1

    return num_files

if __name__ =="__main__":
    statics(path)




