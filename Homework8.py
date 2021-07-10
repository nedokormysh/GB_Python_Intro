# ####1
print("Task 1: Date \n---------\n")

class Date:
    def __init__(self, str_date):
        self.str_date = str(str_date)

    @classmethod
    def str_into_digits(cls, str_date):
        Date.validation(int(str_date.split(' ')[0]), int(str_date.split(' ')[1]), int(str_date.split(' ')[2]))

        day = int(str_date.split(' ')[0])
        month = int(str_date.split(' ')[1])
        year = int(str_date.split(' ')[2])

        return day, month, year

    @staticmethod
    def validation(day, month, year):
        if day > 31 or day < 1:
            print('Вы ввели неверное число')
        if month > 12 or month < 1:
            print('Вы ввели неверный месяц')
        if year > 2050 or year < -6500:
            print(f'Вы ввели неверный год')
        else:
            return day, month, year

    def __str__(self):
        return f'Вы ввели дату {Date.str_into_digits(self.str_date)}'

    # def __str__(self):
    #     return f''
a = Date('50 15 2000')
print(a)
b = Date('20 15 2020')
print(b)
# print(a.str_into_digits('50 15 2000'))
# print(a.str_into_digits('20 12 2020'))



#####2
line = "=" * 150
print(line)
print("Task 2: Own exception  \n---------\n")

print('Var 1. Classes')
class Division():
    def __init__(self, divisible, devider):
        self.div = divisible
        self.dev = devider

    @staticmethod
    def devide(divisible, devider):
        try:
            return divisible / devider
        except:
            return f'В знаменателе 0'

inp_div = int(input("Введите делимое: "))
inp_dev = int(input("Введите делитель: "))

print(Division.devide(inp_div,inp_dev))

####### var2

print('Var 2. Own Class')
class OwnZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt

# inp_div = int(input("Введите делимое: "))
# inp_dev = int(input("Введите делитель: "))

inp_div = 100
inp_dev = 0
try:
    if inp_dev == 0:
        raise OwnZeroDivision('Нельзя делить на ноль')

    inp_div / inp_dev

except OwnZeroDivision as err:
    print(err)

except ZeroDivisionError:
    print('Не мой класс. Но тут ошибка деления на ноль')

# ##### 3

line = "=" * 150
print(line)
print("Task 3: Not a digit  \n---------\n")

class NotADigit(Exception):
    def __init__(self, x):
        self.x = x
    def __str__(self):
        return f'Введено не число. Вы ввели {self.x}'

li_digits_only = []

while True:
    x = input("Для выхода нужно набрать q. Введите число: ")
    try:
        if x.isdigit() == False:
            raise NotADigit(x)
    except NotADigit as err:
        print(err)

    if x.isdigit():
        li_digits_only.append(x)
    elif x.title() == ('Q'):
        break

print(li_digits_only)

#####4-5-6

line = "=" * 150
print(line)
print("Task 4-5-6: Storage  \n---------\n")

from abc import ABC, abstractmethod

class AbctactStorage(ABC):

    def __str__(self):
        return f'\nТеперь общее количество элементов на складах {stor_Main + stor_Random}'


class Storage(AbctactStorage):

    def __init__(self, name='Random'):
        self.name_of_storage = name
        self.__amount_all = 0
        self.li_stor_obj = []

    def __str__(self):
        return f'Это склад {self.name_of_storage}. На нём числиться {self.count} коробок'

    @property
    def count(self):
        sum = 0
        for el in self.li_stor_obj:
            sum += el.get('Количество')
        self.__amount_all = sum

        return self.__amount_all

    def adding(self, di):
        self.li_stor_obj.append(di)

    def deleting(self, di):
        try:
            removed = self.li_stor_obj.pop(self.li_stor_obj.index(di))
            return removed
        except ValueError:
            print('Такой элемент не найден в списке')

    @property
    def contain(self):
        if self.count == 0:
            print(self.__str__())
        else:
            print(f'На складе {self.name_of_storage} находятся:')
            for i, v in enumerate(self.li_stor_obj, 1):
                print(i, v)

    def transfer(self, other_stor, di):
        other_stor.adding(self.deleting(di))

    def __add__(self, other):
        return self.count + other.count


