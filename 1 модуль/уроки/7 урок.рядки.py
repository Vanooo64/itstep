# st ='Python'
# p = st[0:6]
# p1 = st[0:5]
# p2 = st[:]
# p3 = st[::-1]
# print(id(p))
# print(id(p1))
# print(id(p2))
# print(p2)
# print(p3)
# st == st[::-1] #перевірка на паліндром
# print('y' in st)
# print('Pyt' in st)
# print('o' in st and 'y' in st)
# print('o' and 'k' in st)
# print('y' not in st)
# print(not ('y' in st))
# st1 ='Python cool!'
# print(st1.index('o')) #пошук першго індексу
# print(st1.find('o')) #пошук першго індексу, якщо індексу нема видае -1
# print(st1.rfind('o')) #пошук першго індексу c заду наперед, якщо індексу нема видае -1
# print(st1.count('o')) #рахуе кількість симвлів
# print(st1.capitalize()) #робить першу букву велику
# print(st1.title()) #робить першу букву першого слова велик
# print(st1.upper()) #всі великі букви
# print(st1.lower()) #всі маленькі
# print(st1.isalpha()) #Якщо всі букви - Ture
# print(st1.swapcase()) міняе великі букви на маленькі

# st2 = 'pythoncool'
# st_replace = st2.replace('o', 'x') #заміна символа на інший симвл
# print(st2,st_replace)

# st3 = '  pythoncool  '
# st3_strip = st3.strip() #видаляе пробыли с права ы злыва lstrip rstrip
# print(st3_strip)

# st4 = '1pyton1'
# print(st4.rstrip("1")) #видаляе 1 з права і зліва

# st5 = 'age = {}'
# age = 15
# st5.format(age)
# print(st5)
#
# print('name = {0}, age = {1}'.format("Petro", 18))
# print('name = {1}, age = {0}'.format("Petro", 18))
# print('name = {n}, age = {a}'.format(n='Petro', a=18))
# print('name = {n}, age = {a:.2f}'.format(n='Petro', a=18.435623))
# print('name = {n}, age = {a:10.2f}'.format(n='Petro', a=18.435623))
# print('name = {n}, age = {a:^10.2f}'.format(n='Petro', a=18.435623))

# # 0.1 task
# # P
# # y
# # t
# # h
# # o
# # n
# #
# # I
# # t
# # S
# # t
# # e
# # p
# # довжина
# # l = 13
# # P
# # y
# # t
# # h
# # o
# # n
# #
# # I
# # t
# # S
# # t
# # e
# # p
#
# st = "Python ItStep"
# for char in st:
#     print(char)
# l=len(st)
# print(f'довжина {l = }')
#
# for i in range(l):
#     print(st[i])

# st = "Python ItStep"
# for char in st:
#     print(char)
# l=len(st)
# print(f'довжина {l = }')
#
# for i in range(l):
#     if st[i] == 'I': # пошук індксу
#         print(f'index {i = }')

# # підраховуе кількість пробілів
# str = input('Введіть строку: ')
# co = str.count(" ")
# print(f' Кількість пробілів = {co}')

# 2 task
# st = input('Введіть строку: ').lower() #превід в нижній регістр
# count = st.count('a')
# id_left = st.find('a')
# id_right = st.rfind('a')
#
# if count == 0:
#     print('Букви нема у рядку')
# else:
#     print("count = {}, id_left = {}, id_right = {}".format(count,id_left,id_right))

# 3 task
st = input('Введіть строку: ').lower() #превід в нижній регістр
count = st.count('a')
id_left = st.find('a')
id_right = st.rfind('a')

if count == 0:
    print('Букви нема у рядку')
else:
    print("count = {}, id_left = {}, id_right = {}".format(count,id_left,id_right))

for i in range(len(st)):
    if st[i] == 'a':
        print(i, end=' ')

print()
# # інший спосіб
# id = -1
# for i in range(len(st)):
#     id = st.find('a', id+1)
#     if id == -1:
#         break
#     print(id, end=" ")

# 4 task вивести символи які зустрічаються найчастіше

# max_char = 0
# string = 'abc!abc!xyzbb!!aa'
# for char in string:
#     if string.count(char) > max_char:
#         max_char = string.count(char)
# print(max_char)
#
# unique_max_chars = ''
# for char in string:
#     if string.count(char) == max_char and char not in unique_max_chars:
#         print(char, end = " ")
#         unique_max_chars = unique_max_chars + char

# print(ord("F")) # вертае код
# print(chr(70)) # вертае символ
# print(ord("%"))
#
# print(ord('й'))
#
# print(hex(105500)) # перевід в 16-річну систему
# print(chr(128569))
# print(bin(12))  # перевід в 2-річну систему
# x = 0b1100
# print(x)

a = 'hello world'
b= a.un