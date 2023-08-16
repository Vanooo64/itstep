# # Завдання 1.
# # a)	Напишіть функцію, яка приймає довільну кількість чисел і повертає новий список, що містить квадрати
# # цих чисел.
# # b)	Напишіть функцію, яка приймає довільну кількість іменованих аргументів, що є числами і повертає список,
# # що містить квадрати цих чисел.
# # c)	Напишіть функцію, яка може приймає довільну кількість позиційних і іменованих аргументів, що є числами
# # і повертає середнє арифметичне цих чисел.
# # Протестуйте виконання функцій
#
# def kvadrat(*args): # a)	Напишіть функцію, яка приймає довільну кількість чисел і повертає новий список, що містить квадрати цих чисел.
#     return [i**2 for i in args ]
#
# res = kvadrat(1,2,3)
# print(res)
#
# def kvadrat(**kwargs): # b)	Напишіть функцію, яка приймає довільну кількість іменованих аргументів, що є числами і повертає список, що містить квадрати цих чисел.
#     return [k**2 for i, k in kwargs.items()]
#
# res = kvadrat(a=1,b=2,c=3,d=4)
# print(res)
#
# def avg(*args, **kwargs): # c) Напишіть функцію, яка може приймає довільну кількість позиційних і іменованих аргументів, що є числами і повертає середнє арифметичне цих чисел.
#     s = sum(args) + sum(kwargs.values())
#     l = len(args) + len(kwargs.values())
#     return s / l
#
# res = avg(1, 2, 3, x=5, y=6)
# print(res)


# # Завдання 2.
# # Напишіть функцію, яка приймає дві дати (тобто функція приймає шість параметрів year1, month1, day1, year2, month2, day2)
# # та обчислює різницю в днях між цими датами. Для обчислень можна використати модуль datatime
#
# import datetime
#
# def difference_in_days(year1, month1, day1, year2, month2, day2):
#     date1 = datetime.date(year1, month1, day1)
#     date2 = datetime.date(year2, month2, day2)
#
#     return (date2 - date1).days
#
#
# res = difference_in_days(2020,2, 29, 2023, 7, 22 )
# print(f"Різниця в днях між датами: {res} днів")

# # Завдання 3.
# # Напишіть рекурсивну функцію, яка виводить в рядок n зірочок, число n задає користувач. Покажіть приклад роботи функції.
#
# def star(n):
#     if n > 0:
#         print('*', end='')
#         star(n-1)
#
# n = int(input("Введіть число зірочок: "))
# star(n)

# # Завдання 4.
# # Напишіть рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b включно. Користувач вводить a та b.
# # Покажіть приклад роботи функції.
#
# def recursive_sum(a, b):
#     if a > b:
#         return 0
#     return a + recursive_sum(a + 1, b)
#
# a = int(input("Введіть число a: "))
# b = int(input("Введіть число b: "))
# result = recursive_sum(a, b)
# print(f"Сума чисел у діапазоні від {a} до {b}: {result}")

# # Завдання 5.
# # Напишіть рекурсивну функцію для обчислення n-го числа послідовності Фібоначчі. Протестуйте виконання роботи функції
#
# def fibonacci_recursive(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
#
# n = int(input("Введіть число n: "))
# res = fibonacci_recursive(n)
# print(f"{n}-е число послідовності Фібоначчі: {res}")



# # Завдання 1
# # Створити функцію, яка обчислює степінь числа та повертає результат. Використати техніку замикання функції,
# # зовнішня функція приймає степінь, внутрішня  - число. Протестувати роботу окремо для степенів 2 і 3.

# def external_degrees(x):
#     def internal_number(n):
#         return n ** x
#     return internal_number
#
# n = int(input('Введіть число: '))
# x = int(input('Введіть степінь: '))
# res = external_degrees(x)(n)
# print(f"{n} в степені {x} = {res}")


# # Завдання 2
# # Реалізувати функцію, яка для заданого тексту і заданого слова виводить кількість входжень цього слова у цей текст,
# # і повертає кількість викликів (внутрішньої функції) для заданого тексту. Регістр значення не має.
# # Використати техніку замикання функції, зовнішня функція приймає заданий текст, внутрішня  - слово. Протестувати роботу.
#
# def external_text(text):
#     count = 0
#
#     def internal_words(words):
#         nonlocal count
#         count+=1
#         entering = text.count(words)
#         return entering, count
#
#     return internal_words
#
# text = 'Привіт Hello Python Привіт Hello Python Привіт Hello Python Hello Python Python'.lower()
# words = "Привіт".lower()
# res = external_text(text)
# print(f'У заданому тексті слово "{words}" зустрічаеться {res(words)[0]} рази')
# print(f'Кількість викликів (внутрішньої функції) = {res(words)[1]} рази')

# # Завдання 3
# # Створити функцію, яка обчислює середнє значення чисел та виконує округлення до зазначеного десяткового розряду.
# # Використати техніку замикання функції, зовнішня функція приймає кількість знаків після коми для округлення,
# # внутрішня  - число, яке добавляється при кожному виклику у список в області enclosing. Протестувати роботу.
#
# def rounding_signs(num_after_coma):   #приймає кількість знаків після коми для округлення
#     lst = []
#     def append_new_num(num):  #приймає число, яке добавляється при кожному виклику у список в області enclosing
#         nonlocal lst
#         lst.append(round(num, num_after_coma)) #додае у список округлене число
#         avg = round(sum(lst) / len(lst), 2) #повертае середне арефментичне округлене до двох знаків
#         return lst, avg
#
#     return append_new_num
#
# res = rounding_signs(2)
# res(10.2335)
# res(11.5534)
# res(12.9853)
#
# print(f'Сформованний список - {res(13.2335)[0]}, Середне арефметичне = {res(13.2335)[1]}')









# def text_in_wich_search(text):
#     c = 0
#
#     def fragmrent_serch(word):
#         nonlocal c
#         c += 1
#         matches = text.count(word)
#         return matches, c
#
#     return fragmrent_serch
#
# sers_test = text_in_wich_search('Програма завершила роботу Програма завершила роботу')()
# print(sers_test('Програма'))




# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n - 1)
#
# print(fact(5))

# def stars(n):
#     if n == 0:
#         return None
#     print('*', end=' ')
#     stars(n-1)
#
# stars(5)
# print()

# def suma(a,b):
#     if a == b:
#         return b
#     return a + suma(a+1, b)
#
# res = suma(1,4)
# print(res)









