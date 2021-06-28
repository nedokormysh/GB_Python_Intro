####1
print("Task 1: Strings into file \n---------\n")
# tsk1 = open('hw5_tsk1.txt', 'w', encoding='utf-8')

with open('hw5_tsk1.txt', 'w', encoding='utf-8') as tsk1:
    while True:
        str = input('Enter words: ')
        if (str == ''):
            break
        str = str.split()
        for el in str:
            tsk1.write(f'{el}\n')
print('end')

####2

line = "=" * 150
print(line)
print("Task 2: Counts \n---------\n")

try:
    with open('hw5_tsk2.txt', 'r', encoding='utf-8') as tsk2:
        print(tsk2.read())
        tsk2.seek(0)
        li = tsk2.readlines()

        def CountLines(li):

            for el in li:
                print(f'"{el.rstrip()}"')
                el = el.split(' ')
                print(f'Количество слов в строке: {len(el)}\n')
        CountLines(li)

        def CountChars(li):
            amount = 0
            global amount_
            amount_ = 0
            for el in li:
                amount += len(el)
                litemp = list(el)
                for item in litemp:
                    amount_ += item.count(' ')
            return amount
        print('Количество строк = ', len(li),'Количество знаков с пробелами =', CountChars(li),
              'Количество знаков без пробелов = ', CountChars(li) - amount_)
except IOError:
    print('Error')
# finally:
#     tsk2.close()

####3
line = "=" * 150
print(line)
print("Task 3: Salary \n---------\n")
try:
    with open('hw5_tsk3.txt', 'r', encoding='utf-8') as tsk3:

        lit = tsk3.readlines()

        li = []

        for el in lit:
            if el.endswith('\n'):
                el = el[:len(el)-1]
                li.append(el)
            else:
                li.append(el)

        litemp = []
        for el in li:
            lisep = el.split(' ')
            litemp.append(lisep)
        # print(litemp)
        di = dict(litemp)
        print(di)

        def get_key(di, value):
            for k, v in di.items():
                if v == value:
                    return k
        Names = ''
        for i in di.values():
            if float(i) < 20000:
                Names += get_key(di, i) + ', '
        Names = Names[:-2]

        print('Сотрудники с зарплатой ниже 20 тыс.:', Names)

        def average(di_values):
            lin = []
            for el in di_values:
                el = float(el)
                lin.append(el)
            return sum(lin) / len(lin)

        print('Средняя зарплата =', format(average(di.values()), '.2f'))

except IOError:
    print('Error')



####4

line = "=" * 150
print(line)
print("Task 4: Dictionary  \n---------\n")

try:
    with open('hw5_tsk4.txt', 'r', encoding='utf-8') as tsk4:
        li4 = tsk4.read().splitlines()
        print(li4)

        litemp = []

        for el in li4:
            elsep = el.split('—')
            litemp.append(elsep)
        # print(litemp)

        li_russian = ['Один ', 'Два ', 'Три ', 'Четыре ']

        for i in range(0, 4):
            litemp[i][0] = li_russian[i]
        # print(litemp)

        li4 = []

        for i in range(0, len(litemp)):
            el = '—'.join(litemp[i])
            li4.append(el)
        # print(li4)

        with open('hw5_tsk4_return.txt', 'w+', encoding='utf-8') as tsk4_return:
            for el in li4:
                tsk4_return.write(f'{el}\n')
            tsk4_return.seek(0)
            print(tsk4_return.read().splitlines())
except IOError:
    print('Error')
# finally:
#     tsk4.close()
#     tsk4_return.close()

#####5

line = "=" * 150
print(line)
print("Task 5: Summ  \n---------\n")

try:
    with open('hw5_tsk5.doc', 'w+', encoding='utf-8') as tsk5:

        tsk5.writelines('1 2 3 5000 63000 789 45661')

        tsk5.seek(0)

        Summ = 0

        for el in tsk5.read().split(' '):
            el = float(el)
            Summ += el
        print(Summ)

except IOError:
    print('Error')

####6

line = "=" * 150
print(line)
print("Task 6: Schedule  \n---------\n")

try:
    with open('hw5_tsk6.txt', 'r', encoding='utf-8') as tsk6:
        li6 = tsk6.read().splitlines()

        litemp=[]
        for el in li6:
            el = el.split(' ')
            litemp.append(el)
        print(li6)

        def str_in_digit(el):
            str_of_ch = ''
            digits = 0
            for item in el:
                j = 0
                for ch in item:
                    j += 1
                    if ch.isdigit():
                        str_of_ch += ch
                    if j == len(item):
                        if str_of_ch.isdigit():
                            digits += int(str_of_ch)
                            str_of_ch = ''

            return digits

        di = {}
        for el in litemp:
            di[el[0][:-1]] = str_in_digit(el)
        print(di)

except IOError:
    print('error')

#####7

line = "=" * 150
print(line)
print("Task 7: Profit. Json  \n---------\n")

try:
    with open('hw5_tsk7.txt', 'r', encoding='utf-8') as tsk7:

        li7 = tsk7.readlines()
        # print(li7)
        li_temp = []
        for el in li7:
            el = el.split()
    # el = el.rstrip()
            li_temp.append(el)
        # print(li_temp)

        av_profit = 0
        j = 0
        def Profit(earnings, costs):
            global av_profit
            global j
            profit = float(earnings) - float(costs)
            if profit > 0:
                j += 1
                av_profit += profit
                av_profit = av_profit / j
            return profit

        di = {}
        for el in li_temp:
            # print(el[3])
            di[el[0]] = Profit(el[2], el[3])
        di_av = {'Average_Profit': format(av_profit, '.2f')}
        li7 = [di, di_av]
        print(li7)

        import json

        with open('hw5_tsk7.json', 'w') as tsk7_json:
            json.dump(li7, tsk7_json)

except IOError:
    print('error')
