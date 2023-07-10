# synbol = 'ш'
# code = ord(synbol)
# print(code)
# print(chr(68))

# print('A' < 'Z')
# print(ord('A'), ord('Z'))

# from pprint import pprint
# a = '''Извлекайте все изображения, содержащиеся
# в PDF или конвертируйте каждую страницу в файл JPG.'''
# pprint(a)

# txt = "Myname"
# print(txt[1:])
# print()
# for i in txt:
#     print(i)

# txt = ('Myname36'
#       '36'
#        'lksjdlkfjs'
#        )
# print(txt)
#
# print(txt[1:])
# print()
# for i in txt:
#     print(i)


# st = 'ItStep :к'
# l=len(st)
# st_encode = bytes(st, 'utf-8')
# l_bytes = len(st_encode)
# print(st_encode)
# print(f'довжина = {l} байтів = {l_bytes}')

# code = "U+10ffff" #Юныкод + запис в юнікоді 16-тковий
# code_clear = code.lstrip('U+')
# code_clear1 = code[2:]
# code_hex = int(code_clear, 16) #превід в 10-ткову систему
# char = chr(code_hex) #символьна система
#
# char1 = chr(int(code[:2], 16))
#
# print(code)
# print(code_clear)
# print(code_clear1)
# print(code_hex)
# print(char)
# print(char1)

# # 2 task
# st = input('Введіть рядок: ').lower()
# word = input('введіть слово: ').lower()
# count = st.count(word) #підрахунок скільки слово зустрічается у рядку
# print(f'Ваше слово "{word}" зустрічается {count} разів')

# 3 task
# import string
#
# st = "klsadfgj #@or0eur039534 ! 9029e0.,dj0w8ef34"
# my_punctuation = ',.-:!'
# count = 0
# count_punctuation = 0
# sum = 0
#
# for char in st:
#     if char.isdigit(): #підрахунок cуми і кількості цифр
#         count += 1
#         sum += int(char)
#     if char in my_punctuation: #string.punctuation #підрахунок знаків пунтуації
#         count_punctuation += 1
#
# print(count, sum, count_punctuation)

# # 4 task
# strng = 'kdjhxkjxxkkfdlkjglkdjflgkllllldlfkkdflllll'
# often_symbol = None
# max_symbol = 0
#
# for symbol in strng:
#     symbol_count = strng.count(symbol)
#     if symbol_count > max_symbol:
#         max_symbol = symbol_count
#         often_symbol = symbol
# print(f'Найчастыший символ: {often_symbol}, перше входження: {strng.find(often_symbol)}, останне входження: {strng.rfind(often_symbol)}')

# 4 task
# full_mane = input('Введыть імя та прізвище: ')
# year = input("Введыть рік наролдження: ")
# balance = 120.851788
# age = 2023 - int(year)
#
# print(f'Hello, {full_mane}')
# print(f"Your age is {age:010d}.") #d - интове число
# print(f'{age} in hex = {age:X}. {age} in bin {age:b} = {age}.') #{age:x} 16-тковий {age:b} бинарна система
# print(f'Balance={balance:10.2f}') #10 символів під це число, 2 знаки пысля коми f - тип float,  ^ - виривнювання по центру >виривнювання по правому
# print("Welcome".center(15,"*")) #додае зірочки з обох боків
#
# # аналогічно
# # проблеми - пробіли в імені, різні регістри
# # string.capwords( ) видалить пробыли
#
# template = f"""
#  Hello, {full_mane}
#  Your age is {age:10d}.
#  {age} in hex = {age:X}. {age} in bin {age:b} = {age}.
#  Balance ={balance:10.2f}
# """
# print(template, "Welcome".center(15,"*"), sep='\n')
# print()

# import string
# full_mane = input('Введыть імя та прізвище: ').strip()
# full_mane = string.capwords(full_mane)
# print(full_mane)


# Списки  - послыдовності, змінні,
# lst = []
# lst = list()
# lst = input("enter").split()

#cars = ['Alfa Romeo', 'Volvo', "BMW", "Ford",
#        'Toyota', 'Skoda']
# print(cars)
# print(cars[3])

# numbers = list(range(3,1000,3))
# print(numbers)

thislist = ['apple', 'banana', 'cherry']
thislist[1] = 'blaccurrant'
# print(thislist)

for x in thislist:
    print(x)
#
# for i in range(len(thislist)):
#     print()

# thislist.insert(1,'orage') #доасть на индекс додаткое слово
#
# tropical = ['mango', 'papaya']
# thislist.extend(tropical)  #доасть слово в кінець
# print(thislist)
# x=thislist.pop() #видаляе останій елемент і зберыгае в змынну
# thislist.pop(0) #видаляе елемент з вказаного індексу
# thislist.remove()  #видаляе останій елемен
# thislist.clear() #видаляе всі елементи списку
# thislist del #видаляе список
# print(thislist)

# cop = thislist.copy() #копия списку
# cop1 = thislist[::] #копия списку
#
# print(id(cop))
# print(id(cop1))
# print(id(thislist))


