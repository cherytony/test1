from skimage import io,transform
import  os

#将不规则的图像reshape(600,600)
path = "F:\\Project\\Project\\YiTuClassify\\Picture\\Picture"
list_dir = os.listdir(path)

for file_dir in list_dir:
    files = os.listdir(os.path.join(path,file_dir))
    for image in files:
        img = io.imread(os.path.join(path,file_dir,image))
        img = transform.resize(img,(600,600))
        io.imsave(image,img)

# for list in list_dir:
#     if('.jpg' in list ):
#         img = io.imread(os.path.join(root,'images/validation/',list))
#         img = transform.resize(img,(624,832))
#         io.imsave(list,img)
#         # io.imshow(img)
#         # io.show()

