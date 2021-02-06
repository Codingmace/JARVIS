import hashlib
import os


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
        print(size)
        return size

def main():
#    ar = paths("../../brute-force/")
#    ar = paths("C:\\Users\\Master\\Desktop\\sd\\brute-force\\_2")
    ar = paths("C:\\Users\\Master\\Desktop\\sd\\brute-force\\10")
    print(ar[0])
    print(str(hashFile(ar[1])) + "100")
    for name in ar:
        print(str(hashFile(name))+ str(fileSize(name)))

main()
