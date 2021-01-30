import ntpath
import os

from PIL import Image
import piexif

# Author MasterWard

# Try a Different File Formats
# Prints cleaned and not number validly cleaned
#===============================================================================
# Test for positive words
#===============================================================================
def yesNo(cases):
    valid = {'yes', 'YES', 'true'}
    for v in valid:
        if v == cases:
            return True;
    return False;


#===============================================================================
# Tests for valid file extensions
# Can't Do PNG
#===============================================================================
def validPhoto(filename):
    valid = {'jpg', 'JPG', 'jpeg', 'JPEG'}
    for v in valid:
        if v in filename:
            return True;
    return False;    


def main():
    print("Welcome to cleaning JPG Files episode 10")
    print("How much are we cleaning")
    print("1. One File")  # Tested. Works
    print("2. Multiple Files")  # Tested. Fragile but works
    print("3. One Directory")  # Not Tested
    print("4. Multiple Directories")  # Not Tested
    print("5. One Directory and subdirectories")  # Tested. Works
    print("6. Multiple Directories and subdirectories")  # Semi works. Leaves out some
    print("WARNING: Don't Try anything stupid. This will include the following")
    print("- Try number 6 and expect results")
    print("- Enter full file paths put in a folder without files")
    print("- Lastly anything I wouldn't do")
          
    co = input()
    if(co == '1'):
        justOne();
    elif(co == '2'):
        justTwo();
    elif(co == '3'):
        justThree();
    elif(co == '4'):
        justFour();
    elif(co == '5'):
        justFive();
    elif(co == '6'):
        justSix();
    else:
        print("That isn't an option. Goodbye")
    input("Press any button to end the program...")


#===============================================================================
# Transfer/Clean the EXif of a file
#===============================================================================
def getOn(filename, new_file):
    im = Image.open(filename)
    try:
        exif_dict = piexif.load(im.info["exif"])
        exif_bytes = piexif.dump(exif_dict)
        im.save(new_file, "jpeg", exif=exif_bytes)
    except:
        print('shit')


