# def my_sum(a, b): #визначення функції
#     print('a+b', a+b)
#     return a + b
#
# result = my_sum(10, 20)
# print(result)

# def my_sum(a, b): #визначення функції
#     print('a+b', a+b)
#     #return None #автоматично добавляе, якщо return немає
#
# result = my_sum(10, 20)
# print(result)

# def my_sum(a, b): #ключові аргументи
#     return a - b
#
# result = my_sum(b=20, a=10,)
# print(result)

# def my_sum(a=1, b=0): #Аргументи за замовчуванням
#     return a - b
#
# result = my_sum()
# print(result)

# def my_sum(a, b):
#     pass # конструкція яка нічого неробить

# def my_sum(*args):
#     print(args, type(args))
#     print(sum(args))
#     s = 0
#     for i in args:
#         s+=i
#     return s
#
# result = my_sum(1,2,3,4,6,10)
# print(result)
#
# lst = [10,3,11,5,7]
# result = my_sum(*lst) #розпаковуемо список і передаемо в кортеж
# print(result)


# def my_sum_2(array):
#     return sum(array)
#
# lst = [10,3,11,5,7]
#
# result2 = my_sum_2(lst)
# print(result2)

# def avg(*array):
#     return sum(array) / len(array)
#
# result = avg(1,2,3,4,6,10)
# print(result)

# def my_sum(a, b=0, *numbers): #довільна кількість позиційних аргументів мае бути в кінці
#     print(f'{a=} {numbers=}')
#     s = 0
#     for i in numbers:
#         s+=i
#     return s
#
# result = my_sum(1,2,3,3,4,6,10)
# print(result)

# Створення словника
# d = dict(name='Ivan', password=1234)
# # print(d)
#
# def my_func(**kwargs):
#     print(kwargs)
#     for k,v in kwargs.items():
#         print(f'{k=} {v=}')
#
# my_func(name='Ivan', password=1234, email='123@gmail.com') #предаемо аргуументи вручну якщо вказали **kwargs
# my_func(**d)



# d = dict(name='Ivan', password=1234)
# lst = [1,2,3]
#
# def my_func(*args, **kwargs): #*args - позиційні аргументи, **kwargs - меновані аргуументи
#     print(f'{args=}')
#     print(f'{kwargs}')
#
# # my_func(1,2,3, name='Ivan', password=1234, email='123@gmail.com') #предаемо аргуументи вручну якщо вказали **kwargs
# my_func( *lst, **d,) #анологічно



def my(lst,x=0):
    temp = lst.copy() #робимо копію
    temp.append(x) #додаемо нове значення
    return temp

lstt = [1,2,3]

res = my(lstt,5)
print(res)

res2 = my(lstt,9)
print(res2)

