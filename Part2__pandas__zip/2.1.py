import xlrd3

wb = xlrd3.open_workbook('tab.xlsx')

sheet_names = wb.sheet_names()


sh = wb.sheet_by_name(sheet_names[0])
nmin = sh.row_values(6)[2]
for rownum in range(7, 27):
    temp = sh.row_values(rownum)
    nmin = min(nmin, temp[2])
print(nmin)