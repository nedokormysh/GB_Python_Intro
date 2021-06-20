#####1
print("Task 1: Devide \n---------\n")
def devide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('Нельзя делить на 0')

x = float(input('x: '))
y = float(input('y: '))
print(devide(x,y))


####2
line = "=" * 50
print(line)
print("Task 2: Inputs \n---------\n")

name = input('name: ')
surname = input('surname: ')
year = input('year of birth: ')
town = input('town: ')
email = input('email: ')
phone = input('phone number: ')


def spravka(name = 'anonym', surname = 'sir', year = '1980', town = 'Town', email = 'email', phone = 'xxxxxxx'):
    str = name + " " + surname + " " + year + " " + town + " " + email + " " + phone
    return str

print(spravka(name, surname, year, town, email, phone))

####3
line = "="*50
print(line)
print("Task 3: Numbers \n---------\n")

a = int(input('first number: '))
b = int(input('second number: '))
c = int(input('third number: '))
# except ValueError:
#     print('Enter number')
# except NameError:
#     print('Enter number')

def sum_except_min(a,b,c):
    sum = a + b + c - min(a, b, c)
    return sum
print(sum_except_min(a,b,c))

##### 4
line = "=" * 50
print(line)
print("Task 4: Negative degree \n---------\n")

n = float(input('number: '))
s = int(input('stepen: '))
if s > 0:
    print('Работа программы будет неверной. Второй метод не будет давать требуемый результат')

def my_fu(x, y):
    # return (x ** y)
    res1 = f"Результат первым методом = {(x ** y)}"
    # второй метод
    y = abs(y)
    t = 1
    for i in range(0, y):
        t *= x
    res2 =f"Результат вторым методом = {1/t}"
    return res1, res2

print(my_fu(n, s))
#
# def my_fuC(x, y):
#     res1 = (x ** y)
#     y = abs(y)
#     t = 1
#     for i in range(0, y):
#         t *= x
#     return 1 / t

# print(my_fuC(n, s))

#### 5
line = "=" * 50
print(line)
print("Task 5: Summ String \n---------\n")

res = 0
#resu = 0
def Summa(*integers):
    global res #, resu
    # res = 0
    for i in integers:
        res += i
    # resu == sum(integers)
    return res#, resu

IsOn = True
while IsOn:
    str = input("Введите цифры в строку через пробел. Для выхода наберите s: ")
    li = str.split()
    for i in li:
        if i.title() == 'S':
            IsOn = False
            break
        Summa(int(i))
    print(res)

# print(resu)

###### 6 - 7
line = "=" * 50
print(line)
print("Task 6: text_to_Text \n---------\n")

str = input('Введите строку в нижнем регистре: ')

def text_Text(str):
    str_T = ''
    for i in str.split():
        i = i.title()
        str_T = str_T +' '+ i
    return str_T

print(text_Text(str))