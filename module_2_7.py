def print_params(a = 50, b = 'Сергей', c = True):
    print(a,b,c)
print_params()
print_params(b=25)
print_params(a=1,c=[1,2,3])

values_list = [15,'Питон', False]
print_params(*values_list)
values_dict = { 'a' : 20, 'b' : 'Карасев', 'c' : False }
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(values_list_2, 42)
