#               ДОМАШНЯ РОБОТА №35 Функції map, filter, reduce. Анотація.

# # Завдання 1
# #
# # Створіть функцію-генератор, яка приймає два списки та повертає суму значень елементів списків. Опишіть docstring та анотацію типів даних для цієї функції. Протестуйте виконання.
# # Наприклад, якщо у нас є такі списки:
# # [1, 3, 4, 2]
# # [8, 3, 5, 9]
# # Результат буде: 9 6 9 11
# # Якщо передані списки різної довжини, відсутні елементи необхідно вважати рівними нулю.

# from typing import List, Iterable
# def sum_lst(lst1: List[int], Lst2: list[int]) -> Iterable[int]:
#     """
#     Функція повертае суму єлементві двох списків, якщо передані списки різної довжини, відсутні елементи вважаються рівними нулю.
#
#     Параметри:
#     lst1 (list[int]): Перший список цілих чисел
#     lst2 (list[int]): Другий список цілих чисел
#
#     Повертае:
#     Iterable[int]: Генератор, який містить суми відповідних елементів списків."""
#     max_len = max(len(lst1),len(lst2))
#     lst1_update = lst1 + [0] * (max_len - len(lst1))
#     lst2_update = lst2 + [0] * (max_len - len(lst2))
#     if len(lst1) == len(lst2):
#         return map(lambda x, y: x+y, lst1, lst2)
#     else:
#         return map(lambda x, y: x+y, lst1_update, lst2_update)
#
# lst1 = [1, 3, 4, 2, 4, 55]
# lst2 = [8, 3, 5, 9, 6]
#
# res = sum_lst(lst1, lst2)
# print(*res)
# print(sum_lst.__doc__)

# Завдання 2
#
# # Використовуючи функції map, filter, and reduce і lambda, потрібно
# # 1)	Згенерувати вихідну послідовність чисел від 1 до 30.
# # 2)	Отримати послідовність, де кожен елемент піднесений до кубу. Вивести елементи в одному рядку.
# # 3)	Відфільтрувати вихідну послідовність з елементами, які діляться на 3 або на 5. Вивести їх в одному рядку.
# # 4)	Обчислити добуток елементів вихідної послідовності за допомогою reduce.
# # 5)	Перетворити вихідний список у новий список, у якому кожному числу відповідає кількість його цифр.
#
# numbers1_30 = map(int, [x for x in range(1,31)]) # 1)	Згенерувати вихідну послідовність чисел від 1 до 30.
# print('Послідовність чисел від 1 до 30: ')
# print(*numbers1_30)
#
# raised_cube = list(map(lambda x: x**3, [x for x in range(1,11)])) #Отримати послідовність, де кожен елемент піднесений до кубу. Вивести елементи в одному рядку.
# print('Послідовність, де кожен елемент піднесений до кубу:')
# print(*raised_cube)
#
# #3)	Відфільтрувати вихідну послідовність з елементами, які діляться на 3 або на 5. Вивести їх в одному рядку.
# # lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# lst = list(map(int, [x for x in range(1,31)]))
# filt = filter(lambda x: x%3==0 or x%5==0, lst)
# print('Послідовність з елементами, які діляться на 3 або на 5: ')
# print(*filt)
#
# # 4) Обчислити добуток елементів вихідної послідовності за допомогою reduce.
# from functools import reduce
# lst = list(map(int, [x for x in range(1,10)]))
# res = reduce(lambda x, y: x*y, lst)
# print(f'Добуток елементів вихідної послідовності = {res}')
#
# # 5) Перетворити вихідний список у новий список, у якому кожному числу відповідає кількість його цифр.
# lst = [1, 20, 300, 4000, 50000, 600000, 7000000, 80000000, 900000000, 1000000000]
# lst_update = list(map(lambda x: len(x), [str(num) for num in lst]))
# print(f'Список, у якому кожне число відповідає кількість його цифр: {lst_update}')


# # Завдання 4.
# # 1.Задайте функцію log(date, message, important), що форматує та виводить деяку інформацію.
# # 2.Створити часткову функцію з log, у якої «date» та «impotent» — попередньо задані поточні аргументи. Протестуйте виконання.
# # 3.Виконати каррування функції log. Протестуйте виконання.
#
# def log(date: str, message: str, important: bool):
#     print(f'{date}|{message:^20s}|{important}')
# log('28.08.2023', 'Hello world', True)
#
# def tame(date: str, important: bool):
#     def mess(message: str):
#         print(f'{date}|{message:^20s}|{important}')
#     return mess
#
# teams = tame('28.08.2023', True)
# teams('Python')
# teams('CSS')

