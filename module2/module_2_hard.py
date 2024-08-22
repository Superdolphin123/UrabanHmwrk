import random
random_number = list(range(3, 21))  # список возможных чисел
result = ''
number = random.choice(random_number)  # запоминаем случайное число
for i in range(1, number):
    for j in range(1, number):
        if i+j > number:  # проверка на превышение числа, чтобы не ходить по циклу лишний раз
            break
        if str(j) + ',' + str(i) in result or i == j:  # проверка на повторяющиеся пары.',' для определения пар
            continue
        if number % (i+j) == 0:
            result += str(i) + ',' + str(j) + ' '
            # записываем пары в виде строки 'число1,число2'. ' ' - пробел для читабельности
        else:
            continue
print(f'Password for number {number}:', result.replace(',', ''))  # удаляем лишние символы для читабельности
