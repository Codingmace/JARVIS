import os
import json
import jsonmerge  #NEED TO DOWNLOAD THIS

# print(jsonmerge.objectMerge("a.json","b.json"))
'''
a = json.load(open("output0.json"))
b = json.load(open("output1.json"))
c = {**a,**b}
#c = a.append(b)
#c = a.extend(b)

print(len(a['data']))
#print(a)
print(len(b['data']))
#print(b)
print(len(c['data']))
'''
files = os.listdir("Data")
print(files)
f = open('master.json','a')
a = json.dumps(json.load(f))

for file in files:
    if ".json" in file:
        f2 = open(('Data\\' + file), 'r')
        dictB = json.load(f2)
        bStr = json.dumps(dictB)
        lastIndex = bStr.rindex("}")
        print(bStr[0:lastIndex - 1])
        a += bStr + ","

a += "]}"
json.dump(dictA,f)

f.flush()
f.close()
