# # Task 1
# # Напишіть функцію, яка виводить на екран форматований
# # текст, наведений нижче:
# # “Don’t compare yourself with anyone in this world…
# #  if you do so, you are insulting yourself.”
# # Bill Gates
#
# def get_taxt():
#     print(f'''“Don’t compare yourself with anyone in this world…
#     if you do so, you are insulting yourself.”
#                                             Bill Gates''')
#
# get_taxt()

# # Task 2
# # Напишіть функцію, яка приймає два числа як параметр
# # і відображає усі парні числа між ними.
#
# def even_numbers(a, b):
#     lst = []
#     for num in range(a,b+1):
#         if num % 2 == 0:
#             lst.append(num)
#     return lst
#
# # # аналогічно генератором списку
# #     lst = [num for num in range(a,b+1) if num % 2 == 0]
# #     return lst
#
# res = even_numbers(1,100)
# print(res)

# # Завдання 3
# # Напишіть функцію, яка відображає порожній або заповнений квадрат із певним символом. Функція приймає в якості параметрів
# # довжину сторони квадрата, символ та змінну логічного типу:
# # ■ якщо вона дорівнює True, квадрат заповнений;
# # ■ якщо False, квадрат порожній
#
# def square_selection(length_square, symbol, logical_type): #функція для вибору квадрату
#     if logical_type:
#         return filled_square(length_square, symbol)
#     else:
#         return empty_square(length_square, symbol)
# def filled_square(length_square, symbol): #функція для заповненого квадрату
#     for i in range(length_square):
#         for j in range(length_square):
#             print(symbol, end=' ')
#         print()
# def empty_square(length_square, symbol): #функція для пустого квадрату
#     for i in range(length_square):
#         for j in range(length_square):
#             if i == 0 or i == length_square - 1 or j == 0 or j == length_square - 1:
#                 print(symbol, end=' ')
#             else:
#                 print(' ', end=' ')
#         print()
# length_square = int(input('Введіть довжину сторони квадрата: '))
# symbol = input('Введіть символ для заповнення квадрата: ')
# logical_type = input('Якщо Ви хочете, щоб квадрат був заповнений введіть любий символ, щоб квадрат був порожній натисніть Enter: ')
# square_selection(length_square, symbol, logical_type)

# # Завдання 4
# # Напишіть функцію, яка повертає мінімальне з п’яти чисел. Числа передаються як параметри.
# def min_nambers(a,b,c,d,e):
#     return min(a,b,c,d,e)
#
# res = min_nambers(2,4, 10,6,3)
# print(res)

# # Завдання 5
# # Напишіть функцію, яка повертає добуток чисел у зазначеному діапазоні. Межі діапазону передаються як параметри.
# # Якщо межі діапазону переплутані (наприклад, 5 — верхня межа, 25 — нижня межа), їх треба поміняти місцями.
#
# def product_numbers (a,b):
#     if b < a:
#         b, a = a, b
#
#     prod = 1
#     for i in range(a,b+1):
#         prod*=i
#     return prod
#
# res = product_numbers(5,1)
# print(res)

# # Завдання 6
# # Напишіть функцію, яка підраховує кількість цифр у числі.
# # Число передається як параметр. Поверніть з функції отриману
# # кількість цифр. Наприклад, якщо передали 3456, кількість
# # цифр буде 4.
#
# def len_numbers(a):
#     count = len(str(a))
#     return count
#
# num = int(input('Введіть число: '))
# res = len_numbers(num)
# print(f'Кількість цифр у числі {num} = {res}')

# # Завдання 7
# # Напишіть функцію, яка перевіряє число на паліндром.
# # Число передається як параметр. Якщо число є паліндромом,
# # поверніть з функції true, якщо ні — false.
# #
# # «Паліндром» — це число, в якому перша частина цифр
# # дорівнює другій перевернутій частини цифр. Наприклад,
# # 123321 — паліндром (перша частина 123, друга 321, яка після
# # перевороту стає 123), 546645 — паліндром, а 421987 — не
# # паліндром.
#
# def palindrom(a):
#     pali = str(a)
#     palind = pali[::-1]
#     if palind == pali:
#         return 'true'
#     else:
#         return 'false'
#
# res = palindrom(421987)
# print(res)

