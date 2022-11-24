# 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.

x = int(input('Введите x : '))
y = int(input('Введите y : '))
z = int(input('Введите z : '))
if x in range (0,2) and y in range (0,2) and z in range (0,2):
    first_statum = not (x or y or z)
    second_statum = not x and not y and not z
    if first_statum == second_statum:
        print (x, y, z,'True')
    else:
        print (x, y, z,'False')
else:
    print('введите числа в двоичной системе')
