import sys
import time
import components.Parser as myParser
import components.XlsxReader as myReader
import components.XlsxWriter as myWriter
import os
import webbrowser

input_path = input("Введите путь к файлу, из которого нужно достать ИНН (Пример: C:\\folder\\example.xlsx) >> ")
if os.path.isfile(input_path):
    try:
        input_row_start = int(input("Введите номер первой строки >> "))
        input_row_end = int(input("Введите номер последней строки >> "))
    except:
        print("ERROR: Введены неверные значения строк!")
        input("Нажмите ENTER для завершения")
        sys.exit()
    if input_row_start <= input_row_end:
        output_path = input("Введите путь к файлу (файл создавать не надо) в котором будут сохранены данные (.xlsx не будет работать, используйте .xls) (Пример: C:\\folder\\result.xls) >> ")
        try:
            inn_arr = myReader.read_table(input_path, input_row_start, input_row_end)
        except:
            print("ERROR: Вы неверно указали строки")
            input("Нажмите ENTER для завершения")
            sys.exit()
        company_arr = []
        i = 0
        while i < len(inn_arr):
            time.sleep(0.1)
            if inn_arr[i] == "":
                company_arr.append({
                    'name': '',
                    'inn': '',
                    'index': '',
                    'adress': '',
                    'ur_adress': '',
                    'telephone': '',
                    'email': '',
                    'site': ''
                })
                i += 1
            else:
                try:
                    comp = myParser.get_info(inn_arr[i])
                    if comp is not None:
                        company_arr.append(comp)
                        print("INFO: Удачный парсинг компании (index: " + str(i + 1) + ", ИНН: " + inn_arr[i] + ")")
                        i += 1
                    else:
                        print("INFO: Сохраняю уже полученные данные в файл!...")
                        myWriter.write(company_arr, output_path)
                        print("INFO: Файл '" + output_path + "' записан!")
                        input("Нажмите ENTER для завершения")
                        sys.exit()
                except:
                    print("ERROR: Не удалось получить данные о компании (index: " + str(i + 1) + ", ИНН: " + inn_arr[i] + ")")
                    print("ERROR: Ошибка с доступом к сайту. Пройдите капчу.")
                    webbrowser.open("https://www.list-org.com/bot", new=0)
                    ans = input("Нажмите ENTER для продолжения парсинга или введите 'exit' для завершения >> ")
                    if ans == 'exit':
                        myWriter.write(company_arr, output_path)
                        print("INFO: Файл '" + output_path + "' записан!")
                        input("Нажмите ENTER для завершения")
                        sys.exit()
        myWriter.write(company_arr, output_path)
        print("INFO: Файл '" + output_path + "' записан!")
        input("Нажмите ENTER для завершения")
        sys.exit()
    else:
        print("ERROR: Начальная строка не может быть больше конечной")
        input("Нажмите ENTER для завершения")
        sys.exit()
else:
    print("ERROR: Файла по пути: '" + input_path + "' не существует")
    input("Нажмите ENTER для завершения")
    sys.exit()
