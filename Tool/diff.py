from openpyxl import load_workbook


def read_excel(excel_path, sheet_name, col):
    data = load_workbook(excel_path)
    sheet = data[sheet_name]
    newdata = []
    for r in range(2, sheet.max_row + 1):
        if sheet.cell(row=r, column=col).value is None:
            newdata.append("")
        else:
            newdata.append(sheet.cell(row=r, column=col).value)

    return newdata


def aa():
    excel_path = "D:/test.xlsx"
    a = read_excel(excel_path, 'Sheet1', 2)
    b = read_excel(excel_path, 'Sheet1', 3)
    # s1 = set(a)
    # s2 = set(b)
    # s = s1.difference(s2)
    # print(s)
    for x, y in zip(a, b):
        if x != y:
            print(x)


if __name__ == "__main__":
    aa()
