# # task1
# data = {
#     193: {"name": "John", "age": 30, "skills": {"python": 8, "js": 7}},
#     209: {"name": "Bill", "age": 15, "skills": {"python": 6}},
#     746: {"name": "Jane", "age": 58, "skills": {"js": 2, "python": 5}},
#     109: {"name": "Jill", "age": 83, "skills": {"java": 10}},
#     984: {"name": "Jack", "age": 28, "skills": {"c": 8, "assembly": 7}},
#     765: {"name": "Penelope", "age": 76, "skills": {"python": 8, "go": 5}},
#     598: {"name": "Sylvia", "age": 62, "skills": {"bash": 8, "java": 7}},
#     483: {"name": "Anna", "age": 24, "skills": {"js": 10}},
#     277: {"name": "Beatriz", "age": 26, "skills": {"python": 2, "js": 4}},
# }
#
# # # 1.	Відфільтруйте і виведіть елементи словника тільки з віком більше за 30.
# lst_age = []
# for key, value in data.items():
#     age = value['age']
#     if age >= 30:
#         lst_age.append(age)
# print(lst_age)
#
# # # ааналогічно генератором списку
# # gag_30 = [value['age'] for key, value in data.items() if value['age']>= 30 ]
# # print(gag_30)
#
# # 2.	Знайти імена людей та їх id, які мають навички skills по Python.
# id_name = {}
# for key, value in data.items():
#     skills = value['skills']
#     if 'python' in skills:
#         id_name[key] = value['name']
# print(id_name)
#
# # # ааналогічно генератором списку
# # dict_skills_python = {key: value['name'] for key,value in data.items() if 'python' in value['skills']}
# # print(dict_skills_python)
#
# # 3.	Знайти імена людей, які мають навички skills по Python із оцінкою більше 5, та вивести їх середній вік.
#
# name_skills = {}
# for value in data.values():
#     python_skills = value.get('skills', {}).get('python')
#     if python_skills is not None and python_skills>5:
#         name_skills[value['name']] = python_skills
#
# names = ', '.join(name_skills.keys())
# print(f'Імена людей, які мають навички skills по Python із оцінкою більше 5 - {names}')
# print(f'Їх cередній вік {sum(name_skills.values())/len(name_skills.values()):.2f}')

# task2
# Відомісті про країни задані за допомогою словника
#
#
# 1.	Змінити заданий  словник на словник, що містить числовий тип даних щодо населення і площі.
# 2.	Надрукувати «порядково» назву країни, її континент, щільність населення та площу.
# 3.	Знайти загальну кількість населення.
# 4.	Знайти країну із мінімальною кількістю населення.
# 5.	Знайти кількість населення, яке проживає тільки у Азії.
# 6.	Вивести  у вигляді таблиці інформацію тільки про країни та їх площі, які знаходяться у  Європі.
# 7.	Знайти країну із мінімальною площею.

