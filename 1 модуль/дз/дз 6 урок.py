# https://github.com/Vanooo64/itstep

## 1 task
# a = int(input('Введіть перше число діапазону: '))
# b = int(input('Введіть друге число діапазону: '))
#
# for i in range(a, b + 1):
#     if i > 1:
#         prime = True
#         for j in range(2, i):
#             if i % j == 0:
#                 prime = False
#                 break
#         if prime:
#             print(i)

## 2 task
# for i in range(1, 11):
#     for j in range(1, 11):
#         output = f'{j} * {i} = {i * j}'
#         print(output, end='\t')
#     print()

## 3 task
# a = int(input('Введіть перше число діапазону: '))
# b = int(input('Введіть друге число діапазону: '))
# for i in range(1,11):
#     for j in range(a,b+1):
#         output = f'{j} * {i} = {i * j}'
#         print(output, end='\t')
#     print()

# 1 task
# password = '123'
# count = 0
# while True:
#     pas = input('Введіть пароль:')
#     count += 1
#
#     if pas != password:
#         print('Invalid password')
#
#     if pas == password:
#         print('Done')
#         break
#
#     if count == 5:
#         print('You have exceeded the maximum number of attempts')
#         break

# 2 task
n = int(input('Введіть кількість сходинок: '))
for i in range(1,n+1):
    output = (' '*(n-i) + '#'*i)
    print(output)
