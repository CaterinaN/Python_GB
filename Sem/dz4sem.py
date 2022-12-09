
# дз
# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

# number =int(input("Ведите натуральное число N : "))
# def factor_n(number):
#     '''
#     Поиск простых множителей числа 
#     '''
#     list_factor = []
#     fact = 2
#     while fact * fact <= number:
#         if number % fact == 0:
#             if fact not in list_factor:
#                 list_factor.append(fact)
#             number //= fact
#         else:
#             fact += 1
#     if number > 1:
#         list_factor.append(number)
#     return list_factor


# print("простые множители числа",number,"->", factor_n(number))


# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]


# numbers= list(map(int,input("Введите числа через пробел : " ).split()))

# def non_repeating (numbers):
#     """
#     выведет список неповторяющихся элементов исходной последовательности
#     """
#     new_list=[]
#     for i in numbers:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list

# print(non_repeating (numbers))


# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов, которые имеют средний балл более «4».


# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4



# def write_to_file(file):
#     '''
#     сщздание файла 3sem3zad.txt с текстом
#     '''
#     with open('3sem3zad.txt',"w",encoding="utf-8") as file:
#         file.writelines('Ангела Меркель 5\n' 'Энакин Скайуокер 5\n' 'Фредди Меркури 3\n' 'Александр Пушкин 4\n')


# def file_to_spisok(file):
#     '''
#     создание списка из файла
#     '''
#     with open ('3sem3zad.txt',"r",encoding="utf-8") as file:
#         file_spisok=file.readlines()
#         file_spisok= [line.rstrip('\n') for line in file_spisok]

#     return file_spisok



# def serch_student (file_spisok):
#     '''
#     поиск в списке студента с оценкой выше 5 и замнена букв на верхний регистр
#     '''
#     sr_count='5'
#     new_file_spisok =''
#     for i in file_spisok:
#         if i.count(sr_count):
#             i = i.upper()
#         student=i + '\n'
#         new_file_spisok+=student
#     return new_file_spisok



# def change_file(file):
#     '''
#     запись измененного списка в файл
#     '''
#     with open ('3sem3zad.txt',"w",encoding="utf-8") as file:
#         file.write(serch_student (file_spisok))



# write_to_file('3sem3zad.txt')
# file_spisok = file_to_spisok('3sem3zad.txt')
# print(file_spisok)
# print(serch_student (file_spisok))
# change_file('3sem3zad.txt')


# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.



# import string

# def crypt (text: str, key: int, decrypt:bool= False):
#     text_for_crypt =''
#     key =-key if decrypt else key

#     for i in text:
#         index=all_simvols.find(i)
#         index=(index+key)%len(all_simvols)
#         text_for_crypt+=all_simvols[index]
#     return text_for_crypt


# def write_to_file(file):
#     '''
#     создание файла crypt.txt с текстом
#     '''
#     with open('crypt.txt',"w",encoding="utf-8") as file:
#         file.writelines(text_for_crypt)


# def crypt_write_to_file(file):
#     '''
#     создание файла crypt.txt с текстом
#     '''
#     with open('crypt.txt',"w",encoding="utf-8") as file:
#         file.writelines(crypt(text_for_crypt, key,False))

# def derypt_write_to_file(file):
#     '''
#     создание файла crypt.txt с текстом
#     '''
#     with open('crypt.txt',"w",encoding="utf-8") as file:
#         file.writelines(crypt((crypt(text_for_crypt, key,False)), key,True))


# all_simvols =(''.join([chr(i) for i in range(1072,1104)]))+string.punctuation + string.ascii_letters 
# print(all_simvols)
# text_for_crypt='крошка сын к отцу пришёл,и спросила кроха:— что такое хорошо и что такое плохо?'
# write_to_file('crypt.txt') 
# key=int(input("Введите ключ шифрования(дешифрования) : "))
# crypt_write_to_file('crypt.txt') 
# key=int(input("Введите ключ дешифрования : "))
# derypt_write_to_file('crypt.txt')


# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol
# Первая функция - текст зашифровывает
# Вторая - расшифровывает
# Две промежуточные - считывают с файла и записывают в файл

text_for_crypt='AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool'

def crypt_rla(file):
    '''
    RLA сжатие
    '''
    count = 1
    rla_crypt = ''
    for i in range(len(text_for_crypt)-1):
        if text_for_crypt[i] == text_for_crypt[i+1]:
            count += 1
        else:
            rla_crypt = rla_crypt + str(count) + text_for_crypt[i]
            count = 1
    if count > 1 or (text_for_crypt[len(text_for_crypt)-2] != text_for_crypt[-1]):
        rla_crypt = rla_crypt + str(count) + text_for_crypt[-1]
    return rla_crypt

def decrypt_rla():
    '''
    RLA восстановления данных
    '''
    with open('crypt_rla.txt','r') as file:
        text_for_decrput = file.read()
        index=0
        count ='0'
        decrypt_text= ''
        while index< len(text_for_decrput):
            if text_for_decrput[index].isdigit():
                count+= text_for_decrput[index]
            elif count == '':
                decrypt_text+= text_for_decrput[index]
            else:
                decrypt_text+=text_for_decrput[index] * int(count)
                count = ''
            index+=1
    return decrypt_text

def write_crypt_file(file):
    '''
    создание файла crypt_rla.txt с текстом
    '''
    with open('crypt_rla.txt',"w",encoding="utf-8") as file:
        file.writelines(crypt_rla(text_for_crypt))


def write_decrypt_file(file):
    '''
    создание файла decrypt_rla.txt с текстом
    '''
    with open('decrypt_rla.txt',"w",encoding="utf-8") as file:
        file.writelines(decrypt_rla())


write_crypt_file('crypt_rla.txt') 
write_decrypt_file('decrypt_rla.txt')