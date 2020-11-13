#1 задание
def my_divide(arg_1, arg_2):
    return arg_1/arg_2

a1 = int(input())
a2 = int(input())

if a2 == 0:
    print('soryan, mi tut na 0 ne delim')
else:
    print(my_divide(a1, a2))


#2

some_data = []

def data_func(xxx):
    data_dict = {"имя": [] , "фамилия": [], "год рождения": [] , "город проживания": [], "email":[], "телефон":[]}
    n=0
    for i in data_dict:
        data_dict[i] = xxx[n]
        n+=1
    return data_dict

for i in range(6):
    some_data.append(input())


some_data = tuple(some_data)


print(data_func(some_data))



#Задание 3
#Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов

def two_func(var_1, var_2, var_3):
    c = [var_1, var_2, var_3]
    c.sort()
    return c[1] + c[2]
print ('vvedite tri chisla')
tri_chisla = [int(input()) for i in range(3)]
print(two_func(tri_chisla[0], tri_chisla[1],tri_chisla[2]))


#задание 4

#через **

def amp_calc1():
    val1 = float(input("Укажите действительное число: "))
    val2 = int(input("Укажите отрицательное число: "))
    return val1 ** val2
print (amp_calc1())

#с циклом

def amp_calc3():
    val1 = float(input("Укажите действительное число: "))
    val2 = int(input("Укажите отрицательное число: "))
    c = 1
    for i in range(abs(val2)):
        c *= val1
    return 1 / c

print (amp_calc3())




# 5) Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символвведен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.

summ = 0
flag = True


def count_func():
    global summ, flag
    n = [i for i in input().split()]
    for i in n:
        if i != 'x':
            summ = summ + int(i)
        elif i == 'x':
            flag = False


while True:
    count_func()
    if flag == False:
        break

print(summ)


#6

vivod = []


def cap_func(x):
    x = x.capitalize()
    return x


vvod = [i for i in input().split()]

for i in vvod:
    vivod.append(cap_func(i))

print(*vivod, sep=' ')