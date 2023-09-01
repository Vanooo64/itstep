# Завдання 2
# Маємо текстовий файл.
# •	Підрахуйте кількість рядків у ньому
# •	Підрахуйте кількість непорожніх рядків у ньому та виведіть їх.  (функція map)
# •	Підрахуйте кількість всіх символів у ньому.
# •	Підрахуйте кількість кожного символу у текстовому файлі без врахування регістру літер.
# •	Підрахуйте кількість слів, що починаються з символу, який задає користувач.
# Вхідні дані:
# Вхідний файл input.txt з вмістом
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.
#
# При відкритті обробіть виключення FileNotFoundError


with open('input.txt.py') as f:
    lines = list(f)  # •	Підрахуйте кількість рядків у ньому
    count_lines = len(lines)
    print(f'{count_lines}')

    f.seek(0)  # •	Підрахуйте кількість всіх символів у ньому.
    count_chars = len(list(f.read()))
    print(f'{count_chars=}')

    f.seek(0)  # •	Підрахуйте кількість всіх символів у ньому.
    text = f.read().lower()
    unique_chars = set(list(text)) #забирае повторні символи
    count_dict = {}
    for char in unique_chars:
        count_dict[char] = text.count(char) #зробить словник де буде підраховано кількість символів в тексті

    print(count_dict)