# world={
# 'Germany': {'cw': 'Europe', 'ns': '154864', 'sq': '13189 KM^2'},
# 'Ukraine':{'cw': 'Europe','ns': '467591','sq':'6248 KM^2'},
# 'Egypt':{'cw': 'Africa', 'ns': '7891416','sq':'1488228 KM^2'},
# 'Nigeria':{'cw': 'Africa','ns': '77804','sq':'99648 KM^2'},
# 'China':{'cw': 'Asia','ns': '987654321','sq':'9137462 KM^2'},
# 'USA':{'cw': 'North America','ns':'193764825','sq':'1230540 KM^2'},
# 'Brazil':{'cw': 'South America','ns':'123456789','sq':'894484 KM^2'},
# 'Canada':{'cw': 'North America', 'ns': '456852','sq':'69874 KM^2'},
# 'India':{'cw': 'Asia','ns': '87864','sq':'987697 KM^2'},
# 'Finland':{'cw': 'Europe','ns': '28613','sq':'81468 KM^2'}
# }
#
# # 1. Змінити заданий словник на словник, що містить числовий тип даних щодо населення і площі.
# update_world = {}
# for key, value in world.items():
#     update_world[key] = {
#         'cw': value['cw'],
#         'ns': int(value['ns']),
#         'sq': int(value['sq'].split()[0])
#     }
#
# # 2. Надрукувати «порядково» назву країни, її континент, щільність населення та площу.
# for key, value in world.items():
#     print(f'Назву країни - {key}, її континент "{value["cw"]}", щільність населення - {value["ns"]} та площа - {value["sq"]}')
#
# # 3. Знайти загальну кількість населення.
# people = [value['sq'] for value in update_world.values()]
# print(f'Загальна кількість населення = {sum(people)}')
#
# # 4. Знайти країну із мінімальною кількістю населення.
# lst_pe = {key: value['ns'] for key, value in update_world.items()}
# print(f'Країну із мінімальною кількістю населення {key} - {min(lst_pe.values())}')
#
# # 5. Знайти кількість населення, яке проживає тільки у Азії.
# lst_asia = []
# for key, value in update_world.items():
#     if value['cw'] == 'Asia':
#         lst_asia.append(value['ns'])
# print(f'Кількість населення, яке проживає тільки у Азії = {sum(lst_asia)}')
#
# # 6.	Вивести  у вигляді таблиці інформацію тільки про країни та їх площі, які знаходяться у  Європі.
# europe_country = {key: value['sq'] for key, value in update_world.items() if value['cw'] == 'Europe'}
# print('-' * 20)
# print(f'{"Країна":^10s}|{"Площа":^10s}')
# print('-' * 20)
# for country, area in europe_country.items():
#     print(f'{country:^10s}|{area:^10d}', )
#     print('-' * 20)
#
# # 7.	Знайти країну із мінімальною площею.
# country_area = {key: value['sq'] for key, value in update_world.items()}
# print(f'Країну із мінімальною площею {key} = {min(country_area.values())}')

# # Завдання 3
# # Створіть cловник, який зберігає інформацію про працівників: ПІБ, телефон, email, назва посади, номер кабінету.Подумайте
# # та оберіть ключ для працівника, за яким можна отримати його дані.Реалізуйте у вигляді меню можливість додавати, видаляти, знаходити
# # працівника за ключем, змінювати його дані, а також виводити інформацію про всіх працівників у вигляді форматованої таблиці.
#
# workers = {1: {'ПІБ': 'Савченко Іван Дмитрович', 'email': 'glazglojon@gmail.com', 'Телефон': 380663737524,
#                'Назва посади': 'Python розробник', 'Номер кабінету': 7},
#            2: {'ПІБ': 'Мадамінова Людмила Маратівна', 'email': 'madamina@gmail.com', 'Телефон': 380935986691,
#                'Назва посади': 'Java розробник', 'Номер кабінету': 47},
#            3: {'ПІБ': 'Небесна Єва Іванівна', 'email': 'nebo1@gmail.com', 'Телефон': 380675748352,
#                'Назва посади': 'Frontend розробник', 'Номер кабінету': 14}
#            }
# def add_worker(): #одавання нового працівника
#     fio = input('Введіть ПІБ:')
#     email = input('Введіть email:')
#     phone = int(input('Введіть телефон:'))
#     position = input('Введіть назву посади:')
#     office = int(input('Введіть номер кабінет:'))
#
#     max_key = max(workers.keys())
#     new_worker_id = max_key+1
#     new_worker_data = {
#         'ПІБ': fio,
#         'email': email,
#         'телефон': phone,
#         'назва посади': position,
#         'номер кабінет': office
#     }
#     workers[new_worker_id] = new_worker_data
#
# def del_worker(worker_id): #видалення працівника по ID
#     if worker_id in workers:
#         del workers[worker_id]
#         print(f'Користувача з ID {worker_id} видалено')
#     else:
#         print(f'ID-{worker_id} неіснуе у словнику')
#
# def search_worker(worker_id): # знаходити працівника за ключем
#     if worker_id in workers:
#         print(f'''Працівник з ключем {worker_id} має наступні данні: {workers[worker_id]}''')
#     else:
#         print(f'ID-{worker_id} неіснуе у словнику')
#
# def data_replacement(worker_id):# зміна данних користувача по ID
#     if worker_id in workers:
#         fio = input('Введіть ПІБ:')
#         email = input('Введіть email:')
#         phone = int(input('Введіть телефон:'))
#         position = input('Введіть назву посади:')
#         office = int(input('Введіть номер кабінет:'))
#
#         new_worker_data = {
#                     'ПІБ': fio,
#                     'email': email,
#                     'телефон': phone,
#                     'назва посади': position,
#                     'номер кабінет': office
#                 }
#
#         workers[worker_id] = new_worker_data
#
# print(f'{"Меню для користування словником":^50s}')
# print('1. Додати працівника')
# print('2. Видалити працівника по ID')
# print('3. Знайти працівника за ключем ID')
# print('4. Зміна данних користувача по ID')
# print('5. Вивести інформацію про всіх працівників')
#
# res = int(input('Оберіть операцію: '))
#
# if res == 1:
#     add_worker()
#     print(f'''Оновленний словник:
#     {workers}''')
#
# if res == 2:
#     del_worker(int(input('Введіть ID користувача, якого хочете видалити: ')))
#     print(f'''Оновленний словник:
# {workers}''')
#
# if res == 3:
#     search_worker(int(input('Введіть ID користувача, якого хочете знайти: ')))
#
# if res == 4:
#     data_replacement(int(input('Введіть ID користувача, данні якого Ви хочете замінити: ')))
#     print(f'''Оновленний словник:
#     {workers}''')
#
# if res == 5: #виводити інформацію про всіх працівників у вигляді форматованої таблиці
#     print('-' * 112)
#     print(f'|{"ID":^5s}|{"ПІБ":^30s}|{"email":^22s}|{"Телефон":^14s}|{"Назва посади":^20s}|{"Номер кабінету":^14s}|')
#     print('-' * 112)
#     for key, value in workers.items():
#         print(f'|{key:^5d}|{value["ПІБ"]:<30s}|{value["email"]:^22s}|{value["Телефон"]:^14d}|{value["Назва посади"]:^20s}|{value["Номер кабінету"]:^14d}|')
#         print('-' * 112)

