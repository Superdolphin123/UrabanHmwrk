def area_draw():
    for i in area:
        print(*i)


def win_checker():
    if area[0][0] == "X" and area[0][1] == "X" and area[0][2] == "X":
        return "X"
    if area[1][0] == "X" and area[1][1] == "X" and area[1][2] == "X":
        return "X"
    if area[2][0] == "X" and area[2][1] == "X" and area[2][2] == "X":
        return "X"
    if area[0][0] == "X" and area[1][0] == "X" and area[2][0] == "X":
        return "X"
    if area[0][1] == "X" and area[1][1] == "X" and area[2][1] == "X":
        return "X"
    if area[0][2] == "X" and area[1][2] == "X" and area[2][2] == "X":
        return "X"
    if area[0][0] == "X" and area[1][1] == "X" and area[2][2] == "X":
        return "X"
    if area[0][2] == "X" and area[1][1] == "X" and area[2][0] == "X":
        return "X"
    if area[0][0] == "0" and area[0][1] == "0" and area[0][2] == "0":
        return "0"
    if area[1][0] == "0" and area[1][1] == "0" and area[1][2] == "0":
        return "0"
    if area[2][0] == "0" and area[2][1] == "0" and area[2][2] == "0":
        return "0"
    if area[0][0] == "0" and area[1][0] == "0" and area[2][0] == "0":
        return "0"
    if area[0][1] == "0" and area[1][1] == "0" and area[2][1] == "0":
        return "0"
    if area[0][2] == "0" and area[1][2] == "0" and area[2][2] == "0":
        return "0"
    if area[0][0] == "0" and area[1][1] == "0" and area[2][2] == "0":
        return "0"
    if area[0][2] == "0" and area[1][1] == "0" and area[2][0] == "0":
        return "0"
    return "*"

area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print('Это игра в крестики нолики')
print('---------------------------')
area_draw()
for i in range(9):
    print(f'Ход: {i}')
    if i % 2 != 0:
        turn_char = '0'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        print('Ходят крестики')
    row = int(input('Строка: ')) - 1
    column = int(input('Столбец: ')) - 1
    if area[row][column] == '*':
        area[row][column] = turn_char
    else:
        print('Эта клетка уже занята, вы пропускаете ход')
        area_draw()
        continue
    area_draw()
    if win_checker() == turn_char:
        print('--------')
        print(f'Победили {turn_char}')
        break
    else:
        print('Ничья')