#===============================================================================
# Strips string to file name
#===============================================================================
def stripFileName(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


#===============================================================================
# Returns an array with all the files that are valid in the directory
# and its sub directories
#===============================================================================
def allThePaths(mypath):
    f = []
    for (dirName, subdirlist, fileList) in os.walk(mypath):
        for fname in fileList:
            if validPhoto(fname):
                f.append(dirName + "\\" + fname)
    return f


#===============================================================================
# Like allThePaths. Only returns files from the directory (no sub directories)
#===============================================================================
def shallowPath(mypath):
    f = []
    for (dirName, subdirlist, fileList) in os.walk(mypath):
        for fname in fileList:
            if validPhoto(fname):
                f.append(dirName + "\\" + fname)
        break;
    return f


#===============================================================================
# Implements cleaning up just one file and replacing it or making a copy
#===============================================================================
def justOne():
    print("Awesome Just one file")
    filename = input("Enter the file path: ")
    if not validPhoto(filename):
        print("Screwed up you have")
        print("Can't do anything to help you.")
        print("Goodbye")
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
    
    
#===============================================================================
# Implements cleaning up on multiple files but not directories
#===============================================================================
def justTwo():
    print("Ok a couple of files not something to hard")
    # Inputting file paths
    filenames = []
    fileMore = ''
    print("Enter in the file name and when you're done enter \"done\"")
    while(not fileMore == 'done'):
        fileMore = input();
        if os.path.isfile(fileMore):  # If valid File
            print(fileMore + " has been added")
            filenames += fileMore
        elif os.path.isdir(fileMore):  # If is a directory
                print("That doesn't work because that is a directory")
        elif fileMore != 'done':
            print(fileMore + " does not exist")
            print("Maybe there is a typo. Try again")
    
    # Creating Target Destination
    replace = input("Are you going to be replacing the file? ")
    replacing = yesNo(replace);
    newPath = "";
    if not replacing:
        newPath = input("Input the new folder leaf (Folder copying place) ")
        if not os.path.exists(newPath):
            os.mkdir(newPath)
    else:
        print("Glad to hear that. Less work for me")
        
    # Cleans Files
    print("Now it is time for me to get to work")
    con = 0;
    for fil in filenames:
        print('Cleaning ' + os.path.basename(fil))
        con += 1
        if replacing:
            getOn(fil, fil)
        else:
            getOn(fil, newPath + "\\" + fil)
    print("All done with that\nHave a good day with your " + str(con) + " Cleaned files")


#===============================================================================
# Implements cleaning up on multiple files only in 1 directory (No SubDir)
#===============================================================================
def justThree():
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

    
#===============================================================================
# Implements cleaning up multiple files from multiple directories (No subdir)
#===============================================================================
def justFour():
    print("More than one directory. Really putting the program to the test")
    # Inputting directory paths
    dirnames = []
    dirMore = ''
    print("Enter in the directory name and when you're done enter \"done\"")
    while(not dirMore == 'done'):
        dirMore = input();
        if os.path.isdir(dirMore):  # If valid directory
            print(dirMore + " has been added")
            dirnames += dirMore
        elif os.path.isfile(dirMore):  # If is a file
                print("That doesn't work because that is a file")
        elif dirMore != 'done':
            print(dirMore + " does not exist")
            print("You Done Goof. Try again")
    # Creating Target Destination
    replace = input("Are you going to be replacing the file? ")
    replacing = yesNo(replace);
    newPath = "";
    if not replacing:
        newPath = input("What do you call this directory? ")
        if not os.path.exists(newPath):
            os.mkdir(newPath)
    else:
        print("Splendid. Just a replacement")
    # Gets files in the Directories
    filenames = []
    for x in dirnames:
        filenames += shallowPath(x)
    # Cleans Files
    print("We got all the data. Let us now begin")
    con = 0;
    for fil in filenames:
        print('Cleaning ' + os.path.basename(fil))
        con += 1
        if replacing:
            getOn(fil, fil)
        else:
            getOn(fil, newPath + "\\" + (stripFileName(fil)))
    print("That wasn't too hard.\nHave a good day with your " + str(con) + " Cleaned files")


#===============================================================================
# Implements cleaning up on multiple files in 1 directory (and SubDirs)
#===============================================================================
def justFive():
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


#===============================================================================
# Implements cleaning up multiple files from multiple directories (No subdir)
#===============================================================================
def justSix():
    print("You want the Most. This is the max capability of the program")
    # Inputting directory paths
    dirnames = []
    dirMore = ''
    print("Enter in the directory name and when you're done enter \"done\"")
    while(not dirMore == 'done'):
        dirMore = input();
        if os.path.isdir(dirMore):  # If valid directory
            print(dirMore + " has been added")
            dirnames += dirMore
        elif os.path.isfile(dirMore):  # If is a file
                print("That doesn't work because that is a file")
        elif dirMore != 'done':
            print(dirMore + " does not exist")
            print("You Screwed up. Try again")
    # Creating Target Destination
    replace = input("Are you going to be replacing the file? ")
    replacing = yesNo(replace);
    newPath = "";
    if not replacing:
        newPath = input("What do you call this destination directory? ")
        if not os.path.exists(newPath):
            os.mkdir(newPath)
    else:
        print("Zipping Zebras. Just a replacement")
    # Gets files in the Directories
    filenames = []
    for x in dirnames:
        filenames += allThePaths(x)
    # Cleans Files
    print("Galloping Gallardo. We better get started")
    con = 0
    for fil in filenames:
        print('Cleaning ' + os.path.basename(fil))
        con += 1
        if replacing:
            getOn(fil, fil)
        else:
            getOn(fil, newPath + "\\" + (stripFileName(fil)))
    print("DAMN THAT WAS HARD.\nAt least we are done and cleaned " + str(con) + " files")


main()
