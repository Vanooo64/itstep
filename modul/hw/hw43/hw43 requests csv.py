# # Домашня робота №43
# # Завдання 1.
# # Використати API і модуль requests для отримання даних у форматі csv за адресою https://support.staffbase.com/hc/en-us/article_attachments/360009197091/email-password-recovery-code.csv
#
# # 1.	Написати функцію, яка приймає https-адресу API і назву сsv-файлу,  записує отримані дані з інтернету у csv-файл із розділювачем
# # комою. Функція повертає успішність чи неуспішність операції. Обробити виключні ситуації, які можуть трапитись.
#
# import requests
# import csv
#
# def add_csv_file(address, name_file):
#     try:
#         responce = requests.get(address) #отримуемо вміст сторінки
#         csv_text = responce.text #робимо з ньго текст
#         csv_lines = (csv_text.strip().split('\n')) # Розділяємо рядок на рядки за символом нового рядка, робимо список
#
#         with open(name_file, mode='w', encoding="utf8", newline='') as file:
#             writer = csv.writer(file, delimiter=',') # Створюємо об'єкт для запису у файл CSV
#
#             # Записуємо кожний рядок у файл
#             for line in csv_lines:
#                 # Розділяємо рядок за символом ';'
#                 row = line.split(';')
#                 # Записуємо рядок у файл
#                 writer.writerow(row)
#         return True
#
#     except requests.exceptions.RequestException as e:
#         print('Помилка під час виконання запиту до API:', str(e))
#         return False
#     except Exception as e:
#         print('Сталася невідома помилка:', str(e))
#         return False
#
# path = 'https://support.staffbase.com/hc/en-us/article_attachments/360009197091/email-password-recovery-code.csv'
# name_file = 'data.csv'
# add_csv_file(path, name_file)

# # 2.	Напишіть функцію change_csv_value(file_path, row_index, column_name, new_value), яка приймає шлях до CSV-файлу `file_path`,
# # індекс рядка `row_index`, назву стовпця `column_name`, і змінює значення у вказаному рядку файла та стовпці на нове значення
# # `new_value`. Виведіть повідомлення, якщо операція пройшла успішно. Обробити виключні ситуації, які можуть трапитись.
#
# import csv
# def change_csv_value(file_path, row_index, column_name, new_value):
#     try:
#         with open(file_path, mode='r') as file:
#             reader = csv.DictReader(file, delimiter=',')
#             rows = list(reader)
#
#         if row_index < 0 or row_index > len(rows):
#             raise IndexError ('Некорекний індекс')
#
#         # Змінюємо значення вказаного стовпця для вказаного рядка
#         rows[row_index - 1][column_name] = new_value
#
#         # Перезаписуємо CSV-файл з оновленими даними
#         with open(file_path, mode='w',  newline='') as file:
#             fieldnames = rows[0].keys()
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(rows)
#
#         print(f'Значення успішно змінено')
#
#     except FileNotFoundError:
#         print('File not found.')
#     except PermissionError:
#         print('Permission denied. Unable to write to the file.')
#     except IndexError as e:
#         print(str(e))
#     except Exception as e:
#         print('An error occurred:', str(e))
#
# change_csv_value('data.csv', 2, 'Identifier', 208000)

# # 3.	Напишіть функцію change_password(email, new_value, file_path),
# # яка змінює у користувача з email одноразовий пароль One-time password у сsv-файлі.
#
# import csv
# def change_password(email, new_value, file_path):
#     updated_data = []
#
#     with open(file_path, mode='r') as file:
#         reader = csv.DictReader(file, delimiter=',')
#
#         for row in reader:
#             if row['Login email'] == email:
#                 row['One-time password'] = new_value
#             updated_data.append(row)
#
#     with open(file_path, mode='w', newline='') as file:
#         fieldnames = updated_data[0].keys()
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(updated_data)
#
# change_password('rachel@example.com', 111111, 'data.csv')

# # 4.	Напишіть функцію `del_user(email, file_path)`, що видаляє користувача за даним email із csv-файла.
# # Передбачити всі можливі ситуації.
#
# import csv
# def del_user(email, file_path):
#     updated_data = []
#
#     with open(file_path, mode='r') as file:
#         reader = csv.DictReader(file, delimiter=',')
#         print(reader)
#         for row in reader:
#             if row['Login email'] != email:
#                 updated_data.append(row)
#
#         fieldnames = ['Login email', 'Identifier', 'One-time password', 'Recovery code', 'First name', 'Last name',
#                       'Department', 'Location']
#
#         with open(file_path, mode='w', newline='') as file:
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(updated_data)
#
# del_user('rachel@example.com', 'data.csv')

