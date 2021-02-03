import json

print("Started Reading JSON file")
dex = []
for i in range(0,1214):
    try:
        with open(("Data\output" +str(i) + ".json"), "r") as read_file:
            #print("Converting JSON encoded data into Python dictionary")
            print(i)
            developer = json.load(read_file)
            #print(developer['data'])
            for x in developer['data']:
               # print(x['id'])
                del x['date']
                del x['subject']
                del x['recorded-or-robo']
                del x['city']
                del x['state']
                dex.append(x)
    except:
        print("the file " + str(i)+ "")

            
# print("Decoded JSON Data From File")
# for key, value in dex.items():
#    print(key, ":", value)
# print("Done reading json file")

    

# Turning dict to file
with open('result.json', 'w') as fp:
    json.dump(dex, fp)
