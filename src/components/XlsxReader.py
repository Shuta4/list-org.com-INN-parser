import xlrd


def read_table(path, start_row, end_row):
    arr = []
    workbook = xlrd.open_workbook(path, on_demand=True)
    sheet_names = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheet_names[0])
    i = start_row - 1
    while i < end_row:
        arr.append(worksheet.cell(i, 0).value)
        i += 1
    return arr
