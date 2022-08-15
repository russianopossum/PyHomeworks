# Task 1
from typing import List
class Matrix:
    def __init__(self, matrix_data: List[List]):
        self.__matrix = matrix_data
        m_rows = len(self.__matrix)
        self.__matrix_size = frozenset([(m_rows, len(row)) for row in self.__matrix])
        if len(self.__matrix_size) != 1:
            raise ValueError("Недопустимый размер матрицы")
    def __add__(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):
            raise TypeError(f"'{other.__class__.__name__}' "
                            f"Несовместимые объекты")
        if self.__matrix_size != other.__matrix_size:
            raise ValueError(f"Размеры матриц разные")
        result = []
        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])
        return Matrix(result)
    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])
if __name__ == '__main__':
    matrix1 = Matrix([[4, 6, 9], [8, 15, 3], [14, 6, 8]])
    print(matrix1, '\n')
    matrix2 = Matrix([[10, 2, 67], [30, 1, 18], [6, 7, 8]])
    print(matrix2, '\n')
    print(matrix1 + matrix2)

# Task 2
from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, param):
        self.param = param
    @abstractmethod
    def expense(self):
        pass
    def __str__(self):
        return str(self.param)
class Coat(Clothes):
    @property
    def expense(self):
        return self.param / 6.5 + 0.5
class Suit(Clothes):
    @property
    def expense(self):
        return ((self.param * 2 + 0.3) / 100)
a = Coat(46)
b = Suit(175)
print(a.expense)
print(b.expense)

# Task 3
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
    def __add__(self, other):
        return f'После сложения: {self.quantity + other.quantity} клеточек.'
    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'После вычитания: {sub} клеточек.' if sub > 0 else 'Что-то тут не так!'
    def __truediv__(self, other):
        return f'После деления нацело: {self.quantity // other.quantity} клеточек.'
    def __mul__(self, other):
        return f'После умножения: {self.quantity * other.quantity} клеточек.'
    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result
cell = Cell(10)
cell_2 = Cell(2)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(7))
