###1
print("Task 1: Script with arguments \n---------\n")

from sys import argv
print(argv)

output_in_hours, rate_in_hours, bonus = map(int, argv[1:])

def Calculation(output_in_hours = 1, rate_in_hours = 1,bonus = 1):
    return (output_in_hours*rate_in_hours) + bonus
print(Calculation(output_in_hours,rate_in_hours,bonus))

###2
line = "=" * 50
print(line)
print("Task 2: Bigger one \n---------\n")

source2 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
drain = [source2[i] for i in range (1, len(source2)) if source2[i] > source2[i - 1]]
print(f'List {drain}')
# d = [k for k in range(1, len(source2)) if source2[k] > source2[k-1]]
# d=[]
# for i in range(1, len(source)):
#     if source[i] > source[i-1]:
#         d.append(source[i])
# print(d)


###3
line = "=" * 50
print(line)
print("Task 3: 20||21 \n---------\n")

m = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(f'List % 20 || 21 : {m}')

###4
line = "=" * 50
print(line)
print("Task 4: Without repeats  \n---------\n")

source4 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
drain4 = [source4[i] for i in range(0, len(source4)) if source4.count(source4[i]) == 1]
print(f'List without repeats {drain4}')

###5
line = "=" * 50
print(line)
print("Task 5: Multiply  \n---------\n")

from functools import reduce
def Multiply(a, b):
    return a * b
n = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(Multiply,n))

###6 -a
line = "=" * 50
print(line)
print("Task 6: Count - Cycle  \n---------\n")

from itertools import count

for el in count(int(input("Enter number: ")), 10):
    if el > 1000:
        break
    else:
        print(el)

###6 - b
from itertools import cycle

n = [i for i in range(-10, 1)]
# print(n)
# n = [10,20,230]
c = 0
for el in cycle(n):
    if c > 25:
         break
    print(el)
    c += 2

###7
line = "=" * 50
print(line)
print("Task 7: Factorial  \n---------\n")

n = int(input('n = '))
def factorial(n):
    temp = 1
    if (n == 0):
       yield temp
    else:
        for i in range(1, n + 1):
            temp = temp * i
            yield temp

for el in factorial(n):
     print(el)







