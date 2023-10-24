import openpyxl

wb = openpyxl.load_workbook('file_10.xlsx')

sheet = wb.active
print(f'{sheet["B2"].value}')
print(f'{sheet["A2"].value}')
print(f'{sheet["C2"].value}')