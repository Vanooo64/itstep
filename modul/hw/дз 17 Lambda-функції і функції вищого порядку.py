# # Завдання 1
# # Для виконання цього завдання обовязково використовуйте механізм функцій вищого порядку (higher order functions).
# # Створіть окремо дві функції, які перевіряють на парність і непарність передане число відповідно. Користувач визначає
# # на що перевіряти (парність або непарність).
# # Сигнатура функції вищого порядку:
# # def check_value(values_to_check, function_to_call):
# # values_to_check — значення для перевірки.
# # function_to_call — функція перевірки (при виклику в аргумент передається функція для перевірки на парність або функція для перевірки на непарність).
# # Функція check_value повертає значення бульового типу.
# #
# def even_number(num):                               #перевірка на парне число
#     return num % 2 == 0
#
# def odd_number(num):                                #перевірка на непарне число
#     return num % 2 != 0
#
# def check_value(values_to_check, function_to_call):
#     return function_to_call(values_to_check)
#
# # Користувач вводить число для перевірки
# number = int(input("Введіть число: "))
#
# # Користувач вибирає, на що перевіряти: парність чи непарність
# choice = input("Виберіть перевірку (even для парності, odd для непарності): ")
#
# if choice == 'even':
#     res = check_value(number, even_number)
#     print(f"Число {number} є парним: {res}")
#
# elif choice == 'odd':
#     res = check_value(number, odd_number)
#     print(f"Число {number} є непарним: {res}")

# # Завдання 2
# # Написати lambda-функцію, яка приймає на вхід два аргументи. Якщо аргументи більші за нуль, повертаємо їх суму.
# # Якщо обоє менше – різницю. Якщо знаки різні – повертаємо 0. Використати тернарний оператор. Протестувати роботу функції.
#
# a = int(input('Введіть число а: '))
# b = int(input('Введіть число b: '))
# if a > 0 and b > 0:
#     res = lambda a, b: a + b
# elif a < 0 and b < 0:
#     res = lambda a, b: a - b
# elif (a < 0 and b > 0) or (a > 0 and b < 0):
#     res = lambda a, b: 0
#
# result = res(a,b)
# print(result)


# # Завдання 3
# # Заданий список programmers = ['James Gosling', 'Bjarne Stroustrup', 'Donald Knuth', 'Larry Wall', 'Dennis Ritchie'].
# # Відсортуйте елементи списку за зростанням:
# # 1.	за довжиною рядків
# # 2.	прізвищ за алфавітом
# # Використати lambda-функцію.
#
# programmers = ['James Gosling', 'Bjarne Stroustrup', 'Donald Knuth', 'Larry Wall', 'Dennis Ritchie']
# print(sorted(programmers, key=lambda x: len(x))) #1.	сортування за довжиною рядків
# print(sorted(programmers, key=lambda x: x[0]))    # 2.	сортування прізвищ за алфавітом


# Завдання 4
# Задані дані у вигляді списку
# films = [
# {'title': 'The Grand Budapest Hotel', 'year': 2014, 'genre': 'comedy'},
# {'title': 'Inception', 'year': 2010, 'genre': 'thriller'},
# {'title': 'The Hangover', 'year': 2009, 'genre': 'comedy'},
# {'title': 'La La Land', 'year': 2016, 'genre': 'musical'},
# {'title': 'The Social Network', 'year': 2010, 'genre': 'drama'},
# {'title': 'Interstellar', 'year': 2014, 'genre': 'science fiction'},
# {'title': 'Django Unchained', 'year': 2012, 'genre': 'western'},
# {'title': 'The Dark Knight Rises', 'year': 2012, 'genre': 'action'},
# {'title': 'The Wolf of Wall Street', 'year': 2013, 'genre': 'comedy'},
# {'title': 'Mad Max: Fury Road', 'year': 2015, 'genre': 'action'},
# ]

# Завдання 4
# Напишіть функцію my_sort, яка приймає три параметри: список, ключ у словнику та параметр сортування (за зростанням/спаданням) і повертає сортований список.
# Наприклад, виклик функції my_sort(films, 'year', reverse=True) повертає сортований список за спаданням за роком. Використати lambda-функцію.

# films = [
# {'title': 'The Grand Budapest Hotel', 'year': 2014, 'genre': 'comedy'},
# {'title': 'Inception', 'year': 2010, 'genre': 'thriller'},
# {'title': 'The Hangover', 'year': 2009, 'genre': 'comedy'},
# {'title': 'La La Land', 'year': 2016, 'genre': 'musical'},
# {'title': 'The Social Network', 'year': 2010, 'genre': 'drama'},
# {'title': 'Interstellar', 'year': 2014, 'genre': 'science fiction'},
# {'title': 'Django Unchained', 'year': 2012, 'genre': 'western'},
# {'title': 'The Dark Knight Rises', 'year': 2012, 'genre': 'action'},
# {'title': 'The Wolf of Wall Street', 'year': 2013, 'genre': 'comedy'},
# {'title': 'Mad Max: Fury Road', 'year': 2015, 'genre': 'action'},
# ]
#
# def my_sort(lst, key, reverse=True):
#     return sorted(lst, key=lambda x: x[key], reverse=reverse)
#
# res = my_sort(films, 'year', True)
# print(res)

