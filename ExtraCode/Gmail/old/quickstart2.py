from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

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

    for ids in megaThreadList:
        metaMessage = service.users().threads().get(userId='me',id=ids,format="metadata").execute()
        payloads = (metaMessage['messages'][0]['payload'])
        head = payloads['headers']
        for pay in head:
            if(pay['name'] == 'From'):
                temp = pay['value']
                ind = -1
                if "<" in temp:
                    ind = temp.index("<")
#                ind = temp.index("<")
                if (ind < 0):
                    print(temp)
                else:
                    ar.append(temp[ind+1:-1])
#                    print(temp[temp.index("<"):-1])
                break
    
    
    minMessage = service.users().threads().get(userId='me',id="1766fb36b3d82723",format="metadata").execute()
    x = json.dumps(minMessage)
#    print(x)
    print(minMessage['messages'][0]['payload'])
    payloads = (minMessage['messages'][0]['payload'])
    head = payloads['headers']
    for pay in head:
        if(pay['name'] == 'From'):
            print("I FOUND IT")
            ar.append(pay['value'])
            break
    
    # id= 1766fb36b3d82723
    
#    f = open("i.json","w")
#    json.dump(minMessage, f)
    
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
#    print(results)

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

if __name__ == '__main__':
    main()
