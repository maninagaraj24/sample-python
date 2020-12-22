import csv
import gspread
from datetime import date
from oauth2client.service_account import ServiceAccountCredentials
today = date.today()
D = today.strftime("%d")
print("D =", D)
M = today.strftime("%m")
print("M =", M)
Y = today.strftime("%Y")
print("Y =", Y)
today = str(D + '-' + M + '-' + Y)
t = [(today)]
print (t)
def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('csv-google.json', scope)
client = gspread.authorize(credentials)
spreadsheet = client.open('csv-google')
worksheet = spreadsheet.sheet1
new = next_available_row(worksheet)
nl = 'A' + new
test = []
test.append(t)
with open('nse_stat_evening.csv', 'r') as f:
        read = csv.reader(f)
        for row in read:
                test.append(row)
print (test)
spreadsheet.values_update(
    nl,
    params={ 'valueInputOption': 'USER_ENTERED'
    },
    body={
        'values': test
    }
)
