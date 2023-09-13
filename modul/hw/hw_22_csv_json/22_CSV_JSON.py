# #                               РОБОТА З ФАЙЛАМИ.CSV.JSON.ЗАНЯТТЯ №41
#
# # Завдання 1.
# # Припустімо, що у змінній «strng» зберігається рядок JSON, який виглядає так.
# #
# # strng = """{
# #     "emp1": {
# #         "name": "Lisa",
# #         "designation": "programmer",
# #         "age": 34,
# #         "salary": 54000
# #     },
# #     "emp2": {
# #         "name": "Elis",
# #         "designation": "Trainee",
# #         "age": 24,
# #         "salary": 40000
# #     }
# # }"""
# #
# # Виконайте parsing і десереалізацію із рядка strng.
# # Визначте тип отриманого об’єкту, роздрукуйте його порядково.
# # Добавте до об’єкту ще один якісь елемент. Потім виконайте сереалізацію отриманого словника-об’єкту:
# # 1.	за допомогою dump у файл json
# # 2.	за допомогою модуля pickle у бінарний файл.
# # Протестуйте/виконайте десереалізацію об’єктів із json-фaйла та із бінарного файла відповідно. Перевірте чи вони рівні (==, is)
# import json
# import pickle
#
# strng = """{
#     "emp1": {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": 34,
#         "salary": 54000
#     },
#     "emp2": {
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": 24,
#         "salary": 40000
#     }
# }"""
#
# # Виконайте parsing і десереалізацію із рядка strng.
# data = json.loads(strng)
#
#
# # Визначте тип отриманого об’єкту
# print(f"Тип отриманого об’єкту {type(data)}")
#
# # роздрукуйте об’єкт порядково
# for employee_id, employee_data in data.items():
#     print(f"Дані для співробітника {employee_id}:")
#     for key, value in employee_data.items():
#         print(f"{key}: {value}")
#     print()
#
# # Добавте до об’єкту ще один якісь елемент.
# data['emp3'] = {
#     'name': 'John',
#     'designation': 'Manager',
#     'age': 40,
#     'salary': 60000
# }
#
# # Потім виконайте сереалізацію отриманого словника-об’єкту:
# # 1.	за допомогою dump у файл json
#
# with open('dump_json.json', mode="w") as dump_json_file:
#     json.dump(data, dump_json_file, indent=4)
#
# # 2.	за допомогою модуля pickle бінарний файл.
#
# with open('dict_picle.pkl', mode="wb") as picle_file:
#     pickle.dump(data, picle_file)
#
# # Протестуйте/виконайте десереалізацію об’єктів із json-фaйла та із бінарного файла відповідно. Перевірте чи вони рівні (==, is)
# with open("dump_json.json", mode='r') as deceraliz_json:
#     json_data = json.load(deceraliz_json)
#
# with open("dict_picle.pkl", mode="rb") as deceraliz_pkl:
#     pickle_data = pickle.load(deceraliz_pkl)
#
# if json_data == pickle_data:
#     print("JSON і бінарний файл містять однакові дані (за допомогою ==).")
# else:
#     print("JSON і бінарний файл містять різні дані (за допомогою ==).")
#
# if json_data is pickle_data:
#     print("JSON і бінарний файл містять один і той же об'єкт (за допомогою is).")
# else:
#     print("JSON і бінарний файл містять різні об'єкти (за допомогою is).")
#
# # Завдання 2.
# # Реалізуйте функцію validate_json, яка спробує перевірити, чи є рядок у форматі JSON коректним.
# # Якщо рядок має правильний формат JSON, то виводиться повідомлення "Valid JSON". Якщо ж дані не
# # мають коректного формату, виведеться повідомлення "Invalid JSON" разом з описом помилки. Протестувати функцію.
#
# import json
# def validate_json(json_str):
#     try:  # функція яка перевіряе  json файл на коректність
#         json.loads(json_str)
#         print("Valid JSON")
#     except json.JSONDecodeError as a:
#         print(f'Incorect json-str: {a}')
#
# valid_json_str = '{"name": "John", "age": 30, "city": "New York"}'
# invalid_json_str = '{"name": "John", "age": 30, "city": "New York"'
#
# validate_json(valid_json_str)  # Результат: Valid JSON
# validate_json(invalid_json_str)  # Результат: Invalid JSON: Expecting property name enclosed in double quotes: line 1 column 34 (char 33)
#
# # Завдання 3.
# # Задайте вручну табличні дані у деякий файл формату csv. Напишіть функцію convert_csv_to_json, яка
# # приймає назву csv-файла, і з нього програмно створює відповідний json-файл наступного вигляду і повертає
# # повідомлення про успішність чи неуспішність операції.
# import csv, json
#
# def convert_csv_to_json(name_file_csv):
#     try:
#         with open(name_file_csv, mode="r", encoding="utf-8") as csv_file:
#             data = csv.DictReader(csv_file)
#             data_dict = {int(data['No']): {'Company': data['Company'], 'Car Model': data['Car Model']} for data in data}
#
#
#             with open('new_json.json', mode='w', encoding='utf-8') as json_file:
#                 json.dump(data_dict, json_file, indent=4)
#                 return f'Данні з файлу "{csv_file.name}" були записані у json-файл під назвою "{json_file.name}"'
#     except Exception as e:
#         return f"Помилка: {str(e)}"
#
# res = convert_csv_to_json('data.csv')
# print(res)
#
#
#
#
