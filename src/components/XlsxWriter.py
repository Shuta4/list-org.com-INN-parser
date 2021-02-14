import xlwt


def write(arr, path):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('result')
    worksheet.write(0, 0, "Название")
    worksheet.write(0, 1, "ИНН")
    worksheet.write(0, 2, "Индекс")
    worksheet.write(0, 3, "Адрес")
    worksheet.write(0, 4, "Юридический адрес")
    worksheet.write(0, 5, "Телефон")
    worksheet.write(0, 6, "Email")
    worksheet.write(0, 7, "Сайт")
    for i in range(len(arr)):
        worksheet.write(i + 1, 0, arr[i].get('name'))
        worksheet.write(i + 1, 1, arr[i].get('inn'))
        worksheet.write(i + 1, 2, arr[i].get('index'))
        worksheet.write(i + 1, 3, arr[i].get('adress'))
        worksheet.write(i + 1, 4, arr[i].get('ur_adress'))
        worksheet.write(i + 1, 5, arr[i].get('telephone'))
        worksheet.write(i + 1, 6, arr[i].get('email'))
        worksheet.write(i + 1, 7, arr[i].get('site'))
    workbook.save(path)