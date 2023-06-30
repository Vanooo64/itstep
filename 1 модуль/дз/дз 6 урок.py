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

# 2 task
for i in range(1, 11):
    for j in range(1, 11):
        output = f'{j} * {i} = {i * j}'
        print(output, end='\t')
    print()

# # 3 task
# a = int(input('Введіть перше число діапазону: '))
# b = int(input('Введіть друге число діапазону: '))
# for i in range(1,11):
#     for j in range(a,b+1):
#         output = f'{j} * {i} = {i * j}'
#         print(output, end='\t')
#     print()

