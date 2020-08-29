import xbmcaddon
import xbmcgui
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
spreadsheet_id = '' #add your spredsheet ID
spreadsheet_range = '' # add the range
''' 
taken from google sheets api
https://developers.google.com/sheets/api/quickstart/python
'''
def main():
  line_out = ""
  creds = None
  if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
      creds = pickle.load(token)
  with open('/home/osmc/sheets/token.pickle', 'rb') as token:
    creds = pickle.load(token)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file('/home/osmc/sheets/credentials.json', SCOPES)
      creds = flow.run_local_server(port=0)
    with open('/home/osmc/sheets/token.pickle', 'wb') as token:
      pickle.dump(creds, token)
  service = build('sheets', 'v4', credentials=creds)
  sheet = service.spreadsheets()
  result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=SAMPLE_RANGE_NAME).execute()
  values = result.get('values', [])
  if not values:
    print('No data found.')
  else:
    for row in values:
      line_out = line_out + row[0] + '\n'
  xbmcgui.Dialog().ok(addonname, line1)

main()
