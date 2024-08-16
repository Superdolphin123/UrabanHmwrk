import random
random_number = [i for i in range(3, 21)]
result = ''
number = random.choice(random_number)
for i in range(1, number):
    for j in range(1, number):
        if i+j > number:
            break
        if str(j) + ',' + str(i) in result or i == j:
            continue
        if number % (i+j) == 0:
            result += str(i) + ',' + str(j) + ' '
        else:
            continue
print(number)
print('Password: ', result.replace(',', ''))
