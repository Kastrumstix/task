import math

# a = [1,2,-3,-4,5,-6, 11]
# b =0
# for i in a:
#     if i>0 and i<10:
#         b += int(a[i-1])
# print(b)
#a = "asdfghjkl"
# for i in a[::-1]:
#     print(i)
# a = {"123": 2,
#      "456": 3,
#      "789": 4}
# print(sum(x**2 for x in a.values()))
#a = 123456
# b = list(str(a))
# print(b)
# print(sum(int(x) for x in list(str(a))))
# a = [1, 2, 3, 4, 5, 6]
# for i in range(len(a)):
#     a[i] += (a[i]/100)*10
# print(a)
# print(a[-3:])
# for i in a:
#     a[i]=a[i]*2
# print(a)
#print(str(a)[::-1])
# a = ["ashg", "sdfsdg.html", ".htmlfhjhg", "dtwe65.html"]
# # for i in range(len(a)-1):
# #     if not a[i].find(".html"):
# #         del a[i]
# a = [i for i in a if i.endswith(".html")]
# print(a)
# a = "ghf0d4r"
# print(a.find("0"))
#
# print(a.replace('g', ''))
# print(a)
# for i in range(10, 1000):
#     if (int((str(i))[0]))+(int((str(i))[1]))== 5:
#         print(i)
# a = 'abcdeabc'
# print("".join(sorted(list(set(a)))))
# b=0
# for i in range(len(a)):
#     if a[i]<0:
#         b+=1
# print(b)

# print(list(x for x in a if x>0))

# a = [1.456, 2.125, 3.32, 4.1, 5.34]
# a = [round(i,1) for i in a]
# print(a)
# a = {'a': 1,
#      'b': 2,
#      'c': 3,
#      'd': 4, }
# b=list(a.values())
# print(b)
# a = "asdfgh"
# b = "fghjaa"
# c = a[0] == b[len(b)-1]
# print(c)
# a = "0140101"
# caunt =0
# for i in range(len(a)-1):
#     if a[i] =="0":
#         caunt +=1
#         if caunt ==3:
#             print(i+1)
# a = '12,34,56'
# a_list = a.split(",")
# print(sum(map(int, a_list)))
# a = '2025-12-31'
# dict_a = {key: value for key, value in zip(['year', 'month', 'day'], a.split("-"))}
# # print(dict_a)
# a = {'a': 1,
#      'b': 2,
#      'c': 3,
#      'd': 4,}
# print(set(a.values()))
# a = 'ss1df7sdf'
# for i in range(len(a)):
#     if a[i].isdigit():
#         print(i+1)
#         break
# a = 346178
# b = str(a)
# c = 0
# for i in range(len(b)):
#     if int(b[i]) % 2 == 0:
#         c +=1
# print(c)
# a = {'a': 1,
#      'b': 2,
#      'c': 3,
#      'd': 4,}
# print(list(a.keys()))
# a = 'asdfg'
# b = ''
# for i in range(len(a)):
#     if i%2 == 0:
#         print(a[i])
#         b += a[i].upper()
#     else:
#         b+=a[i]
# print(b)
# new = ''.join([c.upper() if i % 2 == 0 else c.lower() for i,c in enumerate(a)])
#
# print(new)
# a = "aaa bbb ccc"
# b=""
# for i in range(len(a)):
#     if a[i-1] == " " or i == 0:
#         b += a[i].upper()
#     else:
#         b+=a[i]
#
# print(b)
# a = '2025-12-31'
# b =()
# b = a.split('-')[::-1]
# print(tuple(b))
# a = "023m0df0dfg0"
# b = {i for i, x in enumerate(a) if x == '0'}
# print(b)
# b = {i for i, x in enumerate(a) if x == '0'}
# a ='abcdefg'
# b=""
# for i,x in enumerate(a):
#     if (i+1)%3 !=0:
#         b+=a[i]
# print(b)
# a = [1, 2, 3, 4, 5, 6]
# b = sum(x for i,x in enumerate(a) if (i+1)%2 != 0)
# c = sum(x for i,x in enumerate(a) if (i+1)%2 == 0)
# print(round(c/b, 2))
# a = ['2025', '12', '31']
# b=(a[2], a[1], a[0])
# print(b)
# a = 'f3g3j65'
# b = list(i for i,x in enumerate(a) if x.isdigit())
# print(b)
# a = 'AbCdE'
# print(a.swapcase())
# a = [1,2,3,4,5,6]
# print(list(int(str(a[i])+str(a[i+1])) for i in range(0, len(a), 2)))
# a = 'aaa bbb ccc eee fff'
# print(' '.join(a.capitalize() if i % 2 == 1 else a for i, a in enumerate(a.split())))
# a =input()
# if a.isupper():
#     print('up')
# elif a.islower():
#     print('down')
# else:
#     print('Fuck')
# a = 123789
# b = ''.join(x for x in str(a) if int(x) % 2 == 0)
# print(b)
# a = ('2025', '12', '31')
# dict_a = {key: value for key, value in zip(['year', 'month', 'day'], a)}
# print(dict_a)
# print(list(x+1 for x in range(10)))
def check_uppercase_limit(s):
    # Генераторное выражение для подсчета заглавных букв
    uppercase_count = sum(1 for char in s if char.isupper())
    return uppercase_count <= 2

# Пример использования
input_string = "Пример Строки"
result = check_uppercase_limit(input_string)

if result:
    print("В строке не более двух заглавных букв.")
else:
    print("В строке больше двух заглавных букв.")