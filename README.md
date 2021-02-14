# Парсер данных с сайта list-org.com
Версия программы и README от 08.12.2019

## Как работать с программой

### Запуск

* Запускаем программу через консоль
* Вводим путь и название файла (расширение .xlsx, .xls) из которого будем парсить (Пример: C:\testFolder\example.xlsx)
* Вводим номер строки с которой начнем парсинг
* Вводим номер последней строки, которую нужно парсить
* Вводим путь и название файла в который будет сохранена информация (расширение ТОЛЬКО .xls). Файл создавать не надо! Путь до файла должен быть доступен (не стоит использовать защищенные директории)! (Пример: C:\testFolder\resultsExample.xls)
* После этого начнется парсинг

### Ошибки

В процессе парсинга будет происходить ошибка: "Не удалось получить данные о компании."
Эта ошибка откроет страницу "list-org.com/bot". На этой странице вам нужно будет ввести капчу. Введите капчу и нажмите в программе ENTER
Если эта страница не открылась автоматически - попробуйте открыть ее в браузере вручную.
Если эта страница не загружается, то проблема или с сервером list-org.com, или с подключением компьютера к интернету.
В этом случае вам нужно ввести "exit" и нажать ENTER. Программа сохранит уже полученные данные в файл.

### Вопросы

В: Что это за пустые строки в выходном файле?
О: В исходном файле с ИНН на этих строках был указан не верный или не был указан ИНН.


В: Почему нельзя использовать расширение выходного файла .xlsx?
О: Используемая в данной программе библиотека для записи данных в таблицу Excel некорректно работает с форматом .xlsx.


В: Почему выводится капча?
О: Сайт каждые 70-120 запросов выдает капчу. Эта капча мешает получению данных. На поиск информации об одной компании нужно 2 запроса.
