import openpyxl

wb = openpyxl.Workbook()

sheet = wb.active
sheet['A1'] = 'Name'
sheet['A2'] = 'Daniil'
sheet['B1'] = 'Surname'
sheet['B2'] = 'Sapunov'
sheet['C1'] = 'age'
sheet['C2'] = '19'

wb.save('workbook.xlsx')
