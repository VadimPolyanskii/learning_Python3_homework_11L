import random


class NumberCalculation:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 1. Метод вывода
    def __str__(self):
        return f'Values x, y: {self.x}, {self.y}'

    # 2. Метод сложения
    def __add__(self, other):
        return NumberCalculation(self.x + other.x, self.y + other.y)

    # 3. Метод сравнения (перегрузка знака =)
    def __eq__(self, other):
        return (self.x == other.x) & (self.y == other.y)

    # 4. Метод перегрузки знака <
    def __lt__(self, other):
        return self.x < self.y

    # 5. Метод умножения
    def __mul__(self, other):
        return NumberCalculation(self.x * other.x, self.y * other.y)


if __name__ == '__main__':
    obj1 = NumberCalculation(1, 5)
    obj2 = NumberCalculation(1, 7)
    print(obj1 == obj2)
    print(obj1 < obj2)
    print(obj1 + obj2)
    print(obj1 * obj2)
