from openpyxl import Workbook
from openpyxl import load_workbook
import xlrd

# data = load_workbook('C:/Users\Administrator\luoyc\Meizhu\meizhu_testcase.xlsx')
# sheet = data["美住登录"]
# list = []
# for r in range(2, sheet.max_row + 1):
#     list.append(sheet.cell(row=r, column=1).value)
# print(list)


data = xlrd.open_workbook('F:\meizhu_testcase.xlsx')
sheet = data.sheets()[0]
username = sheet.col_values(0)
passwd = sheet.col_values(1)
tip = sheet.col_values(2)
print(username)
