import os
import json

files = os.listdir("Data")
print(files)
f = open('master.json','a')
for file in files:
    if ".json" in file:
        f2 = open(('Data\\' + file), 'r')
        print(file)
        data = json.load(f2)
        json.dump(data,f)

f.flush()
f.close()
