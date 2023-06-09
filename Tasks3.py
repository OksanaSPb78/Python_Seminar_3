# Задача №17. 
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# **Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# # импортируем модуль random (встроенная библиотека)
# import random
# # создаем список случайных чисел
# my_list = [random.randint(0,10) for i in range(10)]

# # выводим созданный список
# print(my_list)
# # выводим список уникальных чисел
# print(set(my_list))
# # выводим количество уникальных (неповторяющихся) чисел
# print(len(set(my_list)))



# Задача №19. 
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю 
# последовательность(сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# *Примечание: Пользователь может вводить значения списка или список задан изначально.

# # ВАРИАНТ 1 с помощью pop  и insert
# import random
# # создаем список из чисел по порядку от 0 до 9
# my_list=[i for i in range(10)]
# print(my_list)
# # вводим переменную к (шаг)
# k=int(input('На сколько сдвигаем вправо: '))
# # запускаем цикл на заданное количество сдвигов
# for i in range(k):
#     # вводим переменную, где удаляем последний элемент из списка
#     temp=my_list.pop(len(my_list)-1)   
#     # temp=my_list.pop()  тоже самое 
#     # всталяем удаленный элемент на позицию [0]
#     my_list.insert(0,temp)
# print(my_list)


# # ВАРИАНТ 2 среза
# my_list=[i for i in range(10)]
# print(my_list)
# k=int(input('На сколько сдвигаем вправо: '))
# # делим список пополам срезами двумя и склеиваем их со сдвигом вправо
# print(my_list[-k:]+ my_list[:-k])
# # # делим список пополам срезами двумя и склеиваем их со сдвигом влево
# # print(my_list[k:]+ my_list[:k])

# # ВАРИАНТ 3 прохождение по индексам
# my_list=[i for i in range(10)]
# print(my_list)
# k=int(input('На сколько сдвигаем вправо: '))
# # создаем новый пустой  список
# new_list=[]
# # циклом проходим по длине заданого списка
# for i in range(len(my_list)):
# # в новый список добавляем  элемент из заданного списка в конец нового списка (i-k = 0-3(шаг)=-3)
#     new_list.append(my_list[(i-k)])
# print(new_list)



# import random
# my_list=[random.randint(0,10) for i in range(10)]
# print(my_list)
# k=int(input('Введите число k: '))

# for i in range(len(my_list)):

# item=my_list.pop(0)
# print(my_list)
# my_list.append(item)
# print(my_list)

# item=my_list.pop(0)
# print(my_list)
# my_list.append(item)
# print(my_list)



# Задача №21.
# Напишите программу для печати всех уникальных значений в словарях.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "},
#  {" V ":" S009 "}, {" VIII":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

# # ВАРИАНТ 1
# # создаем список со словарями
# list_1=[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": "S005"},
# {"V":"S009"}, {"VIII":"S007"}]
# # обратимся к данному списку
# print(list_1)
# # создаем пустое множество (уникальность)
# my_set=set()
# # проходимся циклом по каждому словарю с нашем списке
# for item in list_1:
#     # проходим циклом по ключам словарей
#     for value in item.values():
#         # добавляем в множество наши уникальные значения
#         my_set.add(value)
# print(my_set)

# # ВАРИАНТ 2
# # создаем список со словарями
# list_1=[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": "S005"},
# {"V":"S009"}, {"VIII":"S007"}]
# # обратимся к данному списку
# print(list_1)
# my_set=set()
# for item in list_1:
#     # проходим по ключам
#     for key in item.keys():
#         # добавляем во множество, обращаясь к словарювернуть значения уникальные
#         my_set.add(item.get[key])
# print(my_set)



# Задача №23.
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения списка или список задан изначально.

# import random
# my_list=[random.randint(0,15) for i in range(10)]
# print(my_list)
# # вводим переменную , для подсчета количества элементов массива по условию
# count=0
# # счётчик массива
# for i in range(1, len(my_list)):
#     if my_list[i]>my_list[i-1]:
#         count+=1
# print(count)

sum