from openpyxl import load_workbook

data = load_workbook('C:\demo.xlsx')
sheet = data['demo']
print(sheet.cell(row=1, column=1).value)
sheet.cell(2, 2, '写入哈哈')
data.save('C:\demo.xlsx')
