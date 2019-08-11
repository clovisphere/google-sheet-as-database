"""This sample app demonstrates how to use Google sheet
as a database. It's very basic.. the whole point is to show that
you don't always need a fully fledged database like sqlite, MysQL, etc.
"""

import gspread
import pprint
from oauth2client.service_account import ServiceAccountCredentials

# define scope, and authorize client
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)

# open/read @google sheet
sheet = client.open('Programming Books').sheet1
# retrieve all records
records = sheet.get_all_records()
# some pretty print magic
pp = pprint.PrettyPrinter(indent=4, compact=True)
pp.pprint(records)
