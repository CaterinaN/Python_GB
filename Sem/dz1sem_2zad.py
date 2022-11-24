# 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.

# def inputNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Введите значение {xyz[i]}: "))
#     return a


# def checkPredicate(x):
#     first_statum = not (x[0] or x[1] or x[2])
#     second_statum = not x[0] and not x[1] and not x[2]
#     result = first_statum == second_statum
#     return result


# statement = inputNumbers(3)

# if checkPredicate(statement) == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")


x = [0,0,0,0,1,1,1,1]
y = [0,0,1,1,0,0,1,1]
z = [0,1,0,1,0,1,0,1]
for i in [x,y,z] :
    print (x[],y[],z[])
    first_statum = not (x[0] or y[0] or z[0])
    print (first_statum)
    second_statum = not x[0] and not y[0] and not z[0]
    print (second_statum)
    if first_statum == second_statum:
        print ('True')
    else:
        print ('False')
