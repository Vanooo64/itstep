# x = 2
# print(x, type(x))
#
# def func():
#     return 5
#
# y = func()
# print(y, type(y))
# res  = func()
# rez = y()


# def func(x, z):
#     return x**2 + z
#
# def high_func(f, x, z): #функція вищого порядку, яака приймае іншу функцію
#     res = f(x, z)
#     return res
#
# out = high_func(func, 5, 3)
# print(f'{out=}')


# def lambda_1(x):
#     return x+2
# print(lambda_1(3))
#
# # Аналогічно лямбда функціею
# f = lambda x: x + 2
# print(f(3))
#
# # Аналогічно лямбда функціею
# print((lambda x: x + 2) (3))
#
# # Сортування лямбда функціею
# months  = [(1, 'january'), (1, 'january'), (1, 'january') ]

# #                       ітератори
#
# lst = [4, 7, 0, 3]
# for x in lst:
#     print(x)
#
# # анологічно
#
# lst_iter = iter(lst)
# print('__next__' in dir(lst_iter))
# print(next(lst_iter))
# print(next(lst_iter))
# print(next(lst_iter))
# print(next(lst_iter))
# print(next(lst_iter)) # на цьому кроці буде помилка StopIteration
#
# # анологічно
# iter = iter(lst)
# while True:
#     try:
#         x = next(iter)
#         print(x)
#     except StopIteration:
#         break


# r = range(1,10)
# print(list(r), type(r))
#
# it = iter(r) #присвоення ітератору для функції ренж
# it = r.__iter__() #присвоення ітератору для функції ренж за допомогою методу
#
# print('__next__' in dir(it)) # перевірка методів
# print('__iter__' in dir(it))
#
# print(next(it))
# print(it.__next__())

#               Генетатор функцій
# import sys
# n = 1000000
# lst = [x for x in range(n)]
# print(f'список в байтах = {sys.getsizeof(lst)}') #визначае скільки займае память в байтах
# print(f'список в мегабайтах = {sys.getsizeof(lst)/2**20}') #визначае скільки займае память в мегабайтах
#
# g = (x for x in range(n)) #визначае скільки займае память
# print(sys.getsizeof(g)) #визначае скільки займае память в байтах
# print(sys.getsizeof(g)/2**20) #визначае скільки займае память в мегабайтах

#перевірка на ітератор
# print('__iter__' in dir(g))
# print('__iter__' in dir(g))

# def gen():
#     yield '1'
#     print('After 1')
#     yield '2'
#     print('After 2')
#     yield '3'
#     print('After 3')
#     yield 'до побачення'
#
# g = gen() # повертае обект ітератора
# g2 = gen()
# # print(f'{g=}, {type(g)}')
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
#
# for x in g:
#     print(x)
#
# print(list(g2)) #можно додати елементи до списку






# # Завдання 1.
# # Побудуйте ітератор, який буде перебирати всі числа в діапазоні від start до end включно з деяким кроком step.
#
# stat, end, step = 5, 22, 3
# g = (x for x in range(stat, end + 1, step)) #генератор виразу
# print(list(g))
#
# def my_gen(stat, end, step):
#     for x in range(stat, end + 1, step):
#         yield x
#
# gen = my_gen(5, 22, 3)
# print(list(gen))
# print(*gen)

# # Завдання 3.
# # Напишіть функцію-генератор для генерації послідовності довжиною n степенів числа 2 (2, 4, 8, 16, ..., 2**n). Протестувати роботу.

# def power(n):
#     for x in range(0,n+1):
#         yield 2**x
#
# p = power(10)
# print(*p)
#
# for x in power(20):
#     print(x, end=' ')

# #аналогічно
# def power(n):
#     i = 0
#     while i <= n:
#         yield 2 ** i
#         i = i + 1
#
# p = power(10)
# print(*p)
#
# for x in power(20):
#     print(x, end=' ')

# Завдання 4.
# · Написати генератор-функцію, щоб отримати всі числа Фібоначчі (безкінечний генератор). Створити об’єкт цієї генератор-функції та перебрати 10 перших елементів послідовності за допомогою функції next. Перебрати ці елементи іншим способом без next за допомогою циклу for і break.
# · Написати генератор-функцію з параметром n, що дозволяє отримати всі числа Фібоначчі в діапазоні від 1 до n.

# def gen_fibonachi():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = a + b, a
#
# g = gen_fibonachi()
#
# count = 0
# for x in g:
#     print(f'{count} -> {x}')
#     if count > 10:
#         break
#     count += 1
#
# g2 = gen_fibonachi()
# for _ in range(10):
#     x = next(g2)
#     print(x, end= ' ')
#
# def gen_fib(n):
#     a, b = 0, 1
#     while a <= n:
#         yield a
#         a, b = a + b, a
#
#
# for x in gen_fib(10):
#     print(x, end=' ')
