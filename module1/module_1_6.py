my_dict = {'Anton': 1, 'Gleb': 2, 'Petr': 3}
print(my_dict)
print(my_dict['Anton'])
print(my_dict.get('Lena'))
my_dict.update({'Denis': 5, 'Andrey': 6})
a = my_dict.pop('Anton')
print(a)
print(my_dict)

my_set = {0, 1, 1, 2, 2, 'Andrey', 'Andrey', False, False, True, True}
# True = int(1), False = int(0) ne pon
print(my_set)
my_newset = {4, 'Lena'}
my_set.update(my_newset)
my_set.remove(0)
print(my_set)
