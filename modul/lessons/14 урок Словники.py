# data = {'Sam': 42, 'Ron': 35, 'Bob': 38}
# print(data)
#
# empty_dict = dict()  # створення порожнього словника
# empty_dict = {}
#
# print("Ron" in data)  # перевірка на наявність ключа
#
# print(data['Ron'])  # звернення до значення по ключу
# print(data.get('Bob'))  # звернення до значення по ключу через метод
# print(data.get('Alisa',
#                'Такого ключа немає'))  # звернення до значення по ключу через метод, якщо такого ключа немае повертае None або задане значення
# data['Sam'] = 43  # Зміна значення по ключу
# data['Alisa'] = 20  # Додавання нового значення в кінець
#
# x = data.pop('Bob')  # Видалити елесент по ключу і зберігае його
# print(x, data)
#
# x = data.pop('Bob1', 1)  # Видалити елесент по ключу і зберігае його, якщо ключа неіснуе видае помилку
# print(x, data)
#
# y = data.popitem()  # видаляе останній елемент, зберіае (ключ:значення)
# print(y, data)  # ('Alisa', 20) {'Sam': 43, 'Ron': 35}
#
# del data['Sam']  # видалення по ключу
#
# data.clear()  # видаляе всі елементи словника
# del data  # видаляе весь словник

# Обеднання словників
#
data = {'Sam': 42, 'Ron': 35, 'Bob': 38}
# print(data)
# print(data.keys()) #dict_keys(['Sam', 'Ron', 'Bob']) відображае ключі
# print(data.values()) #dict_values([42, 35, 38])
# print(data.items()) #dict_items([('Sam', 42), ('Ron', 35), ('Bob', 38)])
#
# list = list(data.values()) #переводимо у список
# print(list[0]) #звертаемось по індексу
# print(*list, sep= ', ')
#
#
for key in data: # ітерація по ключу
    print(key, end = ' ')
#
# for key in data: # ітерація по значеню
#     print(data[key], end = ' ')
#
# for value in data.values(): # ітерація по значеню
#     print(value, end = ' ')
#
# for key, value in data.items():  # ітерація по ключу:значеню
#     print(key, value)
#
# data = {'Sam': 42, 'Ron': 35, 'Bob': 38}
# lst = [2, 12, 1993]
# data['Vano'] = lst
# print(data) #{'Sam': 42, 'Ron': 35, 'Bob': 38, 'vano': [2, 12, 1993]}
# lst[-1] = 1990
# print(lst)
# print(data) #{'Sam': 42, 'Ron': 35, 'Bob': 38, 'Vano': [2, 12, 1990]}

# persons = [
#     {'name': 'Sam', 'age': 42},
#     {'name': 'Ron', 'age': 35},
#     {'name': 'Bob', 'age': 38},
# ]
# for person in persons:
#     print(person['name'], person['age'])


# persons = [
#     {'name': 'Sam', 'age': [42, 0]},
#     {'name': 'Ron', 'age': [35, 5]},
#     {'name': 'Bob', 'age': [38, 7]},
# ]
#
# for person in persons:
#     print(person['name'], person['age'][0])

# persons = [
#     {'name': 'Sam', 'age': 42},
#     {'name': 'Ron', 'age': 35},
#     {'name': 'Bob', 'age': 38},
# ]
#
# for person in persons:
#     print(person['name'].lower(), person['age'])
#     person['name'] = person['name'].lower()
#
# print(person)






from pprint import pprint

# persons = [
#     {'name': 'Sam', 'age': [42, 0]},
#     {'name': 'Ron', 'age': [35, 5]},
#     {'name': 'Bob', 'age': [38, 7]},
#     {'name': 'Alisa', 'age': [42, 7]}
# ]

# s = 0
# for person in persons:
#     s += person['age'][0]
#
# pprint(person)
# print(f'avg = {s / len(person):.2f}')

# res = sum([person ['age'][0] for person in persons]) / len(persons)
# print(f'{res:.2f}')
#
# max_age = max([person ['age'][0] for person in persons])
# print(f'{max_age:.2f}')
#
# max_namse = [person['name'] for person in persons if person['age'][0] == max_age]
# print(f'max_age = {max_age}, max_name = {max_namse}')



# my_dict = {x: x ** 2 for x in range(10) if x % 2 == 0}
# # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# print(my_dict)

#Створення словника генератором
# a = ['a', 'b', 'c'] #значення
# b = [1, 2, 3] #ключі
# c = list(zip(a,b))
# print(c)
# #1
# my_dict = dict(c)
# print(my_dict)
# #2
# my_dict_2 = dict(zip(a,b))
# print(my_dict_2)
# # 3
# my_dict_3 = {k:v for k,v in zip(a,b)}
# print(my_dict_3)
# # 4
# my_dict_4 = {k:v**2 for k,v in zip(a,b)}
# print(my_dict_4)
# # 5
# # 4
# my_dict_5 = {k:v**2 for k,v in zip(a,b) if k != 'a'}
# print(my_dict_5)


# a = ['a', 'b', 'c', 'd', 'e', 'f'] #значення
# b = [1, 2, 3,] #ключі
# b = b + [None] * (len(a) - len(b)) #заповнити список None
# my_dict_6 = dict(zip(a,b))
# print(my_dict_6)


# data = {'Sam': 42, 'Ron': 35, 'Bob': 38, 'Vova': [2,12,1989]}
# data_2 = data.copy() #поверхнева копія
# print(data)
# print(data_2)
#
# data['Vova'][-1] = 2000
# print()
# print(data)
# print(data_2)
#
# text = '''Окрім пускових установок Patriot, Україна отримала від Німеччини 6525 155-мм димових боєприпасів, 10 гусеничних всюдиходів BV206, п’ять автомобілів охорони кордону, чотири розвідувальні безпілотники VECTOR.
# Згадуються також матеріали для знешкодження вибухонебезпечних предметів, понад тисяча біноклів і 20 тисяч захисних окулярів, шість сідельних тягачів 8x8 HX81 та п’ять напівпричепів, два ваговози 8х6 з контейнерами, а ще – 40 тисяч аптечок.
# Нагадаємо, Німеччина передала Україні зенітно-ракетний комплекс Patriot із ракетами до нього у квітні 2023 року. До складу одного комплексу входять радар, командний пункт і до восьми пускових установок, розрахованих на чотири ракети кожна.'''

# for char in '!?.,–':
#     text = text.replace(char, ' ')
#
# words = text.lower().split()
# print(words)

# mydict = {word: words.count(word) for word in set(words)}
# print(mydict)
#
# max_count = max(mydict.values())
#
# max_dikt = {k: v for k, v in mydict.items() if v == max_count} #k - word, v- count word in words
# print(max_dikt)
