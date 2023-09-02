#map

# import random
# n = 20
# random.seed(1)
#
# lst = [random.randint(-10, 10) for _ in range(n)]
# print(*lst)
#
# lst2 = [i*i for i in lst] # возведення в квадрат
# print(*lst2)
#
# lst_sq = map(lambda item: item**2, lst) #повертае ітератор возведенний в квадрат
# print(list(lst_sq))

# arr = list(map(int, input('Введіть елемент: ').split()))
# print(arr)



# filter повертае значення булевого типу
# import random
# n = 20
# random.seed(1)
#
# lst = [random.randint(-10, 10) for _ in range(n)]
# print(*lst)
#
# lst2 = [i for i in lst if i > 0] # повертае позитивні числа
# print(*lst2)
#
# # аналогвчно за допомогою функції filter
# positive_nums = filter(lambda x: x > 0, lst)
# print(positive_nums)
#
#
# import random
# n = 20
# random.seed(1)
#
# lst = [random.randint(-10, 10) for _ in range(n)]
# print(*lst)
# def positive(x):
#     return x > 0
#
# positive_nums = filter(lambda x: x > 0, lst)
# # аналогічно
# positive_nums2 = filter(positive, lst)
# print(*positive_nums)
# print(*positive_nums2)
#
#
#
# # анотація для розробників (doc string)
# def positive(x: int) -> bool: #: int) -> bool анотація для розробників
#     """This func return ..."""
#     return x > 0

# from collections.abc import  Callable
#
# def hello():
#     print('Hello world')
#
# def process(f: Callable[[], None]) -> None:
#     print('process start')
#     f()
#     print('process end')
#
# process(hello)



# функція reduсe

# from functools import reduce
# lst = [1,2,3,4,5,6] # треба порахувати сумму
# summa = reduce(lambda x,y: x+y, lst)
# print(summa)
#
# factorial = reduce(lambda x,y: x*y, lst) #факторіал
# print(factorial)

# Каріг
# def foo(x, y, z):
#     return x * x + y - z
#
#
# print(foo(5, 10, 34))
#
#
# def carry(x):
#     def inner1(y):
#         def inner2(z):
#             return x * x + y - z
#
#         return inner2
#
#     return inner1
#
#
# f1 = carry(5)
# print(f1, f1.__closure__[0].cell_contents) #<function carry.<locals>.inner1 at 0x1074a27a0> 5
# f2 = f1(10)
# print(f2, f2.__closure__[1].cell_contents) #<function carry.<locals>.inner1.<locals>.inner2 at 0x1074a2830> 10
# f3 = f2(34)
# print(f3)
#
# result = carry(5)(10)(34)
# print(result)



#      Декоратор

# def decorator(fn): # приймае функцію my_print
#     def wrapper(): #повертае обгортку функції fn
#         print('befor call fn')
#         fn() # виконуеться визов  'Hello Python'
#         print('after call fn')
#     return wrapper
#
# def my_print():
#     print('Hello Python')
#
# decor_func = decorator(my_print)
# decor_func()
#
#
# Використання синтаксису
# def decorator(fn): # приймае функцію my_print
#     def wrapper(): #повертае обгортку функції fn
#         print('befor call fn')
#         fn() # виконуеться визов  'Hello Python'
#         print('after call fn')
#     return wrapper
#
# @decorator #@decorator - спеціальний синтаксис для декорування фуункції my_print функціею decorator
# def my_print():
#     print('Hello Python')
#
# my_print()
#
# Декоратор з іменованним параметром
#
# def decorator(fn): # приймае функцію my_print
#     def wrapper(name="Guest"): #повертае обгортку функції fn з параметром name
#         print('******')
#         fn(name) # виконуеться визов  'Hello {name}'
#         print('******')
#     return wrapper
#
# @decorator #@decorator - спеціальний синтаксис для декорування фуункції my_print функціею decorator
# def my_print(name):
#     print(f'Hello {name}')
#
# my_print('Ivan')
#
# # Декоратор з невизначеню кількісю параметрів
# def decorator(fn): # приймае функцію my_print
#     def wrapper(*args, **kwargs): #повертае обгортку функції fn з параметром name
#         print('******')
#         fn(*args, **kwargs) # виконуеться визов  'Hello {name}'
#         print('******')
#     return wrapper
#
# @decorator #@decorator - спеціальний синтаксис для декорування фуункції my_print функціею decorator
# def my_print(*args):
#     print(f'Hello {args}')
#
# my_print('Ivan', 'Petro', 'Vlad')
#
#
#
#
#
# def decorator(fn): # приймае функцію my_print
#     def wrapper(*args, **kwargs): #повертае обгортку функції fn з параметром name
#         print('******')
#         result  = fn(*args, **kwargs) # виконуеться визов  'Hello {name}'
#         print('*' * result)
#     return wrapper
#
# @decorator #@decorator - спеціальний синтаксис для декорування фуункції my_print функціею decorator
# def my_print(*args):
#     print(f'Hello {args}')
#     return 10
#
# my_print('Ivan', 'Petro', 'Vlad')