stor_Main = Storage('Main')
stor_Random = Storage()


class OfficeEquipment(ABC):

    def __init__(self, value, quantity):
        self.q = quantity
        self.v = value

    @abstractmethod
    def push(self):
        pass

    @abstractmethod
    def pull(self):
        pass

    @staticmethod
    def findStorage(di):
        if (stor_Main.li_stor_obj.count(di) == 1):
            return stor_Main
        elif (stor_Random.li_stor_obj.count(di) == 1):
            return stor_Random
        else:
            return None

class Scaner(OfficeEquipment):
    scaner_items = []

    def __init__(self, value, quantity, type_of_scaners):
        super().__init__(value, quantity)
        self.type_scn = type_of_scaners

        self.di_of_scanners = {'Имя переменной': self.v, 'Техника': 'Сканеры', 'Количество': self.q,
                               'Тип': self.type_scn}
        Scaner.scaner_items.append(self.di_of_scanners)

    def __str__(self):
        return f'Вы выбрали сканеры в количестве {self.q} по типу {self.type_scn}.  \n Полный объект теперь {self.di_of_scanners} \n '

    def push(self, stor=stor_Random):
        Storage.adding(stor, self.di_of_scanners)

    def pull(self):
        stor = OfficeEquipment.findStorage(self.di_of_scanners)
        if (stor == None):
            print('Этого элемента нет ни на одном складе.')
        else:
            Storage.deleting(stor, self.di_of_scanners)

type_of_scaners = ['планшетные', 'носимые', 'барабанные']


class Xerox(OfficeEquipment):
    xerox_items = []
    def __init__(self, value, quantity, format_of_sheet):
        super().__init__(value, quantity)
        self.form_sheet = format_of_sheet

        self.di_of_xerox = {'Имя переменной': self.v, 'Техника': 'Ксероксы', 'Количество': self.q,
                            'Тип': self.form_sheet}
        Xerox.xerox_items.append(self.di_of_xerox)

    def __str__(self):
        return f'Вы выбрали ксероксы в количестве {self.q} по типу {self.form_sheet}.  \n Полный объект теперь {self.di_of_xerox} \n'

    def push(self, stor = stor_Random):
        Storage.adding(stor, self.di_of_xerox)

    def pull(self):
        stor = OfficeEquipment.findStorage(self.di_of_xerox)
        if (stor == None):
            print('Этого элемента нет ни на одном складе.')
        else:
            Storage.deleting(stor, self.di_of_xerox)

format_of_sheet = ['A5', 'A4', 'A3', 'A1']


class Printer(OfficeEquipment):
    printer_items =[]

    def __init__(self, value, quantity, type_of_printers):
        super().__init__(value, quantity)
        self.type_prnt = type_of_printers

        self.di_of_printers = {'Имя переменной': self.v, 'Техника': 'Принтеры', 'Количество': self.q,
                               'Тип': self.type_prnt}

        Printer.printer_items.append(self.di_of_printers)

    def __str__(self):
        return f'Вы выбрали принтеры в количестве {self.q} по типу {self.type_prnt}. \n Полный объект теперь {self.di_of_printers} \n'

    def push(self, stor=stor_Random):
        Storage.adding(stor, self.di_of_printers)

    def pull(self):
        stor = OfficeEquipment.findStorage(self.di_of_printers)
        if (stor == None):
            print('Этого элемента нет ни на одном складе.')
        else:
            Storage.deleting(stor, self.di_of_printers)


type_of_printers = ['laser', 'diod', 'matrix', '3D']

print(AbctactStorage.__str__(Storage))

# 1
print('1) Создали 2 объекта класса Storage: stor_Main, stor_Random\n')

stor_Main.contain
print(stor_Random)
# 2
print('\n2) \nСоздаём несколько тестовых объектов разных классов\n')

