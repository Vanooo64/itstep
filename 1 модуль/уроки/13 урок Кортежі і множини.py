# t = () #пустий кортеж
# t1  = tuple() #пустий кортеж
# t2 = ('item', ) #кортеж з 1 елемента
# t3 = 'item', #кортеж з 1 елемента
# t4 = 1, 2 #кортеж з 2 елементів
# t5 =  (1,2,3,4)  #кортеж з 4 елементів
#
# Розпакування і упакування

# Розпакування
# t = (1, 2)
# x, y = t #x = 1     y = 2
#
# t = (1,2,3,4, True)
# x, y, *z = t #x = 1  y = 2   z = [3, 4, True]

# t = (1,2,3,4, True)
# x, *y , z = t #x = 1  y = 2   z = [3, 4, True]
# print(y) #x = 1   y = [2, 3, 4]      z = Ture

# t = (1,2,3,4, True)
# x, y = t[1:3]

# thistuple = ('apple', 'banana', 'cherry')
# for i in thistuple:
#     print(i)

# thistuple = ("apple", "banana", 'cherry')
# for i in range(len(thistuple)):
#     print(thistuple[i])


#
# # Обеднання join
# t1 = (1,2,3)
# t2 = (5,6,7,8)
# t = t1 + t2 #(1, 2, 3, 5, 6, 7, 8)
# t1 = t1 + t2 + (0, ) #додавання в кінець додаткогового єлементу
#
# # Методи
# t1.index(5) #знайде індекс 5
# t1.count(5) #підрахуе кількість 5 в кортежі




# empty_tuple = ()
# subjects1 = ('Python', )
# subjects2 = ('C+', 'Java', 'HTML')
# print(empty_tuple, subjects1, subjects2)
# print(subjects2[-1])
#
# subjects = subjects1 + subjects2
#
# # додаемо в середину кортежа елемент
# mid = len(subjects) // 2
# subjects = subjects[:mid] + ("Python WEB", ) + subjects[mid:]
# print(subjects)
#
# # видалення
# del subjects1, subjects2
#
# # Виведіть отриманий кортеж, його довжину та тип даних в одному рядку за допомогою print.
# print(subjects, len(subjects), type(subjects))
#
# # 11. Виведіть елементи кортежа та їх індекси у окремому рядку, використавши цикл for
# for i in range(len(subjects)):
#     print(f'i = {i}, subjects[{i}] = {subjects[i]}')
#
# for i, item in enumerate (subjects):
#     print(f'i = {i+1}, subjects[{i}] = {item}')
#
# # fаналогічно
# for i, item in enumerate (subjects, 1):
#     print(f'i = {i}, subjects[{i}] = {item}')
#
# # 12. Виведіть зріз у кортежі, починаючи від 2 елементу і закінчуючи передостаннім включно.
# print(subjects[1:-2])
#
# # 13. Перевірте чи існує у кортежі предмет, у якого назва "Math"
# print('Math' in subjects)
#
# # 14. Перевірте чи існує у кортежі предмети, у якого назві яких присутня фраза "Python"
# for item in subjects:
#     if "Python" in item:
#         print(item)
#
# # аналогічно
# fil = tuple(item for item in subjects if 'th' in item.lower())
# print(*fil)
#
#
# # 14. Розпакуйте перші два предмети з кортежу subjects у змінні х та у, решта - кортежем у змінну z.
# x, y, *z = subjects
# print(x)
# print(y)
# print(tuple(z))
#
# # 15. Зробіть swap змінних х та у
# x, y = y, x
# print(x)
# print(y)

# Завдання 2
# Заданий список
# Ist = ['banana', 'apple', 'bananamango', 'mango', 'strawberry-banana'].

# lst = ['banana', 'apple', 'bananamango', 'mango', 'strawberry-banana']
# # Перетворити обернений список Ist у кортеж tpl.
# lst.reverse()
# tpl = tuple(lst)
# print(tpl)
#
# ['banana', 'apple', 'bananamango', 'mango', 'strawberry-banana']
# temp = [(item, len(item)) for item in tpl]
# print(temp)
#
# # Сформуйте список із кортежу temp, елементами якого є кортеж вигляду ("елемент у temp", його довжина).
# temp = [(item, len(item)) for item in tpl if len(item) == 5]
# print(temp)

# # Завдання 4
# # Задано дані у вигляді списку п=5 моделей автомобілів з їх вартістю, віком і тип (легковий або вантажний).
# # Використати представлення автомобіля як кортеж.
# # Скласти програму, яка визначає:
# # -середню вартість легкових автобілів.
# # -суму вартості легкових автобілів.
#
#
# cars = [(1500, 7, 'car'), (2000, 10, 'track'), (2500, 2, 'track'), (3000, 3, 'car'), (1000, 9, 'car'), ]
# s = 0
# count = 0
# for item in cars:
#     if item[2] == 'car': # 'car' in item:
#         s += item[0]
#         count += 1
#
# avg = s / count
# print(f'Середня ціна = {avg:.2f}')
#
# # генератор
# lst_price = [item[0] for item in cars if item[2] == 'car']
# print(lst_price)
# print(sum(lst_price) / len(lst_price))


# # # Множини set
# s = {1,2,3,3,5,3}
# print(s)
# s.add(10) #додасть елемент
# s.update((2,4,11)) #додать декілька елементів
# empty = set() #створення множини
# s.pop() #видаляе рандомний елемент
# s.remove(4)  #видаляе конкретний елемент, видае помилки, якщо даного елементу немае
# s.discard(4)  #видаляе конкретний елемент, але не видае помилки, якщо даного елементу немае
#
# print(s)


a = {3, 1, 7, 4}
b = {2, 8, 3, 1}
c = a | b  # {1, 2, 3, 4, 7, 8}
print(c)

v = a&b #{1, 3}
print(v)

c = b-a
d = a-b
print(c) #{8, 2}
print(d) #{4, 7}

l = b ^ a
m = a^b
print(l) #{2, 4, 7, 8}
print(m) # {2, 4, 7, 8}