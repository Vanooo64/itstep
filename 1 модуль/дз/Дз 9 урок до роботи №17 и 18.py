# # Завдання 1.
# # Два списки цілих заповнюються випадковими числами.
# # Сформуйте третій список, який містить:
# # 1. ■ елементи обох списків;
# # 2. ■ елементи, спільні для двох списків;
# # 3. ■ тільки унікальні елементи кожного зі списків;
# # 4. ■ тільки мінімальне та максимальне значення кожного зі списків
#
# from random import randint, seed
# seed(3)
# n = 10
#
# lis1 = [randint(1,100) for _ in range(n)]
# lis2 = [randint(1,100) for _ in range(n)]
# lis3 = lis1+lis2
# print(f'Елементи обох списків: {lis3}') # 1. ■ елементи обох списків;
#
# lis4 = [] # 2. ■ елементи, спільні для двох списків;
# for i in lis1:
#     for j in lis2:
#         if i==j:
#             lis4.append(i)
# print(f'Елементи, спільні для двох списків: {lis4}')
#
# unique_list1 = [] # 3. ■ тільки унікальні елементи кожного зі списків;
# unique_list2 = []
# for i in lis1:
#     if i not in lis2:
#         unique_list1.append(i)
# for j in lis2:
#     if j not in lis1:
#         unique_list2.append(j)
# print(f'Tільки унікальні елементи першого списку: {unique_list1}')
# print(f'Tільки унікальні елементи другого списку: {unique_list2}')
#
# #■ тільки мінімальне та максимальне значення кожного зі списків
# print(f'''Mінімальне значення першого списку: {min(lis1)}
# Максимальне значення списку першого списку: {max(lis1)}''')
# print(f'''Mінімальне значення другого списку: {min(lis2)}
# Максимальне значення списку другого списку: {max(lis2)}''')

# 2 task

# data = """Om Bhakta male 26 Mar 1976 1707.0
# Krishnin Kakar male 18 Apr 2011 2482.33333
# Neela Tara female 27 Apr 1995 529.33333
# Ajit Pandya male 21 Aug 2001 1231.33333
# Kavita Goda female 25 Jan 1986 1281.33333
# Avinash Tata male 20 Sep 2004 2767.0
# Narinder Raval male 23 Dec 2019 2309.66667"""
# lis = data.split('\n')
# lis1 = [i.split() for i in lis]
# full_name, gender, age, balance  = [], [], [], []
#
# for j in lis1:
#     list_full_nam = j[0], j[1].upper()
#     full_name.append(list_full_nam)
#     gende = j[2].capitalize()
#     gender.append(gende)
#     a = 2023 - int(j[5])
#     age.append(a)
#     bal = round(float(j[6]),2)
#     balance.append(bal)
#
# print('{full_name}|{gender}|{age}|balance'.format(full_name='full_name'.center(20,'*'), gender='gender'.center(10,'#'), age="age".center(5,"-")) )
# for i in range(len(full_name)):
#     print('{full_name}|{gender}|{age}|{balance}'.format(
#         full_name=('{first} {last}'.format(first=full_name[i][0], last=full_name[i][1])).ljust(20),
#         gender=gender[i].center(10),
#         age=str(age[i]).center(5),
#         balance=str(balance[i])
#     ))

# for i in range(len(full_name)):
#     full_name =
#     print(f"{full_name:20s}|{gender.capitalize():^10s}|{age:+5d}|{balance:6.2f}")

#
# print(full_name)
# print(gender)
# print(age)
# print(balance)
# #
#


# task 1
# Cписок цілих розміру n заповнюється випадковими числами від -10 до 10.
# Розрахуйте:
# ■ Добуток від’ємних чисел, що діляться на 2.
# ■ Суму елементів з індексами, кратними 3.
# ■ Суму елементів, що знаходяться між першим та останнім від’ємним елементом.

# from random import randint, seed
#
# seed(40)
# n = 10
# lst = [randint(-10, 10) for i in range(n)]
# print(lst)
#
# # Добуток від’ємних чисел, що діляться на 2.
# lst1 = [i for i in lst if i < 0 and i % 2 == 0] #від’ємних чисел, що діляться на 2
# product = 1 # Добуток від’ємних чисел, що діляться на 2.
# for j in lst1:
#     product*= j
# print(f'Добуток від’ємних чисел, що діляться на 2 = {product}')
#
#
# # Сума елементів з індексами, кратними 3.
# s = 0
# for i in range(0, n, 3):
#     # print('----', i, lst[i])
#     s = s + lst[i]
# print(f'Сума елементів з індексами, кратними 3 = {s}')
#
#
# # ■ Суму елементів між мінімальним та максимальним елементом.
# s1 = 0
# m = min(lst)
# M = max(lst)
# for i in lst:
#     if i == m:
#         s1+=i
#         if i == M:
#             break
# print(f"Суму елементів між мінімальним та максимальним елементом = {s1}")
#
#
# # Суму елементів, що знаходяться між першим та останнім від’ємним елементом.
# first_visible_element = None
# for i in lst:
#     if i < 0:
#         first_visible_element = i
#         index_first = lst.index(first_visible_element)
#         break
#
# last_visible_element = None
# for i in range(len(lst) - 1, -1, -1):
#     if lst[i] < 0:
#         last_visible_element = lst[i]
#         index_last = lst.index(last_visible_element)
#         break
#
# print(f'Сума елементів, що знаходяться між першим та останнім від’ємним елементом = {sum(lst[index_first:index_last+1])}')

