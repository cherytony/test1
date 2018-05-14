from skimage import io,transform
import os

#将不规则的图像reshape(240,240)
# path = "F:\\Project\\Project\\YiTuClassify\\Picture\\JPG_Picture"
# path = "/home/yqw/Github/YiTuClassify/Picture_to_JPG_Nature"
# path = "F:\Project\Project\YiTuClassify\Picture_240\OK"
path = "F:\\Project\\Project\\YiTuClassify\\Picture\\Picture0426_240"
list_dir = os.listdir(path)

for images in list_dir:
    image_dir = os.listdir(os.path.join(path,images))
    for image in image_dir:
      img = io.imread(os.path.join(path,images,image))
      img = transform.resize(img,(240,240))
      io.imsave(os.path.join(path,images,image),img)

# for list in list_dir:
#     if('.jpg' in list ):
#         img = io.imread(os.path.join(root,'images/validation/',list))
#         img = transform.resize(img,(624,832))
#         io.imsave(list,img)
#         # io.imshow(img)
#         # io.show()

