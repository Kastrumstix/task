first = int(input("ВВедите первое число: "))
second = int(input("ВВедите второе число: "))
third = int(input("ВВедите третье число: "))
if first==second==third:
    print(3)
elif first==second or second==third or first==third:
    print(2)
else:
    print(0)