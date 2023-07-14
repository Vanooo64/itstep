
# # 1 task
# # Задається рядок. Якщо в ньому буква f зустрічається тільки один раз, виведіть її індекс.
# # Якщо вона зустрічається два і більше разів, виведіть індекс її першої і останньої появи.
# # Якщо буква f в цьому рядку не зустрічається, виводьте «Букви f нема в рядку».
#
# st = input('Введіть рядок: ')
#
# if st.count('f') == 1:
#     print(f'Індекс символу f = {st.index("f")}')
# if st.count('f') >= 2:
#     print(f'індекс першої появи символу f = {st.index("f")}, індекс останньої появи символу f = {st.rindex("f")}')
# else:
#     print('Букви f нема в рядку')

# # 2 task
# # Вводиться рядок тексту і рядок із деяких букв. Створіть програму для знаходження кількості цих
# # букв у даному тексті.

text = input('Введіть рядок: ')
symbols = input('Введіть симовли: ')

count = 0
for char in text:
    for char_s in symbols:
        if char == char_s:
            count+=1
print(count)

# text = 'Задається рядок. Якщо в ньому буква f зустрічається тільки один раз, виведіть її індекс.'
# symbols = 'абк'
#
# unique_symbol = ''
# for symbol in symbols:
#     if symbol not in unique_symbol:
#         unique_symbol += symbol
#
# count = 0
# for char_symbol in symbols:
#     count = count + text.count(char_symbol)
# print(count)



# print(f'Символ {symbol} зустрічаеться {st.count(symbol)} разів у введеному рядку')

# # 3 task
# # У заданому рядку символів визначити кількість слів та знайти найдовше слово. Слова
# # відділяються довільною кількістю пробілів, ком, крапок.
#
# st = 'У заданому рядку символів визначити кількість слів та знайти найдовше слов'.replace(",", "").replace(".", "")
#
# lst = st.split()
# print(len(lst))
#
# max_word = None
# max_len = 0
# for x in lst:
#     if len(x) > max_len:
#         max_len = len(x)
#         max_word = x
# print(max_word)

# print(f'Кількість слів у рядку = {len(lst)}')
# print(f'Найдовше слово у рядку - "{max(st,key = len)}", його довжина = {len(max(st,key = len))} символів')

# # 4 task
# # Задається рядок, який містить букви та *. Вивести слова, які містяться між зірочками.
# # Визначити мінімальну кількість "*" підряд у заданому рядку.
# # Наприклад, для рядка st = 'Hi**my****friend***Jack' максимальну кількість min_count = 2.

# st = 'Hi**my****friend***Jack'
# for words in st:
#     st_list = st.split()
# print(st_list)
#
# st1 = st.replace("**", "*")
# while '*' in st1:
#     st1 = st1.replace("*", " ")
#     st1 = st1.replace("  ", " ")
# print(st1)







# # 0 task
# # Розбити рядок 'E:/Folder/folder/ MyItems/bin' по '/' у список.
# # Із списку вивести папки, що починаються з малої букви або містять у назві букву «i».
# st = "E:/Folder/folder/ MyItems/bin".replace(' ', '')
# lis = st.split('/')
# lis1 = []
# for char in lis:
#     if char[0].islower():
#         lis1.append(char)
#     if 'i' and 'I' in char[:]:
#         lis1.append(char)
# lis1 = list(set(lis1))
# print(lis1)

# # 1 task
# # Користувач вводить з клавіатури арифметичний вираз.
# # Наприклад, 23+12.
# # Виведіть результат виразу на екран. У нашому прикладі 35.
# # Арифметичний вираз може складатися тільки з трьох частин: число, операція, число.
# # Можливі операції: +, -, *, /.
# lis = input('Введіть арифметичний вираз: ')
# if '+' in lis:
#     plus = list(lis.partition('+'))
#     result = int(plus[0]) + int(plus[2])
#     print(result)
# if '-' in lis:
#     minus = list(lis.partition('-'))
#     result = int(minus[0]) - int(minus[2])
#     print(result)
# if '*' in lis:
#     multiplication = list(lis.partition('*'))
#     result = int(multiplication[0]) * int(multiplication[2])
#     print(result)
# if '/' in lis:
#     divide = list(lis.partition('/'))
#     result = int(divide[0]) / int(divide[2])
#     print(result)

# # 2 task
# # Вводиться список цілих чисел в одному рядку через пропуск.
# # 1) Знайдіть кількість додатних елементів у введеному списку.
# # 2) Мінімальний та максимальний елементи (використати функції min та max )
# # 3) Cформуйте і виведіть новий список, в якому всі елементи початкового списку
# # піднесено до квадрату.
#
# lis = input("Введіть список цілих чисел через пропуск: ").split()
# integer_list = list(map(int, lis))
# count_positive = 0
# new_list = []
#
# for i in integer_list:
#     if i > 0:
#         count_positive += 1
#
# for i in integer_list:
#     new_list.append(i**2)
#
# print(f'Кількість додатних елементів у введеному списку: {count_positive}')
# print(f'Мінімальний елемент: {min(integer_list)}, Максимальний елемент: {max(integer_list)}')
# print(new_list)

# # 3 task
# # Сформуйте програмно список вигляду [3,8,13,...,58] за допомогою діапазону range.
# # Роздрукуйте лише ті елементи елементи списку, які діляться на 3.
#
# lis = []
# lis1 = []
# for i in range(3, 59, 5):
#     lis.append(i)
#
# for j in lis:
#     if j % 3 == 0:
#         lis1.append(j)
#
# print(lis1)


# lst = list(range (3,29,5))
# print(lst)

# lst = [1, 7, 12, 3]
# lst.append(5)
# lst.extend([57,8]) #додати в кінець списка декілька символів
# print(lst)
