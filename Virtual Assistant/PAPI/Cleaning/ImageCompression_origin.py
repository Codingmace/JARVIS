import ntpath
import os

from PIL import Image
import piexif

# Author MasterWard

# Try a Different File Formats
# Prints cleaned and not number validly cleaned

#============================
# Test for positive words   =
#============================
def yesNo(cases):
    cases = cases.lower()
    return "yes" in cases or "true" in cases


#====================================
# Tests for valid file extensions   =
# Can't Do PNG                      =
#====================================
def validPhoto(filename):
    filename = filename.lower()
    return "jpeg" in filename or "jpg" in filename


def main():
    print("Welcome to cleaning JPG Files episode 11")
    print("How much are we cleaning")
    print("1. One File")
    print("2. One Directory")  # Not Tested
    print("3. One Directory and subdirectories")
    print("WARNING: Don't Try anything stupid.")
    print("- So don't do Anything I wouldn't do")

    co = input()
    if(co == '1'):
        optionOne();
    elif(co == '2'):
        optionTwo();
    elif(co == '3'):
        optionThree();
    else:
        print("That isn't an option. Goodbye")
    input("Press any button to end the program...")


#====================================
# Transfer/Clean the EXif of a file =
#====================================
def getOn(filename, new_file):
    im = Image.open(filename)
    try:
        exif_dict = piexif.load(im.info["exif"])
        exif_bytes = piexif.dump(exif_dict)
        im.save(new_file, "jpeg", exif=exif_bytes)
    except:
        print('shit')


#=============================
# Strips string to file name =
#=============================
def stripFileName(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


#====================================
# Returns an array with all the     =
# files that are valid in the       =
# directory and its sub directories =
#====================================
def allThePaths(mypath):
    f = []
    for (dirName, subdirlist, fileList) in os.walk(mypath):
        for fname in fileList:
            if validPhoto(fname):
                f.append(dirName + "\\" + fname)
    return f


#========================================
# Like allThePaths.                     =
# Only returns files from the directory =
# No sub directories                    =
#========================================
def shallowPath(mypath):
    f = []
    for (dirName, subdirlist, fileList) in os.walk(mypath):
        for fname in fileList:
            if validPhoto(fname):
                f.append(dirName + "\\" + fname)
        break;
    return f


#========================================
# Implements cleaning up just one file  =
# and replacing it or making a copy     =
#========================================
def optionOne():
    print("Awesome Just one file")
    filename = input("Enter the file path: ")
    if not validPhoto(filename):
        print("That is not a valid photo type")
        exit()
    replace = input("Are you going to be replacing the file? ")
    replacing = yesNo(replace);
    new_file = "";
    if not replacing:
        new_file = input("Input the file path ")
        if not os.path.exists(new_file):
            os.mkdir(new_file)
        new_file += "\\" + filename
    else:
        print("Awesome. One Conversion coming right up")
        new_file = filename

    # Cleans file
    print("Cleaning " + filename)
    getOn(filename, new_file)
    print("Done.")
    print("Have a good day")



#============================================
# Implements cleaning up on multiple files  =
# only in 1 directory (No SubDir)           =
#============================================
def optionTwo():
    print("One directory. Piece of cake after you answer some questions")
    valdir = False  # Valid directory input
    filename = "";
    while not valdir:
        filename = input("Input the directory name: ")
        if ntpath.isdir(filename):
            valdir = True
        else:
            print("That is not an valid directory. Try again")

    # Creating Target Destination
    replace = input("Are you going to be replacing the file? ")
    replacing = yesNo(replace);
    newPath = "";
    if not replacing:
        newPath = input("What are we going to call this new folder destination ")
        if not os.path.exists(newPath):
            os.mkdir(newPath)
    else:
        print("What a joy. Just replacing")

    # Gets files in the directory
    filenames = shallowPath(filename);
    # Cleans Files
    print("Now it is time for me to get to work")
    con = 0;
    for fil in filenames:
        print('Cleaning ' + os.path.basename(fil))
        con += 1
        if replacing:
            getOn(fil, fil)
        else:
            getOn(fil, newPath + "\\" + (stripFileName(fil)))
    print("Ha. I finished.\nHave a good day with your " + str(con) + " Cleaned files")



#================================================
# Implements cleaning up on                     =
# multiple files in 1 directory (and SubDirs)   =
#================================================
def optionThree():
    print("One directory and their children. That is just great")
    valdir = False  # Valid directory input
    filename = "";
    while not valdir:
        filename = input("Input the directory name: ")
        if ntpath.isdir(filename):
            valdir = True
        else:
            print("That is not an valid directory. Try again")

    # Creating Target Destination
    replace = input("Are you going to be replacing the file? ")
    replacing = yesNo(replace);
    newPath = "";
    if not replacing:
        newPath = input("What is the name of this destination folder ")
        if not os.path.exists(newPath):
            os.mkdir(newPath)
    else:
        print("Perfect. Just replacing")

    # Gets files in the directory
    filenames = allThePaths(filename);
    # Cleans Files
    print("Now lets get down to the good stuff")
    con = 0;
    for fil in filenames:
        print('Cleaning ' + os.path.basename(fil))
        con += 1
        if replacing:
            getOn(fil, fil)
        else:
            getOn(fil, newPath + "\\" + (stripFileName(fil)))
    print("I have finished.\nHave a good day with your " + str(con) + " Cleaned files")


main()
