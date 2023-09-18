# #                                 Домашня робота №42 Робота з файлами~. CSV. JSON.
# #
# # Завдання 1.
# # Використати API і модуль requests для отримання даних у форматі json response = requests.get("https://jsonplaceholder.typicode.com/todos")
# # json_text = response.text
# # 1.	Виконайте десереалізацію даних із json_text. Знайти користувача, що найбільше виконав завдань.
#
# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# json_text = response.text
# data = json.loads(json_text)
#
# new_list = [] # створюэмо список з юзерів, які виконали завданя.
# for item in data:
#     if item['completed']:
#         new_list.append(item)
#
#
# user_counts = {}  # Створюємо словник для збереження кількості для кожного userId
# for item in new_list:
#     user_id = item['userId']
#     if user_id in user_counts:
#         user_counts[user_id] += 1
#     else:
#         user_counts[user_id] = 1
#
# max_count = max(user_counts.values()) # Знаходимо максимальну кількість
# users_with_max_count = [user_id for user_id, count in user_counts.items() if count == max_count] # Знаходимо всіх користувачів, які мають максимальну кількість
#
# print("Користувач(і) з найбільшою кількістю:")
# for user_id in users_with_max_count:
#     print(f"Користувач з ID {user_id}, кількість: {max_count}")
#
#
# # 2.	Виконайте сереалізацію даних із невиконаними завданнями у новий файл data.json.
# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# json_text = response.text
# data = json.loads(json_text)
#
# new_lst = []
# for item in data:
#     if item["completed"] == False:
#         new_lst.append(item)
#
# with open('data.json', mode='w') as file:
#     json_data = json.dump(new_lst, file, indent=4)
#
# # 3.	Виконайте десереалізацію даних із файла data.json. Відсортуйте тільки ті, в яких id > 100, а результат
# # cереалізуйте у деякий рядок і виведіть його.
# import json
#
# with open('data.json', mode='r') as file:
#     loaded_data = json.load(file)
#
#     new_list = []
#     for row in loaded_data:
#         if row['id'] > 100:
#             new_list.append(row)
#
#     json_data = json.dumps(new_list, indent=4)
#
# print(json_data)
#
# # Завдання 2.
# # 1.	Перетворіть дані, отримані із API у завданні 1 у файл формату CSV.
#
# import requests
# import csv
#
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# data = response.json()
#
# with open('data.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['userId', 'id', 'title', 'completed'])
#     for item in data:
#         writer.writerow([item['userId'], item['id'], item['title'], item['completed']])
#
# # # 2.	Написати функцію  write_to_csv(userId, id,  title, completed=False), що добавляє новий запис до csv-файлу. Протестувати виконання.
#
# import csv
# def write_to_csv(userId, id,  title, completed=False):
#     new_record = {
#         "userId": userId,
#         "id": id,
#         "title": title,
#         "completed": completed
#     }
#
#     with open('data.csv', mode='a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([new_record["userId"], new_record["id"], new_record["title"], new_record["completed"]])
#
#     print('новий запис додано до csv-файлу!')
#
# write_to_csv(11,201, "Це новий запис", True)

















