# https://github.com/Vanooo64/itstep/blob/main/1%20%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C/%D0%B4%D0%B7/%D0%B4%D0%B7%207%20%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%8F%20%D1%80%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%D0%B4%D0%BE%20%D0%B7%D0%B0%D0%BD%D1%8F%D1%82%D1%82%D1%8F%20%E2%84%96%2013%20%D0%A2%D0%B5%D0%BC%D0%B0%20%D0%A0%D1%8F%D0%B4%D0%BA%D0%B8.py

# # 1 task
# # Заданий рядок «Я зараз вивчаю Python». Добавити в кінець до заданого рядка деякий смайлик,
# # наприклад з кодом 128522. Далі провести кодування і декодування отриманого рядка, вибравши
# # на свій вибір кодування (наприклад, utf-8, utf-16, utf-32).
#
# st = "Я зараз вивчаю Python"
# st1 = st + chr(128522)
# st2 = st1.encode('utf-8')
# st3 = st2.decode()
# print(st1)
# print(st2)
# print(st3)

# # 2 task
# string = 'abcdefghijklmnopqrstuvwxyz'
# print(string) # 1 Виведення всього рядку
# print(string[0]) # 2 Виведення першого символу рядку
# print(string[1]) # 3 Виведення другого символу рядку
# print(string[-1]) # 4 Виведення останнього символу рядку
# print(string[-2]) # 5 Виведення передостаннього символу рядку
# print(string[2:5]) # 6 Виведення символів починаючи з 3-го індексу до 5-го
# print(string[2:]) # 7 Виведення рядку починаючи з 3-го символу
# print(string[:]) # 8 Виведення послідовності від початку до кінця
# print(string[20:]) # 9 Всі символи, починаючи з 20-го і до кінця
# print(string[-3:]) # 10 Останні три символи
# print(string[17:2:-1]) # 11 Починаючи з 18-го і закінчуючи 4 з кінця включно
# print(string[2::3]) # 12 Кожен третій символ з початку до кінця
# print(string[3::3]) # 13 Кожен 3 символ, починаючи з 4 та закінчуючи передостаннім включно
# print(string[::-1]) # 14 Перевернути рядок

# # 3 task
# strng = " а, б, в, г, ґ, д, е, є, ж, з, и, і, ї, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ь, ю, я "
# strng_bytes = bytes(strng, 'utf-8') #Перевести strng у байтовий рядок strng_bytes за допомогою функції bytes
# print(strng_bytes)
# strng_bytes1 = strng.replace(',', '').replace(' ', '') #Видалити із заданого рядка strng коми та пробіли.
# l = len(strng_bytes1) #Визначити довжину отриманого рядка
# audit = str('клм') in strng_bytes1 #Перевірити чи підрядок "клм" міститься у рядку
# print(f'Індекс входження підрядка "клм" {strng_bytes1.index("клм")}') #вивести індекс входження цього підрядка
# up = strng_bytes1.upper() #Перевести отриманий рядок у верхній регістр.
#
# for char in range(len(up)): # пройтись циклом по кожному символу рядка та надрукувати у форматі:
#      print(f'Номер ітерації = {char}, Символ = {up[char]}, код символу = {ord(up[char])}')

# 1 task
# st = input('Введіть рядок для перевірки на паліндром: ')
# st1 = st.replace(" ", '').lower()
# if st1 == st1[::-1]:
#     print(f'Рядок "{st}" являеться паліндромом')
# else:
#     print(f'Рядок "{st}" неявляеться паліндромом')

# # 2 task
# text = input('Введіть текст: ')
# word = input('Введіть слово: ')
# text1 = text.replace(word, word.upper())
# print(text1)

# 3 task
# Користувач вводить з клавіатури рядок.
# Підрахуйте кількість всіх шістнадцяткових цифр у рядку.
# Підрахуйте кількість знаків пунктуації у рядку.
# Для виконання завдання можна використати модуль string

import string
text = input('Введіть рядок: ')
hex_count = 0
punctuation_marks = 0

for char in text:
    if char.lower() in string.hexdigits:
        hex_count+=1
    if char in string.punctuation:
        punctuation_marks+=1

print("Кількість шістнадцяткових цифр:", hex_count)
print(f'Кількість знаків пунктуації: {punctuation_marks}')
