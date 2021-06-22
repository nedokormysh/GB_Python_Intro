#####1
print("Task 1: Type list \n---------\n")
li=[2,2.7,complex(2,4),'Rock']

for i in li:
    print(type(i))

for i in 1, 2, 3, 'one', 'two', 'three':
    print(i, type(i))

# for (int i=0; i<=li.Length;i++)
#   Console.WriteLine(li[i].GetType())
# foreach(int i in li)


####2
line = "="*50
print(line)
print("Task 2: Changes \n---------\n")
c = int(input('Enter how many elements we will use: '))
li = []
i = 0
while i < c:
    li.append(input(f'You should enter {c} elements. Enter element {i+1}: '))
    i += 1
print("Direct list is:", li)
# li[0], li[1] = li[1], li[0]
# li[2], li[3] = li[3], li[2]
# print(li)
i = 0
while i + 1 < c:
    if i % 2 == 0:
        li[i], li[i + 1] = li[i + 1], li[i]
    i += 1
print("List with reversed elemets is", li)

####3
line = "="*50
print(line)
print("Task 3: Months \n---------\n")
li = ['January', 'February', 'March', 'April', 'May','June',
      'July', 'August', 'September', 'October', 'November','December']
n=13
while n not in range(1,13):
    try:
        n = int(input("Enter month number: "))
    except ValueError:
        continue

seasons = ['winter', 'spring', 'summer' 'autumn']
#if (n == 12 or n == 1 or n == 2):
#    print(f'It is {lis[0]}')
#elif n == 3 or n == 4 or n == 5:
#    print(f'It is {lis[1]}')
#elif n == 6 or n == 7 or n == 8:
#    print(f'It is {lis[2]}')
#else n == 6 or  7 or  8:
#    print(f'It is {lis[3]}')


if n in [12,1,2]:
    print(li[n - 1], f"is {seasons[0]} month")
elif n in [3, 4, 5]:
    print(li[n - 1], f"is {seasons[1]} month")
elif n in [6, 7, 8]:
    print(li[n - 1], f"is {seasons[2]} month")
else:
    print(li[n - 1], f"is {seasons[3]} month")



mons = {(12,1,2):'Winter',
        (3,4,5):'Spring',
        (6,7,8):'Summer',
        (9,10,11):'Autumn'}
for key in mons.keys():
    if n in key:
        print(li[n-1],f"is {mons[key]} month")
        break

##### 4
line = "="*50
print(line)
print("Task 4: Split spaces \n---------\n")
str = input("Enter some words with spaces: ")
# print(str.split(' '))
str.split()
# print(type(li))
for i, v in enumerate(str.split(), 1):
   print(i, v[0:10])

##### 5
line = "="*50
print(line)
print("Task 5: Insertion in sorted list \n---------\n")
my_list=[6,7,4,4,3,3,5]
my_list.sort()
my_list.reverse()
print(my_list)
# print(my_list[1])
# print(my_list.index(my_list[6]))
n=int(input("Enter new number: "))

if n <= my_list[-1]:
   my_list.insert(len(my_list),n)
else:
   for i in range(0,len(my_list)):
      if n > my_list[i]:
         my_list.insert(i,n)
         break

print(my_list)


###### 6
line = "="*50
print(line)
print("Task 6: Database \n---------\n")

li=[]
# lil=[]
list_name=[]
list_price=[]
list_amount=[]
list_unit=[]
while True:
    name = input('Enter name: ')
    price = input('Price: ')
    amount = input('Amount: ')
    unit = input('Unit: ')
    ## all={name, price, amount, unit}
    all = (name,price,amount,unit)
    # alll=[name,price,amount,unit]
    list_name.append(name)
    list_price.append(price)
    list_amount.append(amount)
    list_unit.append(unit)
    li.append(all)
    # lil.append(alll)
    s = input('"s" to exit: ')
    if s.title() == 'S':
        break

for i, v in enumerate(li, 1):
        print(i, {v})
print("analize")
di={"название": list_name, "цена": list_price, "количество": list_amount,"единица измерения": list_unit}
print(di)


# print(lil)
# print(len(lil))
# print(len(lil[0]))
#
# listname=[]
# for i in lil[0]:
#     listname.append(lil[i][1])
# print(listname)
# # print(list(li))
# for i in range(len(lil)):
#     for j in range(len(lil[i])):
#         # print(lil[i][j], end ="")
#         di = {"название": lil[j][0], "цена": lil[j][1], "количество": lil[j][2]}
#         print(di)



# di = {"название":li[0][0]}
# di1= {"название":li[1][0]}
# print(di)
# print(di1)
# for i in li:
#     for n in li[i]:
#         di = {"название":li[i][n]}
# print(di)
#
# print(list(li[0][0]))
# print(li[0][0])

# for el in li:
#     di = {li[i][i]}
#     di={f'{name}':f'"price": {price}, "amount": {amount}, "unit": {unit}'}
# print(di)


# for id, val in enumerate(li, 1):
#     print(id, val)
