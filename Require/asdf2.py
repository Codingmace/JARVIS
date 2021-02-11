
minimal = [2, 3, 13, 18, 20, 35, 38, 44]
basic = [0, 14, 17, 23, 24, 25, 27, 29, 30, 31, 40, 45] # Minimal
speech = [4, 28, 32, 34, 41] # Basic
google = [1, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 19, 21, 22, 26, 33, 36, 37, 39, 42, 43] # Basic


f0 = open("0_Minimal.txt", "r")
lin0 = f0.readlines()
f1 = open("1_Basic.txt", "r")
lin1 = f1.readlines()
f2 = open("2_Speech.txt", "r")
lin2 = f2.readlines()
f3  = open("3_Google.txt", "r")
lin3 = f3.readlines()
f4 = open("4_RequAll.txt", "r")
allLines = f4.readlines()
# print(lines)
temp0 = []
temp1 = []
temp2 = []
temp3 = []

print("Minimal")
for line in lin0:
    if line not in allLines:
        print(line + " has not been found")
    else:
        temp0.append(allLines.index(line))

print("Basic")
for line in lin1:
    if line not in allLines:
        print(line + " has not been found")
    else:
        temp1.append(allLines.index(line))



print("Speech")
for line in lin2:
    if line not in allLines:
        print(line + " has not been found")
    else:
        temp2.append(allLines.index(line))

print("Google")
for line in lin3:
    if line not in allLines:
        print(line + " has not been found")
    else:
        temp3.append(allLines.index(line))

# Removing Minimal
for i in temp0:
    temp1.remove(i)
    temp2.remove(i)
    temp3.remove(i)

# Removing Basic 
for i in temp1:
    temp2.remove(i)
    temp3.remove(i)
    
print("Minimal ",temp0)
print("Basic ",temp1)
print("Speech ", temp2)
print("Google ", temp3)
