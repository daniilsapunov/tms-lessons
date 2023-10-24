import openpyxl

wb = openpyxl.Workbook()

sheet = wb.active
sheet['A1'] = 'Name'
sheet['A2'] = input()
sheet['B1'] = 'Surname'
sheet['B2'] = input()
sheet['C1'] = 'age'
sheet['C2'] = input()

wb.save('file_10.xlsx')
