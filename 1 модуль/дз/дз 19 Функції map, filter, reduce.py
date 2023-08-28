# # Завдання 1
# #
# # Створіть функцію-генератор, яка приймає два списки та повертає суму значень елементів списків. Опишіть docstring та анотацію типів даних для цієї функції. Протестуйте виконання.
# # Наприклад, якщо у нас є такі списки:
# # [1, 3, 4, 2]
# # [8, 3, 5, 9]
# # Результат буде: 9 6 9 11
# # Якщо передані списки різної довжини, відсутні елементи необхідно вважати рівними нулю.

# from typing import List, Iterable
# def sum_lst(lst1: List[int], lst2: List[int]) -> Iterable[int]:
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


# Завдання 4.
# 1.Задайте функцію log(date, message, important), що форматує та виводить деяку інформацію.
# 2.Створити часткову функцію з log, у якої «date» та «impotent» — попередньо задані поточні аргументи. Протестуйте виконання.
# 3.Виконати каррування функції log. Протестуйте виконання.

def log(date, message, important):
    def
    pass







