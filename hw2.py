# 1) Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе

a = 12
b = 'text'
c = 1.12
d = True
e = [1, 2, 3]
f = None
e = "sometext".encode('UTF-8')

a_list = [a, b, c, d, e, f]
for i in a_list:
    print(i, '-', type(i))

# 2) Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При
# нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

# b_list = [i for i in input().split(',') if i != ' '] - неудачный эксперимент, тк список бился по каждому значению, не придумал
# как это исправить, поэтому взял map

b_list = list(map(str, input("Enter a multiple value: ").split()))
# заполняем список элементами
lenblist = len(b_list)
c_list = []
i = 1

# сохранил длину оригинального списка в переменную, дальше выбиваю по элементу из него в нужном порядке
# для нечетного списка сделал исключение с брейком
while True:
    if len(b_list) == 1:
        c_list.append(b_list.pop(i - 1))
        break
    c_list.append(b_list.pop(i))
    c_list.append(b_list.pop(i - 1))
    if len(c_list) == lenblist:
        break

print(c_list)

# 3)Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.
month_list = [[12, 1, 2], [4, 5, 3], [7, 8, 6], [10, 11, 9]]
month_dict = {"зима": [12, 1, 2], "весна": [4, 5, 3], "лето": [7, 8, 6], "осень": [10, 11, 9]}

print('vvedite nomer mesyatsa')
month = int(input())

for i in month_list:
    if month in i and month_list.index(i) == 0:
        print('зима')
    elif month in i and month_list.index(i) == 1:
        print('весна')
    elif month in i and month_list.index(i) == 2:
        print('лето')
    elif month in i and month_list.index(i) == 3:
        print('осень')

for season in month_dict:
    if month in month_dict[season]:
        print(season)


#4)Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
#Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

d_list = [i for i in input().split(' ')]
a = 1
for i in d_list:
    if len(i) < 11:
        print (a, i)
    else:
        print (a, i[:10:])
    a += 1

#5 задание

my_list = [7, 5, 3, 3, 2]
some_numb = int(input())
check = 1
for numb in my_list:
    if some_numb <= numb:
        print("проверка на актуальность вставки")
    else:
        c = my_list.index(numb)
        print(c)
        my_list.insert(c, some_numb)
        print(my_list)
        check = 0
        break

if check == 1:
    #проверочная на случай, если элемент не включили раньше
    my_list.append(some_numb)
print(my_list)


#6 задание

n = []
price_list =[]
b = 1

def new_dict(var1, var2, var3, var4):
    some_dict = {"название": var1, "цена": var2, "количество": var3, "eд": var4}
    return some_dict


while True:
    n.append(b)
    print('vvedite nazvanie')
    var1 = input()
    print('vvedite tsenu')
    var2 = input()
    print('vvedite kolichestvo')
    var3 = input()
    print('vvedite unit')
    var4 = input()
    n.append(new_dict(var1, var2, var3, var4))
    b += 1
    price_list.append(tuple(n))
    n.clear()
    print('esli vi hotite zakonchit sozdanie dokumenta vvedidite: +++, a esli net: ---')
    stop_flag = input()
    if stop_flag == '+++':
        continue
    elif stop_flag == '---':
        break
# print(price_list)

price_list2 = []

for p in price_list:
    aaa, ccc = p
    price_list2.append(ccc)   # выкинули порядковые
# print (price_list2)

analysed_dict = {'название': [], 'цена': [], 'количество': [], 'eд': []}

for position in price_list2:
    for key, val in position.items():
        analysed_dict[key].append(val)

print('lovite slovar s analizom', analysed_dict)
