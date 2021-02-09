import subprocess

f = open("Application.txt", "r")
f1 = open("Paths.txt", "r")

lines = f.readlines()
size = len(lines)
for i in range(0, size): #CLEANING THE FUCKING \n off
    lines[i] = lines[i].strip()
lines1 = f1.readlines()


## WILL HAVE ISSUES IF REQUIRE ADMIN
## ALSO ADD IF CLOSE TO IT
## ADD LOWERCASE TO MATCH
## Add that adding new ones
## Fill out the microsoft Store apps
print(lines)
selectProgram = "UltraDefrag"
ind = lines.index(selectProgram)
print(lines1[ind])
subprocess.Popen(lines1[ind])
#subprocess.call(['C:\Program Files\Mozilla Firefox\\firefox.exe'])
