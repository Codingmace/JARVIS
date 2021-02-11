


f1 = open("asdf.txt", "r")
lines= f1.readlines()
print(lines)

minimal = [0,1,2,3,4,5,6,7] # 0 - 7
basic = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # 0 -20
speech = [0, 25] # 0-25
google = [0-20] # Basic plus ending
f = open("requirements.txt", "w")
for m in minimal:
    print(lines[m].strip())
    f.write(lines[m])
print()
for b in basic:
    print(lines[b].strip())
print()


f.flush()
f.close()