# Завдання 1
# Hапишіть три функції:
# 1.	приймає назву користувача і друкує для нього привітання. Якщо користувач не переданий, то вивести повідомлення для "Guest".
# 2.	приймає довільну кількість користувачів і виводить повідомлення із привітанням для кожного з них
# 3.	приймає довільну кількість іменованих аргументів про користувача (наприклад, name, age, email, score) і виводить їх в окремому рядку.
# Протестувати виклики функцій

# # 1. приймає назву користувача і друкує для нього привітання. Якщо користувач не переданий, то вивести повідомлення для "Guest".
# def hello(name='Guest'):
#     print(f'Вітаю Вас {name}')
#
# name = input("Введіть свое ім'я: ")
# if name:
#     hello(name)
# else:
#     hello()
#
# # 2. приймає довільну кількість користувачів і виводить повідомлення із привітанням для кожного з них
# def many_name(*args):
#     for name in args:
#         print(f'Вітаю Вас {name}')
#
# users = input('Введіть довільну кількість користувачів: ').split()
# many_name(*users)
#
# # 3.Приймає довільну кількість іменованих аргументів про користувача (наприклад, name, age, email, score) і виводить їх в окремому рядку.
#
# def tup(**kwargs):
#     return (kwargs)
#
# res = tup(name='Ivan', age=30, email='glazglojon@gmail.com', score='1234')
# print(res)


# # Завдання 2
# # Напишіть функцію на вхід приймає список і число та видаляє зі цього списку це число.
# # З функції потрібно повернути кількість видалених елементів.
#
# def pop_numbers(lst, num):
#     count = lst.count((str(num)))
#     return count
#     for _ in lst:
#         lst.pop(num)
#
# res = pop_numbers(lst=['35', '89', 'Ivan', '79', '1', '2', '3', '4', '5', '6', '6', '6', '7', '4', '9', 'python'], num = 6)
# print(f'Кількість видалених елементів = {res}')

# # Завдання 3
# # Написати функцію, яка приймає на вхід два аргументи. Якщо аргументи більші за нуль, повертаємо їх суму. Якщо обоє менше – різницю.
# # Якщо знаки різні – повертаємо 0.
#
# def result(a, b):
#     if a > 0 and b > 0:
#         return a+b
#     elif a<0  and b < 0:
#         return a-b
#     else:
#         return 0
# res = result(16,6)
# print(f'Результат = {res}')

# # Завдання 4
# # Імплементуйте функцію, яка приймає два аргументи: перший – список чисел, другий – булевий прапорeць. Якщо прапор = True – повертаємо новий
# # список із непарними числами із вхідного списку, якщо прапор False – повертаємо новий список із парними числами.
#
# def even_or_odd_numbers(lst, bool):
#     if bool == True:
#         return  [num for num in lst if num % 2 != 0]
#     else:
#         return  [num for num in lst if num % 2 == 0]
#
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# odd_numbers = even_or_odd_numbers(num, bool=True)
# even_numbers = even_or_odd_numbers(num, bool=False)
# print(f'Непарні числа із вхідного списку: {odd_numbers}')
# print(f'Парні числа із вхідного списку: {even_numbers}')

# Завдання 5
# a) Напишіть функцію для підрахунку добутку елементів списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
# b) Написати функцію, яка приймає будь-яку кількість аргументів чисел. За її допомогою повернути добуток чисел

# a) Напишіть функцію для підрахунку добутку елементів списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
def product(lst):
    prod = 1
    for i in lst:
        prod*=i
    return prod

res  = product(lst=[1, 2, 3, 4, 5, 6 ])
print(f'Добуток елементів списку цілих чисел = {res}')

# b) Написати функцію, яка приймає будь-яку кількість аргументів чисел. За її допомогою повернути добуток чисел
def product_many_numbers(*args):
    prod = 1
    for i in args:
        prod*=i
    return prod

res  = product_many_numbers(1, 2, 3, 4, 5, 6, 7)
print(f'Добуток будь-якої кількісті аргументів чисел = {res}')
