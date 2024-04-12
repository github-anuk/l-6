import os
import cv2
from PIL import Image

os.chdir("C:/Users/Anukriti/Desktop/all my files (anukriti)/python/projects/open cv/l-6/photo")
path = "C:/Users/Anukriti/Desktop/all my files (anukriti)/python/projects/open cv/l-6/photo"

mean_height=0
mean_width = 0

num_of_images = len(os.listdir("."))
print(os.listdir("."))
print("num of img",num_of_images)

for file in os.listdir("."):
    img=Image.open(os.path.join(path,file))
    width,height=img.size
    mean_width = mean_width+width
    mean_height=mean_height+height

mean_height=mean_height//num_of_images
mean_width=mean_width//num_of_images

print("means1 : ",mean_width)
print("means2",mean_height)

for file in os.listdir("."):
    img=Image.open(os.path.join(path,file))
    imgResized=img.resize((mean_width,mean_height))
    imgResized.save(file,"PNG",quality = 95)
    print("Image resized sucessful")


def VideoGenerator():
    video_name="myFirstVideo.avi"
    os.chdir("C:/Users/Anukriti/Desktop/all my files (anukriti)/python/projects/open cv/l-6/photo")
    images=[]
    for img in os.listdir("."):
        images.append(img)


    frame=cv2.imread(os.path.join(".", images[0]))
    height,width,layer = frame.shape

    #cv2.VideoWriter(filename,fourcc,fps,framesize)
    video = cv2.VideoWriter(video_name,0,1,(width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(".", image)))

    cv2.destroyAllWindows()
    video.release()

VideoGenerator()
    