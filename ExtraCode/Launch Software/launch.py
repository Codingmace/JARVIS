import subprocess
import getpass

f = open("Application.txt", "r")
username = getpass.getuser()
lines = f.readlines()
size = len(lines)
for i in range(0, size): #CLEANING THE FUCKING \n off
    lines[i] = lines[i].strip().replace("%USER%",username)
f.close()

f1 = open("Paths.txt", "r")
lines1 = f1.readlines()
size = len(lines1)
for i in range(0, size): #CLEANING FOR USER SPECIFIC
    lines1[i] = lines1[i].strip().replace("%USER%",username)
f1.close()

## WILL HAVE ISSUES IF REQUIRE ADMIN
## ALSO ADD IF CLOSE TO IT
## ADD LOWERCASE TO MATCH
## Add that adding new ones
## Fill out the microsoft Store apps
print(lines)
selectProgram = "Github Desktop"
ind = lines.index(selectProgram)
print(lines1[ind])
subprocess.Popen(lines1[ind])
#subprocess.call(['C:\Program Files\Mozilla Firefox\\firefox.exe'])