Scaner_Nokia = Scaner('Scaner_Nokia', 5, type_of_scaners[0])
Scaner_Canon = Scaner('Scaner_Canon', 10, type_of_scaners[1])
print('Объекты класса сканеры', '\n', Scaner_Nokia, '\n', Scaner_Canon)
Printer_Canon = Printer('Printer_Canon', 10, type_of_printers[1])

print('Объект класса принтеры', '\n', Printer_Canon)
Xerox_Kseroks = Xerox('Xerox_Kseroks', 60, format_of_sheet[2])
print('Объекты класса сканеры', '\n', Xerox_Kseroks)

# 3
print('3) \nДобавим наши объекты в разные отделы склада')
stor_Main.adding(Scaner_Nokia.di_of_scanners)
stor_Main.adding(Scaner_Canon.di_of_scanners)
# print('Наш основной склад состоит из:\n')
stor_Main.contain
# print('\nДобавим объекты на другой склад вторым способом через объекты')
Xerox_Kseroks.push()
Printer_Canon.push()
print('\nНа втором складе образовались такие товары\n')
stor_Random.contain

print(AbctactStorage.__str__(Storage))

# 4
print('\n4)\nПереместим наши товары с одного склада на другой')

stor_Main.transfer(stor_Random, Scaner_Nokia.di_of_scanners)
stor_Main.contain
stor_Random.contain

print('\n5)\nУдалим наши товары со склада. Это также можно сделать из класса хранилища или из объекта орг. техники')
stor_Random.deleting(Scaner_Nokia.di_of_scanners)
stor_Random.contain

print(AbctactStorage.__str__(Storage))
Printer_Canon.pull()
print(AbctactStorage.__str__(Storage))
Printer_Canon.pull()

print('\n6)\nСоздадим новый объект')

class ErrorMyValue(Exception):
    def __init__(self, txt):
        self.txt = txt

str = input('Введите какой объект мы хотим создать: принтеры, сканеры, ксероксы: ')

try:
    if (str.title() != 'Сканеры' and 'Принтеры' and 'Ксероксы'):
        raise ErrorMyValue('Необходимо ввести: сканеры или принтеры или ксероксы')
except (ErrorMyValue) as err:
    print(err)
else:
    print('Ок')

class ErrorQuantity(Exception):
    def __init__(self, txt):
        self.txt = txt

num = input('Введите количество элементов: ')

try:
    if int(num) <= 0:
        raise ErrorQuantity('Необходимо ввести число больше нуля')
except ErrorQuantity as err:
    print(err)
except ValueError:
    print('Необходимо ввести число')
else:
    print('Ok')

if (str.title() == 'Сканеры'):
    type_of_scaners.append(input('Введите тип сканера: '))
    MyInstance = Scaner('MyInstance', num, type_of_scaners[-1])
elif(str.title() == 'Принтеры'):
    type_of_printers.append(input('Введите формат сканеров: '))
    MyInstance = Printer('MyInstance', num, type_of_printers[-1])
elif(str.title() == 'Ксероксы'):
    format_of_sheet.append(input('Введите формат бумаги для ксерокса: '))
    print(format_of_sheet)
    MyInstance = Xerox('MyInstance', int(num), format_of_sheet[-1])


print(MyInstance)

MyInstance.push()
stor_Random.contain

#####7

line = "=" * 150
print(line)
print("Task 7: Complex numbers  \n---------\n")

class CompexNumbers():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.number = f'{self.a} + i * {self.b}'

    def __str__(self):
        return f'Вы ввели число {self.number}'

    def __add__(self, other):
        return f'Результат сложения {self.a + other.a} + i * {self.b + other.b}'

    def __mul__(self, other):
        return f'Результат умножения {self.a * other.a - self.b * other.b} + i * {self.a * other.b + self.b * other.a}'

one = CompexNumbers(2, 3)
two = CompexNumbers(3, 4)
print(one)
print(two)
print(one + two)
print(one * two)