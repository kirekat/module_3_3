#1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    print()
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

#2
values_list = [4, 'e', False]
values_dict = {'a' : 1, 'b' : 'строка', 'c' : True}
print_params(*values_list)
print_params(**values_dict)

#3
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)