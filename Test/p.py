from selenium import webdriver
from Meizhu._def import waitid,waitxp
from openpyxl import Workbook
from openpyxl import load_workbook
import time
import xlrd
import xlwt

import xlwt
# f = xlwt.Workbook()
# sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
data=load_workbook('F:/text.xlsx')
sheet=data["Sheet1"]
# l_=[2,3,4,5,6]
rows=sheet.max_row
l_=[]
for i in range(2,rows+1):
    l_.append(i)
print(l_)


a=["k","d","d","s","q"]
for i,j in zip(l_,a):
    sheet.cell(i,3,j)
data.save('F:/text.xlsx')