#                               ДОМАШНЯ РОБОТА №36 ДЕКОРАТОРИ
# # Завдання 1
# # Задана функція
# # def divide(a: float, b: float) -> float:
# #     print('виконується ділення')
# #     return a/b
# # Декоруйте задану функцію, не змінюючи її, так, щоб вона приймала тільки числові значення і
# # не приймала b=0, інакше задану функцію не викликати і вивести повідомлення про некоректність
# # даних.
#
# def wrapper_get_int(func):
#     def wrapper(a, b):
#         if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#             print('Функція може приймати тільки числові значення!')
#             return None
#
#         if b == 0:
#             print('Аргумент "b" не може дорівнювати нулю!')
#             return None
#         return func(a, b)
#
#     return wrapper
#
# @wrapper_get_int
# def divide(a: float, b: float) -> float:
#     print('виконується ділення')
#     return a / b
#
# a = int(input('Ведіть число а: '))
# b = int(input('Ведіть число b, воно повинно бути > 0: '))
# res = divide(a, b)
# if res is not None:
#     print(f'{a} / {b} = {round(res, 2)}')
#
# # Завдання 2
# # Задана функція, яка за кількістю і ціною у грн. товару видає суму, яку потрібно заплатити покупцеві у грн.
#
# # A)	Припустимо, що вам потрібно отримати суму покупки у доларах за курсом 37.8, скориставшись функцією check
# # і не міняючи її. Для цього виконати декорування функції check.
# def decor_сheck(func):
#     def wrapper(count, price):
#         result_func = func(count, price)
#         summ = int(result_func[:2])
#         USD = round((summ / 37.8), 2)
#         return f'{USD} USD'
#
#     return wrapper
#
# @decor_сheck
# def check(count, price):
#     print(f"check=|{count}|{price}|")
#     summa = count * price
#     return f"{summa} UAH"
#
# res = check(2, 10)
# print(res)
#
#
# res# B)	Представте, що на наступний день курс обміну змінився. Потрібно змінити у коді числове значення курсу?!
# # Розробіть новий декоратор з параметром для завдання A, де параметром буде курс обміну.
#
#
# def defcreate_decorator(A):
#     def decor_сheck(func):
#         def wrapper(count, price):
#             result_func = func(count, price)
#             summ = int(result_func[:2])
#             USD = round((summ / A), 2)
#             return f'{USD} USD'
#
#         return wrapper
#     return decor_сheck
#
# A = float(input('Введіть курс долара на сьогодні: '))
# @defcreate_decorator(A)
# def check(count, price):
#     print(f"check=|{count}|{price}|")
#     summa = count * price
#     return f"{summa} UAH"
#
# res = check(2, 10)
# print(res)
#
#
# # Завдання 3
# # Задані функції
#
# # def f1():
# #     res = ''
# #     for i in range(10**6):
# #         res += ' '
#
# # def f2():
# #     res = ' ' * 10**6
# # Використовуючи механізм декораторів, створіть декоратор timer для виводу кількості часу виконання деякої функції.
# # Застосуйте цей декоратор до функції f1 і f2.
#
# from time import time
# def timer(func):
#     def wrapper():
#         start = time()
#         res = func()
#         end = time()
#         delta_time = end - start
#         return delta_time
#     return wrapper
#
# @timer
# def f1():
#     res = ''
#     for i in range(10**6):
#         res += ' '
#
# @timer
# def f2():
#     res = ' ' * 10**6
#
# res1 = f1()
# print(f'Кількость часу на виконання функції f1 = {res1}')
# res2 = f2()
# print(f'Кількость часу на виконання функції f2 = {res2}')
#
# # Завдання 4
# # 1.	Створіть функцію even_nums(a,b), що повертає список з усіма парними числами від a до b включно.
# # Створіть декоратор log для виводу назву функції, яка виконувалась, та які аргументи a,b приймала.
# # Застосуйте цей декоратор до функції even_nums. Протестуйте роботу even_nums.
# # 2.	Добавте до функції ще один декоратор timer (для виводу кількості часу виконання функції.),  тобто
#
# from time import time
# def log(func):
#     def wrapper(a, b):
#         name = func.__name__
#         print(f'Була використана функція "{name}" з аргументами від {a} до {b}')
#         return func(a, b)
#     return wrapper
#
# def timer(func):
#     def wrapper(a, b):
#         start = time()
#         res = func(a, b)
#         end = time()
#         calculate_time = end - start
#         print(f'Час виконання = "{round(calculate_time, 5)}" секунди')
#         return f"Результат виконання функції {res}"
#     return wrapper
#
# @timer
# @log
# def even_nums(a,b):
#     return [num for num in range(a,b+1) if num % 2 == 0]
#
# a = int(input('Ведіть число а: '))
# b = int(input('Ведіть число b: '))
# res = even_nums(a,b)
# print(res)
