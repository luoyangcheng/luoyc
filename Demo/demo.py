# 递归函数，比如可以用来计算:1*2*3...*n = ?
from openpyxl import load_workbook
from openpyxl.styles import Font, colors


def read_excel(excel_path, sheet_name, col):
    try:
        data = load_workbook(excel_path)
        sheet = data[sheet_name]
    except Exception as e:
        print('测试用例文件打开错误', e)
    else:
        newdata = []
        for r in range(2, sheet.max_row + 1):
            if sheet.cell(row=r, column=col).value is None:
                newdata.append("")
            else:
                newdata.append(sheet.cell(row=r, column=col).value)
        return newdata


if __name__ == '__main__':
    excel_path = "D:\git\warehouse\TheFame\case\case.xlsx"
    Test_data = []
    for i in range(1, 5):
        one_data = read_excel(excel_path, '美住登陆', i)
        Test_data.append(one_data)
    print(Test_data)
