x = int(input('Введите целое число:'))
y = int(input('Введите целое число:'))
z = int(input('Введите целое число:'))
if x == y and y == z:
    print(3)
elif x == y or y == z or z == x:
    print(2)
else:
    print(0)
    