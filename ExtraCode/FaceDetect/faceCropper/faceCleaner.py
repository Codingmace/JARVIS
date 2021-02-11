import cv2
import sys
import os
from send2trash import send2trash



if __name__ == '__main__':
    CASCADE_PATH = "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(self.CASCADE_PATH)
    # It is going to be double so we get Dir then files of dir
    peopleDirect = os.listdir("./")
    for direct in peopleDirect:
        print("We are now moving to the people")
        paths = os.listdir(direct)
# Now we just have to determine if there is a face or not
        for p in paths:
            print( p + " Is the current file checking")
            print("Maybe check that it is a file")
            img = cv2.imread(p)
            if (img is None):
                print("Can't open image file")
                send2trash(img)
            else:
                faces = face_cascade.detectMultiScale(img, 1.25, 3, minSize=(100, 100))
                if (faces is None):
                    print("Failed to detect face")
                    send2trash(img)
                else:
                    facecnt = len(faces)
                    if facecnt == 0:
                        print("Have not found face so deleting")
                        send2trash(img)
