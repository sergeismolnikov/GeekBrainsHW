

#1
# with open("text.txt",'w') as f_obj:
#     while True:
#         text = f"{input('enter some text  ')}\n"
#         if text == '\n':
#             break
#         f_obj.write(text)




#2
# #
# with open("cite.txt",'r') as f_obj:
#     stroki = f_obj.readlines()
#     print ('kolichestvo strok = ', len(stroki))
#     for i in stroki:
#         print(i, len(i))




# 3
# salaries = []
# with open("salaries.txt",'r') as f_obj:
#     stroki = f_obj.readlines()
#     for i in stroki:
#         _, salary = i.split(' ')
#         salary = int(salary)
#         salaries.append(salary)
#         if salary < 20000:
#             print (salary)
# print (sum(salaries) / len (salaries))

#4

# ru_nums = {"One": "Один", "Two": "Два","Three": "Три","Four": "Четыре"}
# final_dict = {}
# with open('nums.txt', 'r') as f_obj:
#     with open('runums.txt', 'w') as ru_obj:
#         ttt = f_obj.readlines()
#         for i in ttt:
#             ennums = i.split(' - ')
#             d = {ru_nums[ennums[0]]: ennums[1]}
#             a, b = d.items()
#             ru_obj.write(a, ' - ', b)

#5
# summ = []
# with open("newnums.txt",'w') as f_obj:
#     nums = f"{input('enter number  ')}"
#     f_obj.write(nums)
# with open('newnums.txt', 'r') as num_obj:
#     summing = num_obj.readline()
#     summing = summing.split()
#     for i in summing:
#         summ.append(int(i))
#     print (sum(summ))


#6

# some_dict = {}
#
# with open("hours.txt") as f_obj:
#     for line in f_obj:
#         name, hours = line.split(':')
#         summ_hours = sum(map(int, "".join([i for i in hours if i == " " or i.isdigit()]).split()))
#         some_dict[name] = summ_hours
# print (some_dict)

#7

