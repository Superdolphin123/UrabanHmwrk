def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1,2,3])
values_list = [1, '1', False]
values_dict = {'a': 3, 'b': '3', 'c': [25]}
print_params(*values_list)
print_params(**values_dict)
values_list2 = [32, '32']
print_params(*values_list2, 42)