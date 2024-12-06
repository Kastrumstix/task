class Figure:
    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = False

        if len(sides) == self.sides_count:
            self.set_sides(*sides)
        else:
            self.__sides = [1] * self.sides_count  # Заполняем единицами

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)  # Периметр для многогранников

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.__radius = sides[0]
        else:
            self.__radius = 1  # По умолчанию радиус равен 1

    def get_square(self):
        return 3.14159 * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 3:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * 3  # По умолчанию стороны равны 1

    def get_square(self):
        a, b, c = self.__sides
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length=1):
        super().__init__(color)
        self.set_sides(*([side_length] * Cube.sides_count))

    def get_volume(self):
        side_length = self.get_sides()[0]  # Все стороны одинаковы
        return side_length ** 3

# Проверка кода
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())     # Вывод: [55, 66, 77]
cube1.set_color(300, 70, 15)   # Не изменится
print(cube1.get_color())       # Вывод: [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())       # Вывод: [6]*12
circle1.set_sides(15)           # Изменится
print(circle1.get_sides())      # Вывод: [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))             # Вывод: длина окружности равна радиусу (15)

# Проверка объёма (куба):
print(cube1.get_volume())       # Вывод: объем куба равен стороне в кубе (6^3=216)