# task 2
# Cписок цілих чисел вводиться через пробіл (розмір списку зазвичай кратний числу 3).
# Відсортуйте перші дві третини списку в порядку зростання, якщо середнє арифметичне всіх
# елементів більше за нуль; якщо ні — тільки першу третину. Решту списку не сортуйте, а
# розташуйте у зворотному порядку.

# input_list = list(map(int, input('Введіть список цілих чисел через пробіл: ').split()))
# avg = sum(input_list) / len(input_list)
#
# index_1 = len(input_list) // 3
# index_2 = index_1 * 2
#
# part1 = input_list[:index_1]
# part2 = input_list[index_1:index_2]
# part3 = input_list[index_2:]
# part1_2 = part1 + part2
# part2_3 = part2 + part3
#
# # 7 3 42 9 5 -1 2 4 19 тест
# if avg > 0: #Відсортуйте перші дві третини списку в порядку зростання, якщо середнє арифметичне всіх елементів більше за нуль;
#     sorted_part1_2 = sorted(part1_2)
#     reversed_sorted_list3 = sorted(part3, reverse=True)
#     change_list_2_3 = sorted_part1_2 + reversed_sorted_list3
#     print(f'Відсортовані перші дві третини списку в порядку зростання: {change_list_2_3}')
#
# # -4 -3 -5 -2 4 -5 -19 3 14 тест
# if avg < 0: #якщо ні — тільки першу третину. Решту списку не сортуйте, а розташуйте у зворотному порядку.
#     sorted_part1 = sorted(part1)
#     reversed_sorted_list2_3 = sorted(part2_3, reverse=True)
#     change_list_3_2 = sorted_part1 + reversed_sorted_list2_3
#     print(f'Відсортовані перша третина списку в порядку зростання: {change_list_3_2}')

# 3 task
# Написати програму «Успішність». Користувач вводить 10 оцінок студента. Оцінки від 1 до
# 12. Реалізуйте меню для користувача:
# ■ виведення оцінок (виведення вмісту списку);
# ■ перескладання іспиту (користувач вводить номер елемента списку та нову оцінку);
# ■ отримання стипендії (стипендію отримують, якщо середній бал не нижче 10.7);
# ■ виведення відсортованого списку оцінок: за зростанням або спаданням

print('          *****«Успішність»*****     ')
print()
assessment = list(map(int, input('Введіть 10 оцінок студента. Оцінки від 1 до 12: ').split()))
print()
print('''          *****Виберіть операцію*****
1 - виведення оцінок (виведення вмісту списку);
2 - перескладання іспиту (користувач вводить номер елемента списку та нову оцінку);
3 - отримання стипендії (стипендію отримують, якщо середній бал не нижче 10.7);
4 - виведення відсортованого списку оцінок: за зростанням або спаданням''')
print()
result_selection = int(input('Виберіть операцію, цифру від 1 до 4: '))
print()
gpa = (sum(assessment) / len(assessment))
sort_assessment = None

if result_selection == 1:
    for i in range(len(assessment)):
        print(f'{i + 1} оцінка студента: {assessment[i]}')

if result_selection == 2:
    print()
    num_element = int(input('Введіть номер елемента списку: '))
    new_assessment = int(input('Введіть нову оцнку: '))
    print()
    assessment[num_element - 1] = new_assessment
    print('*****Відкорегованний список оцінок*****')
    for i in range(len(assessment)):
        print(f'{i + 1} оцінка студента: {assessment[i]}')

if result_selection == 3:
    if gpa >= 10.7:
        print(f'Ви отримаете стипендію, Ваш середній бал: {round(gpa, 2)}')
    else:
        print(f'Ви не отримаете стипендію, Ваш середній бал: {round(gpa, 2)}')

if result_selection == 4:
    print('Для сортування списку оцінок за зростанням натисніть 1'
          'введіть 2 для ортування списку оцінок за спаданням')
    sort = int(input('Введіть 1 або 2: '))
    print()
    if sort == 1:
        sort_assessment = sorted(assessment)
        print(f"Відсортованний список оцінок за зростанням: {sort_assessment}")

    if sort == 2:
        sort_assessment = sorted(assessment,reverse=True)
        print(f"Відсортованний список оцінок за спаданням: {sort_assessment}")





