from openpyxl import load_workbook


class Excel:
    def read_excel(excel_path, sheet_name, col):
        data = load_workbook(excel_path)
        sheet = data[sheet_name]
        username = []
        for r in range(2, sheet.max_row + 1):
            if sheet.cell(row=r, column=col).value is None:
                username.append("")
            else:
                username.append(sheet.cell(row=r, column=col).value)
        print(username)
        return username


if __name__ == "__main__":
    Excel.read_excel('E:/luoyc\Meizhu\meizhu_testcase.xlsx', '美住登录', 1)
