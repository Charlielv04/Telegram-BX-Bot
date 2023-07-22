# Example on how to use the api to connect with google sheets

import gspread

gc = gspread.service_account('./service_account.json')

sh = gc.open("BX-telegram")

print(sh.sheet1.get('A1:B4'))