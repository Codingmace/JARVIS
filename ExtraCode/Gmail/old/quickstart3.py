from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
from tld import get_tld


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def cleanUrl(url):
#    from tld import get_tld
    newUrl = url.strip()
    
    if not("mailto" in url): # It is email back
#        res = get_tld(url, as_object=True) #Get the root as an object
#        return (res.tld)
        #print("Send them back an email about unsubscribing. Could do this one later")
        return newUrl
    else: # It is an actual URL that needs to be cleaned up
        url = newUrl
        newUrl = url.replace("<","").replace(">","")
        return newUrl

def cleanDomain(url):
    newUrl = url.strip().replace("<","").replace("<","")
    startInd = 0
    if ("mailto" in newUrl):
        startInd = newUrl.index(":") # MAYBE +1
        if ("?" in newUrl): # Has a subject line too
            endInd = newUrl.index("?") 
            return newUrl[startInd:endInd]
        return newUrl[startInd:] # Maybe
    elif ("https" in newUrl):
        newUrl = newUrl.replace("https://","")
        startInd = newUrl.index("/")
        return "https://" + (newUrl[0:startInd])
    elif ("http" in newUrl):
        newUrl = newUrl.replace("http://","")
        startInd = newUrl.index("/")
        return "http://" + (newUrl[0:startInd])
        

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    megaThreadList = []
    ar = []
    unsub = []
    y = open("file2.txt","w")
    x = open("file.txt","w")
    z = open("file3.txt","w")
    moreThreads = True
    threadsList = service.users().threads().list(userId='me',includeSpamTrash=False,prettyPrint=True).execute()
    nextPageToken = threadsList['nextPageToken']
    for thread1 in threadsList['threads']:
        megaThreadList.append(thread1['id'])
        
    while moreThreads:
        threadsList = service.users().threads().list(userId='me',includeSpamTrash=False,prettyPrint=True,pageToken=nextPageToken).execute()
        for thread1 in threadsList['threads']:
            megaThreadList.append(thread1['id'])
        if 'nextPageToken' in threadsList:
            nextPageToken = threadsList['nextPageToken']
            print(nextPageToken)
        else:
            moreThreads = False
#        moreThreads = False

    for ids in megaThreadList:
        metaMessage = service.users().threads().get(userId='me',id=ids,format="metadata").execute()
        fullMessage = service.users().threads().get(userId='me',id=ids,format="full").execute()
#        print(metaMessage)
#        s = input()
        payloads = (metaMessage['messages'][0]['payload'])
        head = payloads['headers']
        # Name = List-Unsubscribe
        curEmail = ""
        for pay in head:
            if(pay['name'] == 'From'):
                temp = pay['value']
                ind = -1
                if "<" in temp:
                    ind = temp.index("<")
#                ind = temp.index("<")
                if (ind < 0):
                    #print(temp)
                    curEmail = temp
                else:
                    curEmail = temp[ind+1:-1]
                    ar.append(curEmail)
                    y.write(curEmail + "\n")
#                    print(temp[temp.index("<"):-1])
            if(pay['name'] == 'List-Unsubscribe'):
                temp = pay['value']
                ind = temp.index("<")
                curLink = temp[ind+1:-1]
                x.write(curLink + "\n")
                unsub.append(curLink)
              #  if("," in temp):
              #      print("True")

    subscribeList = []
    for a in unsub:
        if "," in a:
            split = a.split(",")
            #print(cleanUrl(split[0]))
            #print(cleanUrl(split[1]))
            cleanDom = cleanDomain(split[1])
            if not (cleanDom in subscribeList):
                subscribeList.append(cleanDom)
        else:
            #print(cleanUrl(a))
            cleanDom = cleanDomain(a)
            if not (cleanDom in subscribeList):
                subscribeList.append(cleanDom)

    x.close()
    y.close()
    for b in subscribeList:
        print(b)
        z.write(b + "\n")
    z.close()

    
if __name__ == '__main__':
    main()
