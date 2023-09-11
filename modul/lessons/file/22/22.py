# Завдання 1.
# Заданий рядок
#
# 1. Запишіть вмістиме json_str у json-файл
# import json, csv
#
# import json
# json_str= """[
#  {
#   "Employee ID": 1,
#   "Name": "Abhishek",
#   "Designation": "Software Engineer"
#  },
#  {
#   "Employee ID": 2,
#   "Name": "Garima",
#   "Designation": "Email Marketing Specialist"
#  }
# ]"""
#
# 1 спосіб
try: # функція яка перевіряе  json файл на коректність
    json.loads(json_str)
except json.JSONDecodeError as a:
    print('Incorect json-str')
else:
    try:
        with open('sample1.json', mode='w') as file:
            file.write(json_str)
    except FileExistsError:
        print('File exists')

#
# # 2 спосіб
# with open('sample2.json', mode='w') as file:
#
#     try: # функція яка перевіряе  json файл на коректність
#         lst = json.loads(json_str)
#         json.dump(lst, file, indent=4)
#
#     except json.JSONDecodeError as a:
#         print('Incorect json-str')
#
# # 2. Завантажте отриманий json-файл та перетворіть дані у файл CSV.
# with open('sample2.json', mode='r') as json_f, open('sample.csv', mode='w') as csv_f:
#     lst = json.load(json_f) #отримаемо список
#     print(lst)
#     writer = csv.DictWriter(csv_f, fieldnames=lst[0].keys(), lineterminator='\n') # список словників - DictWriter список списків - writer
#     writer.writeheader()
#     for item in lst:
#         writer.writerow(item)
#
# # Завдання 2.
# # За допомогою модуля request за посиланням
# # “https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/people/people-100.csv”
# # отримати дані та записати їх у csv-файл.
#
#
# import requests
# path = "https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/people/people-100.csv"
# res = requests.get(path)
# text = res.text
# # print(res) #<Response [200]> - відповідь прийшла успішно
# with open('temp/data.scv', mode='w', newline='') as file:
#     file.write(text)
#
# # Напишіть функцію change_csv_value(file_path, row_index, column, new_value), яка приймає шлях до CSV-файлу `file_path`, індекс рядка `row_index`, `column` може приймати номер стовпця або ім’я стовпця, і змінює значення у вказаному рядку та стовпці на нове значення  `new_value`.
# # Напишіть функцію функція `delete_csv_row`, що приймає шлях до CSV-файлу `file_path` та індекс рядка `row_index`, який потрібно видалити.
# def change_csv_value(file_path, row_index, column, new_value):
#     with open(file_path, mode="r+", newline='') as file:
#         csv_file = csv.reader(file) #зчитуемо файл
#         list_data = list(csv_file) #перетворюемо у список
#         list_data[row_index][column] = new_value #достукуемось до значення і замінюемо його
#         # print(list_data[row_index][column])
#
#         file.seek(0) # переводимо курсор в початок файлу
#         csv_writer = csv.writer(file) #визначаемо що треба записати ((dictwraiter - дз))
#         csv_writer.writerows(list_data) #записуемо у файл
#
#
# change_csv_value("temp/data.scv", row_index=2, column=2, new_value='Moris')

# Завдання 3.
# 1. Імпортувати модуль os: `import os`
# 2. Вивести поточну робочу директорію: `print(os.getcwd())`
# 3. Змінити поточну робочу директорію на певну директорію: `os.chdir("шлях_до_директорії")`
# 4. Отримати список файлів та папок в поточній директорії: `print(os.listdir())`
# 5. Створити нову директорію: `os.mkdir("назва_директорії")`
# 6. Створити декілька вкладених директорій: `os.makedirs("шлях/до/директорій")`
# 7. Перейменувати файл або директорію: `os.rename("початкове_ім'я", "нове_ім'я")`
# 8. Видалити файл: `os.remove("назва_файлу")`
# 9. Видалити порожню директорію: `os.rmdir("назва_директорії")`
# 10. Видалити директорію та всі її вміст: `os.rmtree("назва_директорії")`
# 11. Перевірити, чи існує файл або директорія: `os.path.exists("шлях_або_назва_файлу_директорії")`
# 12. Отримати абсолютний шлях до файлу або директорії: `print(os.path.abspath("назва_файлу_директорії"))`
# 13. Розділити шлях та назву файлу або директорії: `print(os.path.split("шлях_або_назва_файлу_директорії"))`
# 14. Визначити розширення файлу з його назви: `print(os.path.splitext("назва_файлу"))`
# 15. Перевірити, чи є об'єкт файлом: `os.path.isfile("шлях_або_назва_файлу_директорії")`
# 16. Перевірити, чи є об'єкт директорією: `os.path.isdir("шлях_або_назва_файлу_директорії")`
# 17. Отримати інформацію про файл (наприклад, розмір, дата створення): `print(os.stat("назва_файлу").st_size, os.stat("назва_файлу").st_mtime)`


# import os
# # dir_list = os.scandir(".")
# # print(*dir_list)
# #
# # for item in dir_list:
# #     print(item.name, item.path, item.stat())
#
# for root, dirs, file in os.walk("."): # "." - поточна директорія
#     print(root, dirs, file)










