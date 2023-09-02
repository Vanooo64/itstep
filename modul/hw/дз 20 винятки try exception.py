# Завдання 1
# Напишіть програму, яка запитує у користувача ім'я та вік. Після отримання даних програма повинна виводити привітання
# у форматі: "Привіт, {ім'я}! Твій вік — {вік}". Обробіть виняток, що виникає при введенні некоректного віку
# (вік < 0 або вік > 130), і виведіть повідомлення про помилку.

while True:
    try:
        name = input("Введіть ім'я користувача: ")
        age = int(input('Введіть вік користувача від 0 до 130 років: '))

        if not name.isalpha():
            raise ValueError("Ім'я повинно містити лише букви!")

        if age < 0 or age > 130:
            raise ValueError ('Вік, який Ви вели некоректний, допустиме значення від 0 до 130 років!')

        print(f"Привіт, {name}. Твій вік — {age} років")
        break

    except ValueError as e:
        print(f'Помилка: {e}. Будь ласка, спробуйте ще раз.')


# Завдання 2
# Реалізуйте перше завдання через функцію. Функція повинна приймати ім'я і вік як параметри і повертати відформатований
# рядок. Створіть дві версії реалізації функції:
# •	Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
# •	Друга версія обробляє виняток усередині функції.

def get_name_age(name='Guast', age=30): # •	Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
    return (f"Привіт, {name}. Твій вік — {age} років")

while True:
    try:
        name = input("Введіть ім'я користувача: ")
        age = int(input('Введіть вік користувача від 0 до 130 років: '))
        get_name_age(name,age)

        if not name.isalpha():
            raise ValueError("Ім'я повинно містити лише букви!")

        if age < 0 or age > 130:
            raise ValueError ('Вік, який Ви вели некоректний, допустиме значення від 0 до 130 років!')

        print(f"Привіт, {name}. Твій вік — {age} років")
        break

    except ValueError as e:
        print(f'Помилка: {e}. Будь ласка, спробуйте ще раз.')


# •	Друга версія обробляє виняток усередині функції.
def get_name_age(name='Guast', age=30): # •	Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
    while True:
        try:
            name = input("Введіть ім'я користувача: ")
            age = int(input('Введіть вік користувача від 0 до 130 років: '))
            if not name.isalpha():
                raise ValueError("Ім'я повинно містити лише букви!")

            if age < 0 or age > 130:
                raise ValueError('Вік, який Ви вели некоректний, допустиме значення від 0 до 130 років!')

            return (f"Привіт, {name}. Твій вік — {age} років")
            break

        except ValueError as e:
            print(f'Помилка: {e}. Будь ласка, спробуйте ще раз.')

res = get_name_age()
print(res)

# Завдання 3
# Напишіть програму, яка дозволяє користувачеві ввести з клавіатури набір додатних (число більше нуля) чисел.
# Числа необхідно накопичувати у списку. Після отримання всіх значень програма повинна проаналізувати дані.
# У разі виявлення від'ємного значення або рядка програма має згенерувати виняток. Якщо всі значення у списку
# додатні, програма має повернути на екран суму всіх чисел списку.
# Згенерований виняток має бути оброблений кодом програми.

def invalid_data():
    while True:
        try:
            data = list(map(int, input('Введіть набір додатніх чисел більше нуля через пробіл: ').split()))

            for num in data:
                if num <= 0:
                    raise ValueError(f'У рядку виявлено число "{num}", допустимі тільки додатні значення')

            return data

        except ValueError as e:
            print(f'Помилка: {e}. Введіть коректний набір додатніх чисел.')


list_data = invalid_data()
sum_data = sum(list_data)
print(f'Введені дані: {list_data}')
print(f'Сума введених чисел: {sum_data}')

# Завдання 4
# Реалізуйте третє завдання через функцію. Функція повинна приймати список як аргумент і повертати суму елементів списку.
# Створіть дві версії реалізації функції:
# •	Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
# •	Друга версія обробляє виняток усередині функції.

def get_data(lst): # •	Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
    return sum(lst)

while True:
    try:
        data = list(map(int, input('Введіть набір додатніх чисел більше нуля через пробіл: ').split()))
        sum_data = get_data(data)

        for num in data:
            if num <= 0:
                raise ValueError(f'У рядку виявлено число "{num}", допустимі тільки додатні значення')

        print(f'Введені дані: {data}')
        print(f'Сума введених чисел: {sum_data}')

    except ValueError as e:
        print(f'Помилка: {e}. Введіть коректний набір додатніх чисел.')


def invalid_data(): # •	Друга версія обробляє виняток усередині функції.
    while True:
        try:
            data = list(map(int, input('Введіть набір додатніх чисел більше нуля через пробіл: ').split()))

            for num in data:
                if num <= 0:
                    raise ValueError(f'У рядку виявлено число "{num}", допустимі тільки додатні значення')

            return data

        except ValueError as e:
            print(f'Помилка: {e}. Введіть коректний набір додатніх чисел.')


list_data = invalid_data()
sum_data = sum(list_data)
print(f'Введені дані: {list_data}')
print(f'Сума введених чисел: {sum_data}')











