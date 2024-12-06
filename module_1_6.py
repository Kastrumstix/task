my_dict = {'Михаил': 1997, 'Макс': 2003, 'Саша':2000}
print(my_dict)
print(my_dict.get('Михаил'))
print(my_dict.get('Квазимодо'))
my_dict['Антон'] = 1999
my_dict['Квазимодо'] = 2011
Del_value = my_dict.pop('Макс')
print('Удалено', Del_value)
print(my_dict.get('Макс'))
print(my_dict)

my_set = {1, 3, 'Яблоко', 42.314, 1}
print('Set: ', my_set)
my_set.add(23)
my_set.add(45)
my_set.discard(3)
print('Modified set: ', my_set)