# ####1
print("Task 1: Matrix \n---------\n")

class Matrix():
    def __init__(self, matrix):
        self.matrx = matrix

    def __str__(self):
        strtt = ''
        for el in self.matrx:
            strt = ''
            for item in el:
                strt += str(item) + ' '
            strtt += strt  +  '\n'
        return (f'{strtt.strip()}')

    def __add__(self, other):
        print('Был вызыван метод __add__')
        if isinstance(other, Matrix):

            if(len(self.matrx) != len(other.matrx)):
                print('You can not add matrices with different range')
            else:
                print('Размерность матриц =',len(self.matrx))
                str_add_full_matrix = ''
                for i in range(0, len(self.matrx)):
                    str_add_line_matrix = ''
                    for j in range(0, len(self.matrx[i])):
                        str_add_line_matrix += str(int(self.matrx[i][j]) + int(other.matrx[i][j])) + ' '
                    str_add_full_matrix += str_add_line_matrix + '\n'
            return str_add_full_matrix


a = [31, 22]
matrix_1 = [[31, 22], [37, 43], [51, 86]]
matrix_2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
matrix_3 = [[3, 5, 8, 3], [8, 3, 7, 1]]
matrix_4 = [[1, 2], [3, 4], [5, 6]]


mx1 = Matrix(matrix_1)
mx2 = Matrix(matrix_2)
mx3 = Matrix(matrix_3)
mx4 = Matrix(matrix_4)
#
# for i in range(0,3):
#     print(f'Пример матрицы {i}:')
#     print(mx{i})

print('Пример матрицы 1:')
print(mx1)
print('Пример матрицы 2:')
print(mx2)
print('Пример матрицы 3:')
print(mx3)
print('Пример матрицы 4:')
print(mx4)
print("Пример суммирования матриц")

print(mx1 + mx4)



#####2
line = "=" * 150
print(line)
print("Task 2: Clothes  \n---------\n")

from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, name: str):
        self.name = name

    @property
    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):

    i = 0
    list_coats = []

    def __init__(self, name, size):
        super().__init__(name)
        self.v = size
        Coat.list_coats.append(self.consumption)

    @property
    def size(self):
        return self.__v

    @size.setter
    def v(self, size):
        if size < 38:
            self.__v = 38
        elif size > 52:
            self.__v = 52
        else:
            self.__v = size

    @property
    def consumption(self):
        return round(self.v / 6.5 + 0.5, 2)

    def __str__(self):
        Coat.i += 1
        return f'Количество ткани на пальто {self.name} под номером {Coat.i} : {self.consumption}'

    # def __add__(self, other):
    #     return Clothes.__add__(self.consump, other.consump)
    # def __add__(self, other):
    #     return self.consumption + other.consumption

class Suit(Clothes):

    j = 0
    list_suits = []

    def __init__(self, name, height):
        super().__init__(name)
        self.h = height

        Suit.list_suits.append(self.consumption)

    @property
    def height(self):
        return self.__h

    @height.setter
    def h(self, height):
        if height < 150:
            self.__h = 150
        elif height > 200:
            self.__h = 200
        else:
            self.__h = height

    @property
    def consumption(self):
        return round((2 * self.h) + 0.3, 2)

    def __str__(self):
        Suit.j += 1
        return f'Количество ткани на костюм {self.name} под номером {Suit.j}: {self.consumption}'

    # def __add__(self, other):
    #     return Suit(self.consumption + other.consumption)


# coats
coat1 = Coat('Coat X', 38)
coat2 = Coat('Coat Y', 52)
coat3 = Coat('Coat Z', 45)
print(coat1)
print(coat2)
print(coat3)
add_coats = round(sum([coat for coat in Coat.list_coats]), 2)
print('Общее количество ткани на все пальто:', add_coats)
#suits
suit1 = Suit('Suit A', 150)
suit2 = Suit('Suit B', 172)
suit3 = Suit('Suit C', 200)
print(suit1)
print(suit2)
print(suit3)
add_suits = round(sum([suit for suit in Suit.list_suits]), 2)
print('Общее количество ткани на все костюмы:', add_suits)
print('Итого требуется ткани:', add_coats + add_suits)

######3

line = "=" * 150
print(line)
print("Task 3: Cells  \n---------\n")

class Cell():
    def __init__(self,  quantity):
        # self.name = name
        self.quantity = quantity

    def __str__(self):
        return f'Результат операции {self.quantity}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return Cell(self.quantity - other.quantity)
        else:
            return f'Количество ячеек в клетке равно или меньше нуля, поэтому операция не может быть выполнена'

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        # return Cell(int(self.quantity // other.quantity))
        try:
            return Cell(int(self.quantity//other.quantity))
        except ZeroDivisionError:
            return f'Поделить на клетку без ячеек нельзя'
        except AttributeError:
            return f'Поделить на клетку без ячеек нельзя'

    def make_order(self, cells_in_row):
        a = int(self.quantity) // cells_in_row
        b = int(self.quantity) % cells_in_row
        print(f"{'*'* cells_in_row} \n" * a + '*' * b)

cell1 = Cell(44)
cell2 = Cell(2)
print(cell1)

print(cell1 + cell2)
print(cell2 - cell1)

cell3 = Cell(44)

print(cell3 - cell1)
print(cell1 - cell2)

print(cell3 * cell1)

print(cell3 / cell1)
print(cell3 / cell2)

cell0 = Cell(0)
print(cell3/cell0)
# try:
# #     print(cell3/cell0)
# except ZeroDivisionError:
#     print('Поделить на клетку без ячеек нельзя')
# except AttributeError:
#     print('Поделить на клетку без ячеек нельзя')

cell0 = None
print(cell3/cell0)
# try:
#     print(cell3/cell0)
# except ZeroDivisionError:
#     print('Поделить на клетку без ячеек нельзя')
# except AttributeError:
#     print('Поделить на клетку без ячеек нельзя')
cell4 = Cell(34)
cell4.make_order(int(input('Введите количество ячеек в ряду ')))