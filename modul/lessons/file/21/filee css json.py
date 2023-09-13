# Завдання 4.
# Припустімо, що у змінній «x» зберігається рядок JSON, який виглядає так.
# x = """{
# "Name": "Jennifer Smith",
# "Contact Number": 7867567898,
# "Email": "jen123@gmail.com",
# "Hobbies":["Reading", "Sketching", "Horse Riding"]
# }"""
# Виконайте parsing і десереалізацію x. Визначте тип x, Надруйте його порядково.
# Добавте до x ще один елемент. Потім виконайте сереалізацію x
# 1. за допомогою dumps та dump у деякий файл json
# 2. за допомогою модуля pickle.
#
#
# import json, pprint
# import pickle
#
# x = """{
# "Name": "Jennifer Smith",
# "Contact Number": 7867567898,
# "Email": "jen123@gmail.com",
# "Hobbies":["Reading", "Sketching", "Horse Riding"]
# }"""
# # Виконайте parsing і десереалізацію x. Визначте тип x, Надруйте його порядково.
# obj = json.loads(x) #із рядка робить json-str -> dict-obj (сералізація)
# # print(obj)
# # print(obj["Hobbies"][0]) #звернення за індексом
# # for k, v in obj.items():
# #     print(f"{k=}, {v=}")
#
# # Добавте до x ще один елемент.
# obj['salary'] = 2000
# # for k, v in obj.items():
# #     print(f"{k=}, {v=}")
#
# # Потім виконайте сереалізацію x
# # 1. за допомогою dumps та dump у деякий файл json
#
# # 1 спосіб
# with open('sample.json', mode='w')as file:
#     json.dump(obj, file, indent=4) #десералізація із dict-obj -> sample.json
#
# # 2 спосіб
# with open('sample2.json', mode='w')as outfile:
#     json_str = json.dumps(obj) #dict-obj -> json-str
#     print(json_str)
#     outfile.write(json_str) #запис в файл
#
# # Потім виконайте сереалізацію x
# # 2. за допомогою модуля pickle.
#
# import pickle
# with open('sample3.pkl', mode='wb') as binfile: #запис у бінарний файл
#     pickle.dump(obj, binfile)
#
#
# # Завдання 6.
# # Задано файл films.json із вмістом
# # { "response": [ { "title": "The Grand Budapest Hotel", "year": 2014, "genre": "comedy" }, { "title": "Inception", "year": 2010, "genre": "thriller" }, { "title": "The Hangover", "year": 2009, "genre": "comedy" }, { "title": "La La Land", "year": 2016, "genre": "musical" }, { "title": "The Social Network", "year": 2010, "genre": "drama" }, { "title": "Interstellar", "year": 2014, "genre": "science fiction"
# # }, { "title": "Django Unchained", "year": 2012, "genre": "western" }, { "title": "The Dark Knight Rises", "year": 2012, "genre": "action" }, { "title": "The Wolf of Wall Street", "year": 2013, "genre": "comedy" }, { "title": "Mad Max: Fury Road", "year": 2015, "genre": "action" } ] }
# # Перетворіть дані у файл CSV.
# # Написати функцію write_json(title, year, gender), що добавляє деякий новий фільм. Зміни відбуваються в обох файлах.
# # Протестувати виконання.
#
# import json, csv
#
# with open("films.json", mode="r") as file:
#     obj = json.load(file)
#
# print(obj)
# films = obj.get('response')
#
# with open('films.csv', mode='w') as csv_file:
#     fieldnamse = list(films[0].keys()) #формуемо шапку
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnamse, lineterminator='\n')
#     print(type(writer))
#
#     writer.writeheader()
#     for film in films:
#         writer.writerow(film)
#
#
# with open('films2.csv', mode='w') as csv_file:
#     fieldnamse = list(films[0].keys()) #формуемо шапку
#     writer = csv.writer(csv_file, lineterminator='\n')
#     writer.writerow(fieldnamse)
#     for film in films:
#         films_values = film.values()
#         print(films_values)
#         writer.writerow(films_values)
#
#
# def add_films_to_csv(title, year, genre):
#     with open('films2.csv', mode='a') as f:
#         csv_writer = csv.writer(f, lineterminator="\n")
#         csv_writer.writerow([title, year, genre])
#
# add_films_to_csv('terminato 4', 2009, 'action')
#
#
#
# import requests
# res = requests.get('https://www.bestprog.net/uk/2020/04/22/python-files-general-concepts-opening-closing-a-file-functions-open-close-ua/')
# print(res.text)
