# #                               ДОМАШНЯ РОБОТА №39 ФАЙЛИ
#
# # Завдання 1.
# # Задайте два текстові файли. З’ясуйте, чи співпадають їхні рядки. Якщо ні, то виведіть із кожного файлу рядки, які не співпадають.
#
# with open('file1.txt', mode='w') as file1, open('file2.txt', mode='w') as file2:
#     text1 = """Головне
# управління
# розвідки
# Міноборони
# оприлюднило
# анонс
# документального
# фільму
# «Збиті льотчики Росії»"""
#     file1.write(text1)
#     text2 = """Головне
# управління
# Міноборони
# розвідки
# оприлюднило
# анонс
# документального
# фільму
# «Збиті льотчики Росії»"""
#     file2.write(text2)
#
#
# with open('file1.txt', mode='r') as open_file_1, open('file2.txt', mode='r') as open_file_2:
#     line1 = open_file_1.readlines()
#     line2 = open_file_2.readlines()
#
# for i, (line_file1, line_file2) in enumerate(zip(line1, line2), start=1):
#     if line_file1 != line_file2:
#         print(f"Не співпадае рядок {i}:")
#         print(f"У файлі 1 написано: {line_file1.strip()}")
#         print(f"У файлі 2 написано: {line_file2.strip()}")
#         print()
#
# # Завдання 2.
# # Задайте текстовий файл language.txt із таким вмістом:
# # 1. Python is an easy to learn, powerful programming language.
# # 2. It has efficient high-level data structures and a simple but effective approach to object-oriented programming.
# # 3. Python’s elegant syntax and dynamic typing, together with its interpreted nature,
# # make it an ideal language for scripting and rapid application development in many areas on most platforms.
# #
# # 4. The Python 3 interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python web site.
# # 5. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.
# #
# #
# # Створіть новий файл output_2.txt і запишіть до нього наступну статистику за вихідним файлом:
# # 1.	кількість символів;
# # 2.	кількість рядків;
# # 3.	кількість голосних літер;
# # 4.	кількість знаків пунктуації;
# # 5.	кількість цифр.
# # 6.	довжину і номер найдовшого рядка.
# # 7.	кількість слів Python
# import string
# with open('language.txt', mode='w') as file:
#     text = """1. Python is an easy to learn, powerful programming language.
# 2. It has efficient high-level data structures and a simple but effective approach to object-oriented programming.
# 3. Python’s elegant syntax and dynamic typing, together with its interpreted nature,
# make it an ideal language for scripting and rapid application development in many areas on most platforms.
#
# 4. The Python 3 interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python web site.
# 5. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.
#
# """
#     file.write(text)
#
# with open('output_2.txt', mode='w') as file_output_2_txt, open('language.txt', mode='r') as file_language_txt:
#     file_output_2_txt.write(f'Cтатистику за вихідним файлом {file_language_txt.name} \n')
#     read_text = file_language_txt.read()
#     # 1. Кількість символів
#     file_output_2_txt.write(f'1. Кількість символів = {len(read_text)} \n')
#     # 2. Кількість рядків
#     line_count = len(read_text.splitlines())
#     file_output_2_txt.write(f'2.	Кількість рядків = {line_count} \n')
#     # 3. Кількість голосних літер
#     vowels = 'aeiouAEIOU'
#     sum_vowls = [i for i in read_text if i in vowels]
#     file_output_2_txt.write(f'3. Кількість голосних літер = {len(sum_vowls)} \n')
#     # 4. Кількість знаків пунктуації;
#     punctuation = string.punctuation
#     sum_punctuation = [i for i in read_text if i in punctuation]
#     file_output_2_txt.write(f'4. Кількість знаків пунктуації = {len(sum_punctuation)} \n')
#     # 5. Кількість цифр
#     digit = [i for i in read_text if i.isdigit()]
#     file_output_2_txt.write(f'5. Кількість цифр = {len(digit)} \n')
#     # 6. Довжину і номер найдовшого рядка.
#     line = read_text.splitlines()
#     list_lens_line = [(num + 1, len(value)) for num, value in enumerate(line)]
#     list_lens_line.sort(key=lambda x: x[1])
#     num_len = list_lens_line[-1]
#     file_output_2_txt.write(f'6. Довжина найдовшого рядка = {num_len[1]} його номер - {num_len[0]} \n')
#     # 7. Кількість слів Python
#     python_word_count = read_text.lower().count("python")
#     file_output_2_txt.write(f'7. Кількість слів Python у тексті = {python_word_count}')
#
# # Завдання 3.
# # Маємо початковий текстовий файл language.txt із завдання 2.
# # Видаліть останній рядок і порожній рядок, поміняйте місцями 2 і 3 рядки. Результат запишіть до іншого файлу output_3.txt
#
# with open('language.txt', mode='r') as file_language_txt, open('output_3.txt', mode='w') as file_output_3_txt:
#     line = file_language_txt.readlines()
#
#     if len(line) >= 3:
#         line[1], line[2] = line[2], line[1]
#
#     non_empty_lines = [l for l in line if l.strip() != '']
#     file_output_3_txt.writelines(non_empty_lines)
#
# # Завдання 4.
# # Маємо масив  чисел
# # stock_prices = [190.64, 190.09, 192.25, 191.79, 194.45, 196.45, 196.45, 196.42,
# # 200.32, 200.32, 200.85, 199.2, 199.2, 199.2, 199.46, 201.46, 197.54, 201.12, 203.12, 203.12, 203.12, 202.83, 202.83, 203.36, 206.83, 204.9, 204.9, 204.9, 204.4, 204.06]
# #
# # 1.	Запишіть їх у новий файл list.txt, розташувавши кожен елемент масиву на окремому рядку із збереженням порядку.
# stock_prices = [190.64, 190.09, 192.25, 191.79, 194.45, 196.45, 196.45, 196.42,
# 200.32, 200.32, 200.85, 199.2, 199.2, 199.2, 199.46, 201.46, 197.54, 201.12, 203.12, 203.12, 203.12, 202.83, 202.83, 203.36, 206.83, 204.9, 204.9, 204.9, 204.4, 204.06]
#
# with open('list.txt', mode='w') as file:
#     for item in stock_prices:
#         file.write(str(item) + "\n")
#
# # 2.	Допишіть у цей файл в один рядок через пробіл числа відсортованого масиву  за зростанням.
# sorted_stock_prices = sorted(stock_prices)
# sorted_str = " ".join(map(str, sorted_stock_prices))
#
# with open('list.txt', mode='a') as file:
#     file.write(sorted_str)
#
#
# #                               ДОМАШНЯ РОБОТА №40 ФАЙЛИ
# # Завдання 1.
# # Задайте деякий текстовий файл.
# # На вхід програми через CLI задаються назва txt-файлу та два символи (використати sys.args).
# # Напишіть функцію, яка записує до іншого файлу всі рядки вхідного файлу, замінюючи в них перший символ  на другий символ,
# # і навпаки.
# import sys
# def character_replacement (variables):
#     try:
#         with open(variables[1], mode='r', encoding='utf8') as file, open('output_file.txt', mode='w', encoding='utf8') as new_file:
#             text = file.read()
#             new_text = ""
#             for char in text:
#                 if char == variables[2]:
#                     char = variables[3]
#                 elif char == variables[3]:
#                     char = variables[2]
#                 new_text += char
#             new_file.write(new_text)
#     except FileNotFoundError:
#         print(f"Файл {variables[1]} не знайдено")
#     else:
#         print("Операція проведена успішно, файл збережено")
#
# character_replacement(sys.argv)
#
# # Завдання 2.
# # Створіть деякий текстовий файл.
# # 1.	Зробіть  копіювання вмісту заданого текстового файлу в інший текстовий файл.
# # 2.	Перепишіть його рядки в інший файл, у якому порядок рядків має бути зворотним
# # до порядку рядків у заданому файлі. Здійсніть корегування останнього рядка - додати '\n', якщо потрібно.
#
# with open("news.txt", mode='r') as file, open ("news_copy.txt", mode='w+') as copy_file, open ("reverse_row_order.txt", mode='w') as reverse_row_order_file:
#     text = file.read()
#     copy_file.write(text)
#
#     lines = text.splitlines()
#     reversed_line = list(reversed(lines))
#     for line in reversed_line:
#         reverse_row_order_file.write(str(line))
#         reverse_row_order_file.write('\n')
#
# # Завдання 3.
# # У вхідному файлі записано цілі числа, які можуть бути розділені пропусками і кінцями рядків. Виведіть у вихідний файл їх суму.
#
# try:
#     with open("numbers.txt", mode="r") as numbers, open('sum_num.txt', mode="w") as sum_num:
#         num = numbers.read().split()
#         num = [int(num) for num in num]
#         sum_num.write(f'У файлі {numbers.name} присутні настуні числа: {num} їх сума = {sum(num)}')
# except FileNotFoundError:
#     print(f'Файл {numbers.name} не знайдено')
#
# # Завдання 4
# # Відомості про учня, записані у файлі input.txt, складаються з його прізвища і назви класу (рік навчання і буква без пропуску),
# # а також оцінок, отриманих за семестр, у форматі: Прізвище Клас Оцінки. Число оцінок в різних класах може бути різним.
# # Запишіть у файл output.txt прізвища тих учнів, середній бал яких більше, ніж 6.
#
# with open('student_evaluations.txt', mode='r') as student_file, open('sorted_student.txt', mode='w') as sorted_file:
#     student_data = student_file.read().splitlines()
#
#     student_list = [] # створюемо список списків [['Barnes', '9A', '4', '5', '7', '2', '3', '2'], ['Davidson', '10A', '7', '7', '5'], ['Clifford', '11B', '11', '10', '8', '9', '7'], ['Ramacey', '8A', '5', '6', '6', '5'], ['White', '7A', '8', '5', '5', '8', '9'], ['Porter', '11A', '11', '8'], ['Dean', '10B', '3', '4', '5', '4', '5'], ['Gate', '11A', '6', '5', '3', '4', '3', '5']]
#     for line in student_data:
#         values = line.split()
#         student_list.append(values)
#
#     dict_student = {} # створюемо словник {'Barnes': [4, 5, 7, 2, 3, 2], 'Davidson': [7, 7, 5], 'Clifford': [11, 10, 8, 9, 7], 'Ramacey': [5, 6, 6, 5], 'White': [8, 5, 5, 8, 9], 'Porter': [11, 8], 'Dean': [3, 4, 5, 4, 5], 'Gate': [6, 5, 3, 4, 3, 5]}
#     for row in student_list:
#         name = row[0]
#         values = row[2:]
#         dict_student[name] = [int(values) for values in values]
#
#     for key, value in dict_student.items():
#         avg = sum(value) / len(value)
#         if avg > 6:
#             sorted_file.write(key + '\n')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
