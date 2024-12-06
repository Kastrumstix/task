grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_list = sorted(list(students))
grades_sr = [sum(sub_list) / len(sub_list) for sub_list in grades]
slovar = dict(zip(my_list, grades_sr))
print(slovar)
