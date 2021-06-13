# ####1
print("Task 1: Random variables \n---------\n")
celoe = 5
stroka = 'Hello tutor'
decimal = 0.5
print(celoe)
print(decimal,stroka,"\n")
# a, b, c
a:str
b:str
c:str
#print(type(a))
a = "Black Swan"; b = "of"; c = "econometrics"
print(f'{a:<20}'f'{b:<8}'f'{c:<20}')
Name = input("Enter your name: ")
Age = input("Enter your age: ")
print("Your name is: ",Name)
print("Your age: ",Age)


# ####2
line = "="*50
print(line)
print("Task 2: Time \n---------\n")
time = int(input('Enter time in seconds: '))
seconds = time%60
minutes = int((time)%3600//60)
hours = int(time//3600)
print(f"{hours}:{minutes}:{seconds}")

####3
line = "="*50
print(line)
print("Task 3: One-Two-Three \n---------\n")
n = input('Enter number ')
nn = (n+n)
nnn = n + n + n
print("n =", n)
print("nn =", nn)
print("nnn =", nnn)
print('Result of n + nn + nnn is:', int(n) + int(nn) + int(nnn))

####4
line = "="*50
print(line)
print("Task 4: Max Digit \n---------\n")
number = input('Enter positive integer number ')
#print(type(number))
#if isinstance(number,int):
number=int(number)
ni = number % 10
max_digit = 0
while number > 0:
    if ni > max_digit:
        max_digit = ni
        if max_digit == 9:
            break
    number = number // 10
    ni = number % 10
print(max_digit)
#else:
#    print("Wrong input!")

####5
line = "=" * 50
print(line)
print("Task 5: 'Financial_and_Operating_highlights'\n---------\n")
revenue = float(input("Input revenue: "))
cost = float(input('Input costs: '))
profit_loss = revenue-cost
if revenue >= cost:
    print('You have profit! =', profit_loss)
    margin = print('Your margin in percents is = ',(profit_loss/revenue)*100)
    number_of_employees = int(input('Enter number of employees'))
    profit_per_employee = print('Your profit per employee is = ', profit_loss/number_of_employees)
else:
    print('You have loss. =', profit_loss)

####6
line = "=" * 50
print(line)
print("Task 6: 'Athlete'\n---------\n")
km_ni_day = float(input('Enter how many kilometres did the athlete run on the first day: '))
km_last_day = float(input('Enter the kilometres to finish: '))
# try:
#     if km_ni_day > km_last_day:
#         raise ValueError("Error")
# except:
#     print('\n km of the last day should be bigger than ')
i = 1
print(i,'day', km_ni_day)
while km_ni_day<=km_last_day:
    km_ni_day = km_ni_day+km_ni_day*0.1
    i+=1
    #print(i,'day', round(km_ni_day,2))
    #print(i,'day',"%.2f" % km_ni_day)
    print(f"{i} day {km_ni_day:.2f}")
print('\nAnswer: on the', i, 'day')

 # целое = 8
 # print(целое)