# # Проект 2 "Система реєстрації та аутентифікації користувачів зі збереженням даних у файлі"
# #
# # Проект передбачає створення системи реєстрації, входу та зміни облікових даних користувачів та збереження цих даних у текстовому файлі, наприклад у json або сsv.
# # Програма має надавати можливість користувачам за пунктами меню створювати нові облікові записи (процес реєстрації), входити у систему зі своїми обліковими даними (процес аутентифікації) та змінювати особисті відомості.
# #
# # Основні функції проекту можуть включати:
# # · Реєстрація нового користувача з введенням необхідних облікових даних, таких як ім'я, електронна пошта та пароль. Перевірка унікальності електронної пошти при реєстрації. Збереження облікових даних користувачів в текстовому файлі (наприклад, в форматі CSV чи JSON).
# # · Аутентифікація (вхід) користувача з перевіркою введених облікових даних (електронна пошта та пароль). Якщо введені користувачем почта і пароль є у файлі і співпадають, то вхід успішний.
# # · Можливість зміни облікових даних користувача, таких як зміна паролю, електронної пошти.
# # · Видалення свого облікового запису.
#

import csv
import os

print('             Вас вітає система реєстрації та аутентифікації користувачів')
print()
print('''1. Реєстрація нового користувача з введенням необхідних облікових даних, таких як ім'я, електронна пошта та пароль.
2. Аутентифікація (вхід) користувача з перевіркою введених облікових даних (електронна пошта та пароль).
3. Можливість зміни облікових даних користувача, таких як зміна паролю, електронної пошти.
4. Видалення свого облікового запису.''')
print()
choice = int(input('Введіть пункт меню який Вас цікавить: '))
def checking_email(email, path): #функція для перевірки присутності email у csv файлі
    with open(path, mode='r') as file:
        reader = csv.DictReader(file)
        list_data = list(reader)

        for row in list_data:
            if row["Email"] == email:
                return False
    return True

def add_user(path, name, email, password): # функція додає нового користувача
    add_data = [name, email, password]

    with open(path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(add_data)

if choice == 1:
    email = input('Введіть email: ')
    while not checking_email(email, 'authentication_data.csv'):
        print('Користувач вже зарєстрованний, введіть унікальний email')
        email = input('Введіть email: ')

    name = input('Введіть імя користувача латинськими буквами: ')
    password = input('Введіть пароль: ')

    add_user("authentication_data.csv", name, email, password)
    print('Користувача було зарєстрованно у системі')


# Аутентифікація (вхід) користувача з перевіркою введених облікових даних (електронна
# пошта та пароль). Якщо введені користувачем почта і пароль є у файлі і співпадають, то вхід успішний.

def authentication(path, email, password): #функція для перевірки присутності email у csv файлі
    with open(path, mode='r') as file:
        reader = csv.DictReader(file)
        list_data = list(reader)

        for row in list_data:
            if row["Email"] == email and row["Password"] == password:
                return True
        return False

if choice == 2:
    email = input('Введіть email: ')
    password = input('Введіть пароль: ')

    if authentication("authentication_data.csv", email, password):
        print('Ви успішно автеризувались у системі')
    else:
        print('Електронна пошта або пароль не некоректні!')

# Можливість зміни облікових даних користувача, таких як зміна паролю, електронної пошти.

def modify_user_data(path, old_email, new_email, new_password):
    modified = False
    new_data = []
    with open(path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        for row in reader:
            # Перевірте, чи збігається електронна адреса
            if row['Email'] == old_email:
                row['Email'] = new_email
                row['Password'] = new_password
                modified = True
            new_data.append(row)
    # Якщо дані були змінені, файл  перезаписуется
    if modified:
        with open(path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(new_data)
        return True
    else:
        return False

if choice == 3:
    old_email = input('Введіть email для якого хочете змынити пароль: ')
    new_email = input('Введіть новий email: ')
    new_password = input('Введіть новий пароль: ')


    if modify_user_data("authentication_data.csv", old_email, new_email, new_password):
        print("Дані користувача успішно змінено.")
    else:
        print("Користувача з цією електронною адресою не знайдено, або дані неправильні.")

# Видалення свого облікового запису.

def delet_user(path, email): # функція додає нового користувача
    add_data = [name, email]

    with open(path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(add_data)

if choice == 4:
    def delete_user(path, email):
        # Перевіряємо, чи існує файл з вказаним шляхом
        if not os.path.exists(path):
            print("Файл не знайдено.")
            return

        # Створюємо тимчасовий файл для збереження оновлених даних
        temp_file = "temp.csv"
        try:
            # Відкриваємо вихідний CSV-файл для читання та створюємо тимчасовий CSV-файл для запису
            with open(path, mode='r', newline='') as file_read, open(temp_file, mode='w', newline='') as temp_write:
                reader = csv.DictReader(file_read)
                fieldnames = reader.fieldnames

                # Записуємо дані в тимчасовий файл, крім видаленого запису
                writer = csv.DictWriter(temp_write, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    if row['Email'] != email:
                        writer.writerow(row)

            # Переміщуємо тимчасовий файл на місце вихідного файлу
            os.replace(temp_file, path)
            print("Користувача успішно видалено.")
        except Exception as e:
            print("Помилка під час видалення користувача:", str(e))
            # Видаляємо тимчасовий файл у разі помилки
            os.remove(temp_file)

    # Викликаємо функцію для видалення користувача за його електронною поштою
    if choice == 4:
        email_to_delete = input("Введіть email для видалення користувача: ")
        delete_user("authentication_data.csv", email_to_delete)

