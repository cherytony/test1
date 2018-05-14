import os


path = "C:\\Users\\Administrator\\Desktop\\汇总\\汇总"

file_dir = os.listdir(path)

for classes in file_dir:

    count = 1

    file_list = os.listdir(path,classes)

    for image in file_list:
        newname = classes + str(count) + '.jpg'
        os.rename(os.path.join(path, classes,image), os.path.join(path, newname,newname))
        os.remove(os.path.join(path,classes,image))
        count += 1
    #files_dir = os.listdir(os.path.join(path, classes))
    #for classes in files_dir:

