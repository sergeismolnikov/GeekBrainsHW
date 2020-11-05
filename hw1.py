"""

1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = 12
b = 'something'
c = float(14)
print ('type some number')
d = int(input())
print ('type something')
e = str(input())

print (a, b, c, d, e)
"""

print('введите количество переменных, которые хотите сохранить:')
d = int(input())
y = []

for i in range(0, d):
    data = input()
    y.append(data)

print('saved data', y)

"""2. Пользователь вводит время в секундах. 
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк."""

print ('type as many seconds as you want')
a = int(input())

b = a//3600
a = a - b*3600
c = a//60
d = a%60
time = "{:02}:{:02}:{:02}".format(b, c, d)
print ('time: ', time)

"""3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. 
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""

a = int(input())
a = str(a)
b = int(a)+int(a+a)+int(a+a+a)
print(b)

"""4. Пользователь вводит целое положительное число. 
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции."""

some_numb = int(input())
max_numb = 0
for i in str(some_numb):
    xxx = i
    if int(xxx) > int(max_numb):
        max_numb = xxx
print (max_numb)

"""5. Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). 
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника."""

income = int(input())
costs = int(input())
profit = income - costs
if profit < 0:
    print('negative profit :(')
if profit == 0:
    print('0 profit')
if profit > 0:
    profitability = profit / income
    print('positive profit', 'profitability = ', profitability)
    print('type workers count')
    workers = int(input())
    print ('profit per worker = ', profit / workers)

"""6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
на который общий результат спортсмена составить не менее b километров. 
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня."""

print('type initial distance')
start = int(input())
print('type target distance')
finish = int(input())
dist = []

while start < finish:
    start = start*1.1
    dist.append(start)

print(dist)
print('days to achieve', len(dist)+1)