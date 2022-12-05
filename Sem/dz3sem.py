# дз
# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# new_list = list(map(int,input("введите числа через пробел: ").split()))

# def find_sum_nechet_elementov (new_list):
#         """
#         cумма элементов списка, стоящих на нечётных позициях
#         """
#         summa=0
#         for i in range(1,len(new_list),2):
#                 summa+=new_list[i]
#         return summa

# print(f"сумма элементов списка, стоящих на нечётных позициях = ", find_sum_nechet_elementov(new_list))


# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# first_list = list(map(int,input("введите  целые числа через пробел: ").split()))


# def find_proizvedenie_par(first_list):
#         """
#         произведение пар чисел списка
#         """
#         result_list=[]
#         for i in range(int(len(first_list)/2)):
#                 result_list.append(first_list[i]*first_list[-(i+1)])
#                 if len(first_list)%2!=0:
#                         result_list.append(first_list[i+1]**2)
#         return result_list

# print("произведение пар чисел =", find_proizvedenie_par(first_list))

# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.9814] - 0.9114 или 9114



# first_list = list(map(float,input("введите  вещественные числа через пробел: ").split()))

# def find_difference_max_min(first_list):
#         """
#         разница между максимальным и минимальным значением дробной части элементов
#         """
#         new_list= [round(i%1,2) for i in first_list if i%1 !=0]
#         return (max(new_list) - min(new_list)) 

# print('разница между максимальным и минимальным значением дробной части элементов = ', find_difference_max_min(first_list))

# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# dvoichniy=[]
# def conv_des_v_dvoich(num):
#         """
#         рекурсивная функция. 
#         выход из фунцции при num==0
#         иначе в список dvoichniy добавляется остаток от деления на 2
#         """
#         if (num==0):
#                 return 1
#         ostatoc=num%2
#         dvoichniy.append(ostatoc)
#         conv_des_v_dvoich(num//2)


# desatich= int(input("Введите  десятичное число: "))
# conv_des_v_dvoich(desatich)
# dvoichniy.reverse()
# print("Двоичная форма числа :")
# for i in dvoichniy:
#         print(i,end=" ")



# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи


n=int(input("Введите число: "))

def get_fibbonachi (n):
        '''
        список чисел Негафибоначчи
        '''
        fibbonachi= []
        fib1,fib2=1,1
        for i in range(n-1):
                fibbonachi.append(fib1)
                fib1,fib2=fib2,fib1+fib2
        fib1,fib2=0,1
        for i in range(n):
                fibbonachi.insert(0,fib1)
                fib1,fib2= fib2,fib1-fib2
        return fibbonachi

fibbonachi = get_fibbonachi(n)
print(get_fibbonachi(n))