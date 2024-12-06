#import random
g = int(input("ведите число от 3 до 20: ",))
mass = []
string = ''
#g = random.randint(3, 20)
for i in range(1, g+1):
    for j in range(i+1, g+1):
        if (i+j) == g or g % (i+j) == 0:
            mass.append(i)
            mass.append(j)
        else:
            continue
for el in range(len(mass)):
    string += str(mass[el])
print(string)
