
# дз
# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "галок" => Пугать ты пугай
# Пугать ты галок пугай => заданная строка "пуг" => Пугать ты галок

# все слово нужно ввести
# my_text= "Пугать ты галок пугай".split()
# del_word = input('тескт:"Пугать ты галок пугай" введитe слово для удаления его из текста :  ')
# my_text.remove(del_word)
# print("получившийся текст :",(my_text))


# с фильтром любой фрагмент слова
# my_text= "Пугать ты галок пугай".split()
# del_word = input('тескт:"Пугать ты галок пугай" введитe слово для удаления его из текста :  ')

# delete_word_in_text = ' '.join((filter(lambda e :del_word not in e,my_text)))
# print(delete_word_in_text )




# 2-Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021(или сколько вы скажете) конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28(или сколько вы зададите в начале) конфет. Все конфеты оппонента достаются сделавшему последний ход. Сделайте эту игру.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""



# def candy_game (all_candy,take_max_candy):
#     """
#     игра с конфетами ( на вход общее количество конфет и сколько конфет
#     можно взять за один ход)
#     """

#     player = name_first_player
#     while all_candy!=0:
#         take_candy= int(input(f"{player} берет конфеты : "))
#         if all_candy-take_candy<0 or take_candy>take_max_candy:
#             print(" слишком много :) Возьми меньше конфет ")
#         else:
#             all_candy= all_candy-take_candy
#             print(f"{player} взял {take_candy} осталось {all_candy} конфет")
#             if all_candy ==0:
#                 print(f" игрок {player} выйграл! поздравляем!")
#             if player == name_first_player:
#                 player = name_second_player
#             else :
#                 player = name_first_player


# all_candy= int(input('введите количество конфет: '))
# take_max_candy = int(input("сколько конфет можно взять за один раз?  "))
# name_first_player= input('введите имя первого игрока : ')
# name_second_player= input('введите имя второго игрока : ')
# candy_game (all_candy,take_max_candy)




# # 3-Создайте программу для игры в ""Крестики-нолики"".



def welcome():
    """
    приветствие
    """
    print('         чтобы сделать ход,      ')
    print('   ведите координаты x и y черезе пробел:')
    print('         x - номер строки        ')
    print('         y - номер столбца       ')


def create_game_map():
    """
    создаем поле игры
    """
    print()
    print('  | 1 | 2 | 3 |')
    print('---------------')
    for i, row in enumerate(map_play, start=1):
        print(f'{i} | {" | ".join(row)} |')
        print('---------------')
    print()


def inp_xy(step):

    """
    ввод x и у координат
    """

    while True:
        if step % 2 == 1:
            print(f'{step} ход, {player_1}: ')
        else:
            print(f'{step} ход, {player_2}: ')
        coord_xy = input().split()

        if len(coord_xy) != 2:
            print('Нужно ввести 2 координаты: X и Y!')
            continue

        x, y = coord_xy

        if not x.isdigit() or not y.isdigit():
            print('Координаты X и Y должны быть положительными числами!')
            continue

        x, y = int(x), int(y)

        if (x < 1 or x > 3) or (y < 0 or y > 3):
            print(f'Введенные координаты x={x}, y={y} вне игрового поля!')
            continue
        
        if map_play[x - 1][y - 1] != ' ':
            if step % 2 == 1:
                print(f'{player_1}, внимательнее! :) выбранная клетка x={x}, y={y} уже занята! введи координаты верно. ')
            else:
                print(f'{player_2}, мимо :) выбранная клетка x={x}, y={y} уже занята! введи координаты верно ')
            continue

        return x, y


def game_win():
    """
    проверка победителя
    """
    win_tab = (
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2))
    )

    for tab in win_tab:
        win_list = []
        for i in tab:
            win_list.append(map_play[i[0]][i[1]])
        if win_list == ['X', 'X', 'X']:
            create_game_map()
            print(f'Победитель - {player_1}!!!')
            return True
        if win_list == ['0', '0', '0']:
            create_game_map()
            print(f'Победитель - {player_2}!!!')
            return True

    return False


welcome()

map_play = [[' '] * 3 for _ in range(3)]
step = 0
player_1= input('Введите имя первого игрока,он играет за Х : ')
player_2= input('Введите имя второго игрока,он играет за О : ')
while True:
    step += 1
    create_game_map()
    if step == 10:
        print('Победителя нет! Сражайтесь сново!')
        break

    x, y = inp_xy(step)

    if step % 2 == 1:
        map_play[x - 1][y - 1] = "X"
    else:
        map_play[x - 1][y - 1] = "0"

    if game_win():
        break