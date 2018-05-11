import itchat
import math
import PIL.Image as Image
import os
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
# itchat.auto_login(hotReload=True)
# friends = itchat.get_friends(update=True)[0:]
# user = friends[0]["UserName"]

image_local_dir = "C:/Users/yoho/Desktop/imageHead2"

# num = 0
# for i in friends:
#     img = itchat.get_head_img(userName=i["UserName"])
#     fileImage = open(image_local_dir + "/" + str(num) + ".jpg",'wb')
#     fileImage.write(img)
#     fileImage.close()
#     num += 1

ls = os.listdir(image_local_dir)
size = 640
each_size = int(math.sqrt(float(size*size)/len(ls)))
lines = int(size/each_size)
image = Image.new('RGBA', (size, size))
x = 0
y = 0
for i in range(0,len(ls)+1):
    try:

        img = Image.open(image_local_dir + "/" + str(i) + ".jpg")
    except IOError:
        print("Error")
    else:
        img = img.resize((each_size, each_size), Image.ANTIALIAS)
        image.paste(img, (x * each_size, y * each_size))
        x += 1
        if x == lines:
            x = 0
            y += 1
image.save(image_local_dir + "/" + "all.jpg")
# itchat.send_image(image_local_dir + "/" + "all.jpg", 'filehelper')