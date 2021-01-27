import os
import json
from jsonmerge import merge  #NEED TO DOWNLOAD THIS 
#### THIS FAILED
files = os.listdir("Data")
print(files)
f = open('master.json','a')
dictA = dict()
out = dict()
for file in files:
    if ".json" in file:
        f2 = open(('Data\\' + file), 'r')
        dictB = json.load(f2)
#        dictA.update(dictB)
        out = merge(dictA, dictB)
        dictA = out
#        print(dictB + dictB.update(dictA))
#        print(len(dictB['data']))
        #out = dictA.items() + dictB.items()
       # dictA = out
#        merged_dict = {key: value for (key, value) in (dictA.items() + dictB.items())}
#        dictA = merged_dict
#        jsonString_merged = json.dumps(merged_dict)
        print(len(json.dumps(dictA)))

json.dump(dictA,f)

f.flush()
f.close()
