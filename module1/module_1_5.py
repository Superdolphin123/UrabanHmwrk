immutable_var = (1,'1',True)
print('Tuple:',immutable_var)
#2) immutable_var[0] = 2   'tuple' object does not support item assignment
mutable_list = [1,'1',True]
mutable_list[0] = mutable_list[1]
print('List:',mutable_list)