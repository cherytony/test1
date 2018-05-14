import os
import pandas as pd

path = 'C:\\Users\\Administrator\\Desktop\\汇总\\汇总\\damage'

classes_list = os.listdir(path)

list_all =[]
for image in classes_list:
    count=0
    if os.path.isfile(os.path.join(path,image)):
        count +=1
    else:

        os.path.isdir(os.path.join(path,image))
        image_list = os.listdir(os.path.join(path,image))
        dict = {image:len(image_list)}
        list_all.append(dict)
    list_all.append({'damage':count})

    # df = pd.DataFrame(list)
    # df.to_csv('output_statics_csv.csv', index=False, header=False)

    print(list_all)