# task1   27
# employees = [
#     {"name": "John Mckee", "age": 38, "department": "Sales"},
#     {"name": "Lisa Crawford", "age": 29, "department": "Marketing"},
#     {"name": "Sujan Patel", "age": 33, "department": "HR"}
# ]
#
# employees_dict = {}    #робимо із списка словник
# for employee in employees:
#     name = employee["name"]
#     employees_dict[name] = employee
#
# for key, value in employees_dict.items():     #Вивести дані у вигляді
#         print(f'Name: {key}')
#         print(f'Age: {value["age"]}')
#         print(f'Department: {value["department"]}')
#         print('-' * 20)
#
# employees_dict['Ivan Savchenko '] = {'name': 'Ivan Savchenko', 'age': 30, 'department': 'development'} #додаемо у словник нового користувача
# print(employees_dict)
#
# for key, value in employees_dict.items(): #модифікувати вивід так, щоб замість name окремо виводилось first name і last name, а замість age – year (рік народження).
#         print(f'First name: {key.split()[0]}')
#         print(f'Last name: {value["name"].split()[1]}')
#         print(f'Year: {2023 - (value["age"])}')
#         print(f'Department: {value["department"]}')
#         print('-' * 20)

# # task2
# Задайте чи згенеруйте окремо два списки: перший – з елементами рядками, інший – з елементами, що є цілими числами.
# Сформуйте словник із цих списків, де перший використовується для ключів, інший відповідно – для значень.
# Користуючись словником виведіть всі ключі із мінімальним значенням.
# Користуючись словником виведіть всі ключі із значеннями, які більші за середнє арифметичне всіх значень у списку.