# #           декоратор з параметром
# def defcreate_decorator(param):
#     def decorator(fn): # приймае функцію my_print
#         def wrapper(*args, **kwargs): #повертае обгортку функції fn з параметром name
#             print('*' * param)
#             result  = fn(*args, **kwargs) # виконуеться визов  'Hello {name}'
#             print('*' * param)
#         return wrapper
#     return decorator
#
# @defcreate_decorator (param = 10)#@decorator - спеціальний синтаксис для декорування фуункції my_print функціею decorator
# def my_print(*args):
#     print(f'Hello {args}')
#
# my_print('Ivan', 'Petro', 'Vlad')

# #           декоратор з двома параметрами
# def defcreate_decorator(param1, param2):
#     def decorator(fn): # приймае функцію my_print
#         def wrapper(*args, **kwargs): #повертае обгортку функції fn з параметром name
#             print('*' * param1)
#             result  = fn(*args, **kwargs) # виконуеться визов  'Hello {name}'
#             print('*' * param2)
#         return wrapper
#     return decorator
#
# @defcreate_decorator (5, 10) #@decorator - спеціальний синтаксис для декорування фуункції my_print функціею decorator
# def my_print(*args):
#     print(f'Hello {args}')
#
# my_print('Ivan', 'Petro', 'Vlad')

# def decorator(fn): # приймае функцію my_print
#     def wrapper(*args, **kwargs): #повертае обгортку функції fn з параметром name
#         print('******')
#         result  = fn(*args, **kwargs) # виконуеться визов  'Hello {name}'
#         print('*' * result)
#     return wrapper
#
# @decorator #@decorator - спеціальний синтаксис для декорування фуункції my_print функціею decorator
# def my_print(*args):
#     print(f'Hello {args}')
#     return 10


# from time import time, sleep
#
# def timer(fn): # приймае функцію my_print
#     def wrapper(*args, **kwargs): #повертае обгортку функції fn з параметром name
#         start = time()
#         result  = fn(*args, **kwargs) # виконуеться визов  'Hello {name}'
#         end = time()
#         delta_time = end - start
#         return delta_time
#     return wrapper
#
# @timer #@decorator - спеціальний синтаксис для декорування фуункції my_print функціею decorator
# def my_print(*args):
#     sleep(2)
#     print(f'Hello {args}')
#
# delta_time = my_print('Ivan', 'Glib')
# print(delta_time)
#
#
#
#
#
from time import time, sleep

def timer(fn): # приймае функцію my_print
    def wrapper(*args, **kwargs): #повертае обгортку функції fn з параметром name
        start = time()
        result  = fn(*args, **kwargs) # виконуеться визов  'list_time'
        end = time()
        delta_time = end - start
        return delta_time
    return wrapper

@timer
def list_time(*args):
    sleep(2)
    lst = list(range(1000000))
    return lst

print(list_time())