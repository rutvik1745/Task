import xlsxwriter

Workbook = xlsxwriter.Workbook('Example2.xlsx')
worksheet = Workbook.add_worksheet()

row = 0
column = 0

content = ["Parker","Smith","Jhon"]

for item in content:
    worksheet.write(row,column,item)

    row +=1
Workbook.close()