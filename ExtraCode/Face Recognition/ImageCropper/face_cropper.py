import cv2
import sys
import os


class FaceCropper(object):
    CASCADE_PATH = "haarcascade_frontalface_default.xml"

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(self.CASCADE_PATH)

    def generate(self, image_path, show_result):
        img = cv2.imread(image_path)
        if (img is None):
            print("Can't open image file")
            return 0

        
        faces = self.face_cascade.detectMultiScale(img, 1.25, 3, minSize=(100, 100))
        if len(faces) > 1:
            faces = self.face_cascade.detectMultiScale(img, 1.5, 3, minSize=(100, 100))
        if (faces is None):
            print('Failed to detect face')
            return 0

        if (show_result):
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            cv2.imshow('img', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        facecnt = len(faces)
        print("Detected faces: %d" % facecnt)
        i = 0
        height, width = img.shape[:2]

        for (x, y, w, h) in faces:
            r = max(w, h) / 2
            centerx = x + w / 2
            centery = y + h / 2
            nx = int(centerx - r)
            ny = int(centery - r)
            nr = int(r * 2)

            faceimg = img[ny:ny+nr, nx:nx+nr]
            lastimg = cv2.resize(faceimg, (64, 64))
            # Getting the new file name
            filePathSplit = os.path.splitext(image_path)
            extension = filePathSplit[1]
            filename = filePathSplit[0]
            i += 1
            while("/" in filename): # Cleaning up the filename (Since extended folders doesn't help)
                index = filename.index("/") + 1
                filename = filename[index::]
            while("\\" in filename):
                index = filename.index("\\") + 1
                filename = filename[index::]
            newLocation = 'face'
            if facecnt > 1:
                newLocation += 's'
            newLocation += '/'
            newName = newLocation + filename + str(i) + extension
            cv2.imwrite(newName, lastimg)


if __name__ == '__main__':
    baseDir = "Example/"
    paths = os.listdir(baseDir)
    print(paths)
#    image_path = "two_people.jpg"
    detecter = FaceCropper()
    for file in paths:
        if os.path.isfile(baseDir + file):
            detecter.generate(baseDir + file, False)
    