# srt_lst_cities = ["Київ", "Лондон", "Париж", "Нью-Йорк", "Токіо", "Рим", "Сідней", "Дублін", "Барселона", "Моршин"]  # Задайте чи згенеруйте окремо два списки: перший – з елементами рядками, інший – з елементами, що є цілими числами.
# int_lst = [i*10 for i in range(1,11)]
#
# create_dictionary = dict(zip(srt_lst_cities,int_lst)) # Сформуйте словник із цих списків, де перший використовується для ключів, інший відповідно – для значень.
#
# min_value = min(create_dictionary.values()) # Користуючись словником виведіть всі ключі із мінімальним значенням.
# key_min_value = []
# for key, value in create_dictionary.items():
#     if value == min_value:
#         key_min_value.append(key)
#
# print(f'Ключі із мінімальним значенням: {key_min_value}')
#
# # Користуючись словником виведіть всі ключі із значеннями, які більші за середнє арифметичне всіх значень у списку.
# avg = sum(int_lst) / len(int_lst)
# key_avg_value = []
# for key, value in create_dictionary.items():
#     if value > avg:
#         key_avg_value.append(key)
#
# print(f'Всі ключі із значеннями, які більші за середнє арифметичне всіх значень у списку: {key_avg_value}')

# # task3
# # bank = {1:8, 2:4, 5:20, 10:5, 50:2, 100:20}

# # Словник bank моделює стан гаманця у такий спосіб:
# # -значення банкноти (номінал) – це ключ, а кількість банкнот цього номіналу – значення.
# # -якщо у гаманці відсутня банкнота певного номіналу, то такий елемент відсутній
# #  -у гаманці (не допускається у словнику наявність пар типу {20:0})
# # 1.	Потрібно порахувати суму коштів, що міститься у гаманці.
# # 2.	Згенерувати словник тільки з номіналами, яких є найбільше.

# bank = {1:8, 2:4, 5:20, 10:5, 50:2, 100:20}

# sum = 0  # 1.	Потрібно порахувати суму коштів, що міститься у гаманці.
# for key, value in bank.items():
#     res = key * value
#     sum += res
#
# print(f'Суму коштів, що міститься у гаманці = {sum}')
#
# max_banknotes = {key: value for key, value in bank.items() if
#                  value == max(bank.values())}  # 2.	Згенерувати словник тільки з номіналами, яких є найбільше.
# print(f'Словник тільки з номіналами, яких є найбільше: {max_banknotes}')

# # task 4
# # Видозмініть словник, щоб ключі починатись з великої букви.
# # Виведіть словник у вигляді таблиці, застосувавши форматування.
# # Також знайдіть
# # 1.	середній бал студентів
# # 2.	cтудентів, які мають максимальні оцінки
# # 3.	cтудентів, які не мають оцінки

# students = {
#     'cartman': 10,
#     'stan': 12,
#     'kyle': 9,
#     'kenny': 10,
#     'lisa': None,
#     'jon': 12,
#   }

# new_students = {} #Видозмініть словник, щоб ключі починатись з великої букви.
# for key, value in students.items():
#     new_key = key.capitalize()
#     new_students[new_key] = value
# print(new_students)

# print('-' * 33) #Виведіть словник у вигляді таблиці, застосувавши форматування.
# print(f'|{"Name":^15s}|{"Rating":^15s}|')
# print('-' * 33)
# for key, value in new_students.items():
#     formatted_value = "None" if value is None else value # Використовуємо тернарний оператор
#     print(f'|{key:^15s}|{formatted_value:^15}|')
#     print('-' * 33)

# average_score_of_students = [value for value in new_students.values() if value!= None] #1. середній бал студентів
# print(f'Середній бал студентів = {sum(average_score_of_students) / len(average_score_of_students)}')
#
# max_rating_tuple = {} # 2. cтудентів, які мають максимальні оцінки
# max_rating = (max(average_score_of_students))
# for name, reting in new_students.items():
#     if reting == max_rating:
#         max_rating_tuple[name] = reting
# print(f'Студенти, які мають максимальні оцінки: {max_rating_tuple}')
#
# students_without_a_grade = [] # 3.	cтудентів, які не мають оцінки
# for name, reting in new_students.items():
#     if reting == None:
#         students_without_a_grade.append(name)
# print(f'Cтуденти, які не мають оцінки: {students_without_a_grade}')





