# first_digit = int(input('ведіть першу цифру: '))
# second_digit = int(input('ведіть другу цифру: '))
# third_digit = int(input('ведіть другу цифру: '))
# result = (first_digit * 100 + second_digit * 10 + third_digit)
# print(result)
#
# num = int(input('ведіть число: '))
# digit1 = num // 1000
# digit2 = num // 100 % 10
# digit3 = num // 10 % 10
# digit4 = num % 10
# result = digit1 * digit2 * digit3 * digit4
# print(f'результат добутку: {digit1}*{digit2}*{digit3}*{digit4}={result}')

# meters = int(input('Ведіть кількість метрів: '))
# centimeters = meters*100
# decentimeters = meters*10
# milimeters = meters*1000
# conversion_miles = 0.000621371
# miles = meters * conversion_miles
#
# print(f'\nРезультат у сантиметрах: {centimeters} \nРезультат у дециметрах: {decentimeters} \nРезультат у міліметрах: {milimeters} \nРезультат у милях:  {miles}')

# base_triangle = int(input('Ведіть основу трикутника: '))
# height_triangle = int(input('Ведіть висоту трикутника: '))
# area_triangle = (0.5*base_triangle)*height_triangle
# print(f'Площа трикутника = {area_triangle} метрів квадратних')

# number = int(input('Ведіть чотиризначне число: '))
# number4 = number%10
# number3 = number//10%10
# number2 = number//100%10
# number1 = number//1000
# print(f'{number4}{number3}{number2}{number1}')

# from math import sqrt, pi
#
# cat_a = int(input('Ведіть катет а: '))
# cat_b = int(input('Ведіть катет b: '))
# hypotenuse = sqrt(cat_a ** 2 + cat_b ** 2)
# perimeter = cat_a + cat_b + hypotenuse
# circuit = hypotenuse * pi
#
# print(f'Довжини гіпотенузи прямокутного трикутника = {int(hypotenuse)}')
# print(f'Периметр прямокутного трикутника = {int(perimeter)}')
# print(f'Довжину кола описаного навколо трикутника = {round(float(circuit), 1)}')

# from math import sqrt, log, fabs, e, sin, pi
# x = int(input('Ведіть число х: '))
# y = (log(fabs(x+0.05))/(sqrt(x+1)))+(5*x**3*e**(2+x))+(sin((3*x)+(pi/2)))
# print(f'Значення виразу = {round(y,2)}')

# n = int(input('Ведыть скільки секунд минуло з початку доби: '))
# hours = n // 3600
# minutes = (n % 3600) // 60
# seconds = (n % 3600) % 60

s = int(input())
f = '0' * (1 - s // 10) + str(s)
print(s)

f2 = f'{s//10}:{s%10}'
print(f2)