
# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# new_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# find ="qwe"
# def func(new_list, find):
#     n = [index for index in range(len(new_list)) if find == new_list[index]]
#     position = -1 if new_list.count(find)<2 else n[1]
#     return position
# print(func(new_list, find))


# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


# first_list = list(map(int,input("введите  целые числа через пробел: ").split()))

# def find_proizvedenie_par(first_list):
#         """
#         произведение пар чисел списка
#         """
#         result_list = list(map(lambda i:(first_list[i]*first_list[-(i+1)]), [i for i in range(int(len(first_list)/2))]))

#         return result_list

# print("произведение пар чисел =", find_proizvedenie_par(first_list))


# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# num=int(input('введите чило N : '))
# def get_numbers(num):
#     numbers = list(map(lambda i :((-3)**i), [i for i in range(num)]))
#     return numbers
# print(get_numbers(num))


# 4 - Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.


# url =  ['https://school.novakid.ru/parent/dashboard',
#         'https://www.detmir.ru/product/index/id/3436877/',
#         'https://gb.ru/lessons/284811']


# def domen (url):
#         domen_list = [i for i in map(lambda i : i.replace('https://', ''), url)]
#         domen_list = [i for i in map(lambda i :i[:i.find('/')], domen_list)]
#         return domen_list

# print(*domen (url))


# 5 - Есть список случайных чисел в промежутке от 1 до 100, количеством 200.
#  Создайте список кортежей, первый элемент которого - индекс элемента, а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

import random

numbers = [random.randint(1, 10) for i in range(21)]

not_reapit_numbers = list(filter(lambda x: x[0] != x[1], enumerate(numbers)))

print(numbers)
print(not_reapit_numbers)



# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

import random

numbers = [random.randint(1, 10) for i in range(21)]

not_reapit_numbers = list(filter(lambda x: ((x[0]+x[1])%5==0), enumerate(numbers)))

print(numbers)
print(not_reapit_numbers)
