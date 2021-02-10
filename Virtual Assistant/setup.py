print("Hello and welcome to the setup of Tobias")
print("This program is a little big if you download everything")
print("I made it better by only downloading what you need")
print("Well let us begin")
rapidValid = False
rapidApiSelect = input("Do you have a rapidAPIKey (yes/no)? ")
rapidApi = ""
if "yes" in rapidApiSelect.lower():
    while not rapidValid:
        rapidApi = input("Please input your rapidApiKey now: ").strip()
        if len(rapidApi) == 50:
            print("The length is 50 so most likely a valid key")
            rapidValid = True
        else:
            print("That doesn't seem to be the right. Length of " + len(rapidApi))
            temp = input("Is " +rapidApi + " correct (yes/no)?")
            rapidValid = "yes" in temp.lower()
        
else:
    print("That sucks. Disabling all API Keys")

dncValid = False
dncValidSelect = input("Do you have a doNotCall ApiKey (yes/no)? ").strip()
dncApi = ""
if "yes" in dncValidSelect.lower():
    while not dncValid:
        dncApi = input("Please input your doNotCallApiKey now: ").strip()
        if len(dncApi) == 40:
            print("The length is 40 so most likely a valid key")
            dncValid = True
        else:
            print("That doesn't seem to be the right. Length of "+ len(dncApi))
            temp = input("Is " + dncApi + " correct (yes/no)?")
            dncValid = "yes" in temp.lower()
else:
    print("Oh boy. Disabling the DoNotCall Database")

print("Writting information to file variables.py")
print("You can change the information later on if you would like")
f = open("variables.py", "w")

variableInfo = "rapidApiKey = \"" + rapidApi + "\"\ndncApiKey = \"" + dncApi + "\"\n"
variableInfo2 = 'weatherInfo = {"language" : "english", "lang" : "en", "units": "e", "callback": "test", "mode":"JSON", "types": "link, accurate", "measurement":"imperial", "count": "10"} # Can change measurement to metric")'
f.write(variableInfo)
f.write(variableInfo2)
f.flush()
f.close()
print("A few big ones up next. To setting up the requirements")


