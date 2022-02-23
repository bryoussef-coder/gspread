import gspread

client = gspread.service_account(filename='peerless-sensor-342219-a0f5ef5614b7.json')

sheet = client.open('list1').sheet1
print(sheet.get_all_records())
