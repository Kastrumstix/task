my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
b = len(my_list)
while a < b or int(my_list[a]) < 0:
    if my_list[a]> 0:
        print(my_list[a])
        a=a+1
    elif int(my_list[a]) == 0:
        a=a+1
    else:
        break
