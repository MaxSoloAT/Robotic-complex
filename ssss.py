import urllib.request
import os
import numpy
from PIL import Image
def store_raw_images():
    neg_images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03679712'   
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 1
    a=5590
    #
    if not os.path.exists('neg'):
        os.makedirs('neg')
        
    for i in neg_image_urls.split("\n"):
        try:
           print(i)
           urllib.request.urlretrieve(i, "neg/"+str(pic_num+a)+".jpg")
           imP = Image.open("neg/"+str(pic_num+a)+".jpg")
           if not imP.mode == 'RGB':
                imP = imP.convert('RGB')
           imP.save("neg/"+str(pic_num+a)+".jpg")
           pic_num += 1
            
        except Exception as e:
            print(str(e)) 


store_raw_images()
