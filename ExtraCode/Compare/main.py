import os
import hashlib
from send2trash import send2trash
def hashFile(filename):
    hasher = hashlib.md5()
    with open(filename, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()


def paths(path):
    #we shall store all the file names in this list
    filelist = []

    for root, dirs, files in os.walk(path):
            for file in files:
            #append the file name to the list
                    filelist.append(os.path.join(root,file))
    return filelist

def fileSize(path):
    with open(path, 'r') as f:
        size = f.seek(0, os.SEEK_END)
        return size


def cleanup(path):
    print("Cleaning up")
    ar = paths(path)
    fileList = []
    for name in ar:
        curStr = str(hashFile(name))+ str(fileSize(name))
#        if len(fileList) > 10000:
#            fileList = []
        if curStr in fileList:
            send2trash(name)
            print("Sending", name, "to the trash")
        else:
            fileList.append(curStr)
    del fileList

# for i in range(1000, 10000,1):
#     cleanup("C:\\Users\\Master\\Desktop\\sd\\brute-force\\BackupForce_1000-10000\\BackupForce\\"+str(i))
cleanup("C:\\Users\\Master\\Desktop\\sd\\brute-force\\")
   
