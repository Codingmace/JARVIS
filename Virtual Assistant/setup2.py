def getGoogle():
    return "google-api-python-client google-auth-httplib2 google-auth-oauthlib dnspython tld wikipedia "
    
def getSpeech():
    return "pytsx3 speech_recognition "

def getCamera():
    return "piexif Pillow pyautogui opencv-python "

def getMinimal():
    return "psutil requests datetime beautifulsoup4 "
    # re webbrowser json shutil ntpath fnmatch zipfile socket threading platform getpass smtplib
    # ISSUE hashlib

print("First a bundle packs. Enter the number below of selection")
print("1. Mega : Everything")
print("2. Command : Everything - Speech Recognition")
print("3. Talkative : Everything - Camera")
print("4. Mailless : Everything - Google")
print("5. Minimal : Bare minimum for it to run well")
print("6. Custom : Whatever you want")
print("7. More info : Explination of one")
print("8. HEEELLLLLPPPPP")
      

requireMade = False # Make true once writting to file
while not requireMade:
    selection = input("Enter your selection : ")
    choice = 7
    requireMade = not requireMade
    try: 
        choice = int(selection)
    except:
        print("That isn't a number choice. I am going with number 6")

    requireFileString = ""
    if choice == 1:
        print("Ok building file")
        requireFileString = getMinimal() + getGoogle() + getSpeech() + getCamera()
        
        
    elif choice == 2:
        print("Ok building file with Everything Except Speech")
        requireFileString = getMinimal() + getGoogle() + getCamera()
    
    elif choice == 3:
        print("Ok building without Camera")
        requireFileString = getMinimal() + getGoogle() + getSpeech()

    elif choice == 4:
        print("Ok building without Google")
        requireFileString = getMinimal() + getSpeech() + getCamera()
        
    elif choice == 5:
        print("Ok building bare minimum")
        print("That means no camera, no google, no talking. Nothing")
        requireFileString = getMinimal()
        
    elif choice == 6:
        print("Ok So you want to choose. How brave")
        print("1. Google\n2. Speech\n3. Camera")
        selection = input("Which add on would you like (Seperate with ,) : ")
        split = selection.split(",")
        requireFileString = getMinimal()
        for s in split:
            currentSelection = s.strip()
            if currentSelection == 1:
                requireFileString += getGoogle()
            elif currentSelection == 2:
                requireFileString += getSpeech()
            elif currentSelection == 3:
                requireFileString += getCamera()
        
    elif choice == 7:
        print("Let me break this down")
        print("If you do not have much space... Select 5")
        print("If you want all features except one Select 2-4")
        print("If something else choose 6")
        print("Finally if you are still clueless choose 7")

    elif choice == 8:
        print("Thank you so much for choosing this.")
        print("Here is what each one is")
        print("Google : "+ getGoogle())
        print("Speech Recognition : " + getSpeech())
        print("Camera : " + getCamera())
        print("Minimum : " + getMinimal())
        print("Any more questions, report it to the complaint box")
        
    else:
        print("You done fucked. I am a nice computer and will give you another chance.")

print("Ok so we are done with that. Awesome. You are ready to go. Have a nice day")


f = open("part1.txt", "r")
lines = f.readlines()
for line in lines:
    print(line.strip())
f.close()

f1 = open("part2.txt", "r")
lines = f1.readlines()
for line in lines:
    print(line.strip())
f1.close()

input()
