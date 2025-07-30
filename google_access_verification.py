import gspread
from oauth2client.service_account import ServiceAccountCredentials

# specify name of your specific google sheet
google_sheet_name = "Cell Tracker v3 Sandbox"

# authorize 
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# verify

sheet = client.open(google_sheet_name)
print(f"{google_sheet_name} has been found.")

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# authorize

gauth = GoogleAuth()
gauth.credentials = creds
drive = GoogleDrive(gauth)

# create folder variables and input your specific folder IDs

raw_data_folder_ID = "folder ID goes here"
combined_data_folder_ID = "folder ID goes here"
figures_folder_ID = "folder ID goes here"

# list files found in the folders

print("Files found:")
file_list = drive.ListFile({'q' : f"'{raw_data_folder_ID}' in parents and trashed=false"}).GetList()
for file in file_list:
    print(f"- {file['title']} ({file['id']})")