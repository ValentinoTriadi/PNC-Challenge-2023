import os,time, msvcrt, random
from colorama import Fore

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Stored Data ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

print_menu = """--===[ Dungeon of Hopeless ]===--\n
[1] Play
[2] Introduction
[ESC] Exit"""


'''---===== Struktur Data =====---'''
# Maps Awal (Array [0..26] of Array [0..69] of string)
maps  = [
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
['▒', ' ', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'], 
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', '~', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'], 
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

player = [1,2]

# Enemy ~> enemies[i][j]
# i [0..11] ~> data 12 enemy
# j [0..2] ~> 0 -> enemy ke berapa, 1 -> posisi y ( baris ke-y ), 2 -> posisi x ( kolom ke-x ), 3 -> True (Hidup) & False (Mati)
enemies = [[1, 5, 10, True], [2, 11, 16, True], [3, 11, 37, True], [4, 3, 37, True], [5, 5, 27, True], [6, 11, 49, True], [7, 11, 59, True], [8, 19, 43, True], [9, 19, 22, True], [10, 20, 6, True], [11, 22, 54, True], [12, 23, 64, True]]

# Range Enemy ~> range_enemies[i][j][k] (indeks k hanya ada pada saat j[1..2])
# i [0..11] ~> data 12 enemy
# j [0..2] ~> 0 -> enemy ke berapa, 1 -> range baris [Y_awal..Y_akhir]], 2 -> range kolom [X_awal..X_akhir]
# k [0..1] ~> 0 -> awal, 1 -> akhir
range_enemies = ((1,(3,7),(1,20)), (2, (9,13), (11,21)), (3, (9,13), (33,42)), (4, (1,5), (33,42)), (5, (3,7), (22,31)), (6, (9,13), (44,64)), (8, (15,19), (12,63)), (10, (17,23), (1,10)), (11, (21,22), (33,57)), (12, (21,25), (59,68)))

# Key ~> keys[i][j]
# i [0..2] ~> data 3 kunci
# j [0..3] ~> 0 -> kunci ke berapa, 1 -> posisi y ( baris ke-y ), 2 -> posisi x ( kolom ke-x ), 3 -> True (Belum diambil) & False (Sudah diambil)
keys = [[1, 13, 42, True], [2, 7, 22, True], [3, 22, 57, True]]

# Door ~> doors[i][j]
# i [0..2] ~> data 3 pintu
# j [0..2] ~> 0 -> pintu ke berapa, 1 -> posisi y ( baris ke-y ), 2 -> posisi x ( kolom ke-x ), 3 -> True (Belum dibuka) & False (Sudah dibuka)
doors = [[1,3,32, True], [2,1,43, True], [3,25,69, True], [4,1,0,False]]

inventory_keys = ["","",""]
kill_count = 0
next_move1 = ""
next_move2 = ""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Stored Data ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""




"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Validate Input ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

def validate(type, var1):
    if type == "menu":
        if var1 in b'\x00':
            print("[!] Menu doesn't exist [!]")
            time.sleep(1)
            return False
        elif var1 == b'1' or var1 == b'2' or var1 == b'\x1b':
            return True
        else:
            print("[!] Menu doesn't exist [!]")
            time.sleep(1)
            return False


"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Validate Input ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""




"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Game ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

def lose():
    exit()

def win_yeay():
    print(ascii("Yeay Menang"))
    exit()

def cek_keys(action):
    if action == "cek":
        for i in range(3):
            if player[0] == keys[i][1] and player[1] == keys[i][2] and keys[i][3]:
                return "~"
        return " "
    elif action == "take":
        for i in range(3):
            if player[0] == keys[i][1] and player[1] == keys[i][2] and keys[i][3]:
                keys[i][3] = False
                for i in range(3):
                    if inventory_keys[i] == "":
                        inventory_keys[i] = "~"
                        break

def cek_key_door(door):
    if inventory_keys[0] == "~" and door[0] == 1:
        return True
    elif inventory_keys[1] == "~" and door[0] == 2:
        return True
    elif inventory_keys[2] == "~" and door[0] == 3:
        return True
    return False

def cek_doors(action):
    if action == "cek":
        for i in range(4):
            if player[0] == doors[i][1] and player[1] == doors[i][2] and not doors[i][3]:
                return "▒"
            
        return " "
    elif action == "open":
        for i in range(3):
            if player[0] == doors[i][1]:
                if player[1] - 1 == doors[i][2] or player[1] + 1 == doors[i][2]:
                    if doors[i][3]:
                        if cek_key_door(doors[i]):
                            doors[i][3] = False
                            maps[doors[i][1]][doors[i][2]] = "▒"
                            break
    
def play_game():
    while True:
        os.system("cls||clear")
        for i in range(27):
            for j in range(70):
                print(maps[i][j],end="")
            if i == 2:
                print("       --===[ DUNGEON OF HOPELESS ]===--", end="")
            elif i == 4:
                print("           W", end="")
            elif i == 5:
                print("         A S D       [Spacebar]", end="")
            elif i == 6:
                print("        Movement       Attack", end="")
            elif i == 8:
                print("          [F]         [ENTER]", end="")
            elif i == 9:
                print("       Take a key    Open Gate", end="")
            elif i == 12 and inventory_keys[0] != "":
                print(f"       Keys : {inventory_keys[0]} {inventory_keys[1]} {inventory_keys[2]}", end="")
            elif i == 13 and kill_count != 0:
                print(f"       Kill Count : {kill_count}", end="")
            print()


        def enemy_movement():
            def cek_trigger():
                for i in range(10):
                    if range_enemies[i][1][0] <= player[0] <= range_enemies[i][1][1] and range_enemies[i][2][0] <= player[1] <= range_enemies[i][2][1]:
                        if i < 5:
                            if enemies[i][3]:
                                return range_enemies[i][0]
                        elif i == 5:
                            if enemies[5][3] or enemies[6][3]:
                                return range_enemies[i][0]
                        elif i == 6:
                            if enemies[7][3] or enemies[8][3]:
                                return range_enemies[i][0]
                        elif i > 6:
                            if enemies[i+2  ][3]:
                                return range_enemies[i][0]
                return -1
            anyone_triggered = cek_trigger()

            def random_move(index,i):
                global maps, enemies
                if enemies[index][3]:

                    if i > 5:
                        i -= 1
                    if i >= 7:
                        i -= 1
                    valid = False
                    x,y = enemies[index][1], enemies[index][2]
                    maps[x][y] = " "
                    while not valid:
                        x,y = enemies[index][1], enemies[index][2]
                        x += random.randint(-1,1)
                        y += random.randint(-1,1)
                        if x != enemies[index][1] and y != enemies[index][2] and maps[x][y] == " " and range_enemies[i][1][0] <= x <= range_enemies[i][1][1] and  range_enemies[i][2][0] <= y <= range_enemies[i][2][1]:
                            valid = True
                    enemies[index][1], enemies[index][2] = x,y
                    maps[x][y] = "E"

            def targeting_move(index):
                global win
                index -= 1
                
                def cek_double(x,y):
                    if maps[x][y] == "E":
                        return True
                    return False

                if index != 5 and index != 7 and enemies[index][3]:

                    maps[enemies[index][1]][enemies[index][2]] = " "
                    if maps[enemies[index][1]-1][enemies[index][2]] == "!":
                        maps[enemies[index][1]-1][enemies[index][2]] = " "

                    x,y = player[0] - enemies[index][1], player[1] - enemies[index][2]
                    if x<0 and y<0:
                        enemies[index][1] -= 1
                        enemies[index][2] -= 1
                    elif x>0 and y>0:
                        enemies[index][1] += 1
                        enemies[index][2] += 1
                    elif x>0 and y<0:
                        enemies[index][1] += 1
                        enemies[index][2] -= 1
                    elif x<0 and y>0:
                        enemies[index][1] -= 1
                        enemies[index][2] += 1
                    elif x == 0 and y > 0:
                        enemies[index][2] += 1
                    elif x == 0 and y < 0:
                        enemies[index][2] -= 1
                    elif x > 0 and y == 0:
                        enemies[index][1] += 1
                    elif x < 0 and y == 0:
                        enemies[index][1] -= 1
                    elif x == 0 and y == 0:
                        lose()

                    maps[enemies[index][1]][enemies[index][2]] = "E"
                    if player[0] == enemies[index][1] and player[1] == enemies[index][2]:
                        lose()

                elif index == 5:

                    if enemies[5][3]:
                        if maps[enemies[5][1]-1][enemies[5][2]] == "!":
                            maps[enemies[5][1]-1][enemies[5][2]] = " "
                        maps[enemies[5][1]][enemies[5][2]] = " "
                        x1,y1 = player[0] - enemies[5][1], player[1] - enemies[5][2]

                        if x1<0 and y1<0:
                            enemies[5][1] -= 1
                            enemies[5][2] -= 1
                            if cek_double(enemies[5][1],enemies[5][2]):
                                enemies[5][1] += 1
                                enemies[5][2] += 1

                        elif x1>0 and y1>0:
                            enemies[5][1] += 1
                            enemies[5][2] += 1
                            if cek_double(enemies[5][1],enemies[5][2]):
                                enemies[5][1] -= 1
                                enemies[5][2] -= 1
                        elif x1>0 and y1<0:
                            enemies[5][1] += 1
                            enemies[5][2] -= 1
                            if cek_double(enemies[5][1],enemies[5][2]):
                                enemies[5][1] -= 1
                                enemies[5][2] += 1
                        elif x1<0 and y1>0:
                            enemies[5][1] -= 1
                            enemies[5][2] += 1
                            if cek_double(enemies[5][1],enemies[5][2]):
                                enemies[5][1] += 1
                                enemies[5][2] -= 1
                        elif x1 == 0 and y1 > 0:
                            enemies[5][2] += 1
                            if cek_double(enemies[5][1],enemies[5][2]):
                                enemies[5][2] -= 1
                        elif x1 == 0 and y1 < 0:
                            enemies[5][2] -= 1
                            if cek_double(enemies[5][1],enemies[5][2]):
                                enemies[5][2] += 1
                        elif x1 > 0 and y1 == 0:
                            enemies[5][1] += 1
                            if cek_double(enemies[5][1],enemies[5][2]):
                                enemies[5][1] -= 1
                        elif x1 < 0 and y1 == 0:
                            enemies[5][1] -= 1
                            if cek_double(enemies[5][1],enemies[5][2]):
                                enemies[5][1] += 1
                        elif x1 == 0 and y1 == 0:
                            lose()
                        
                        maps[enemies[5][1]][enemies[5][2]] = "E"
                        if player[0] == enemies[5][1] and player[1] == enemies[5][2]:
                            lose()

                    if enemies[6][3]:
                        if maps[enemies[6][1]-1][enemies[6][2]] == "!":
                            maps[enemies[6][1]-1][enemies[6][2]] = " "
                        maps[enemies[6][1]][enemies[6][2]] = " "
                        x2,y2 = player[0] - enemies[6][1], player[1] - enemies[6][2]
                        if x2<0 and y2<0:
                            enemies[6][1] -= 1
                            enemies[6][2] -= 1
                            if cek_double(enemies[6][1],enemies[6][2]):
                                enemies[6][1] += 1
                                enemies[6][2] += 1

                        elif x2>0 and y2>0:
                            enemies[6][1] += 1
                            enemies[6][2] += 1
                            if cek_double(enemies[6][1],enemies[6][2]):
                                enemies[6][1] -= 1
                                enemies[6][2] -= 1
                        elif x2>0 and y2<0:
                            enemies[6][1] += 1
                            enemies[6][2] -= 1
                            if cek_double(enemies[6][1],enemies[6][2]):
                                enemies[6][1] -= 1
                                enemies[6][2] += 1
                        elif x2<0 and y2>0:
                            enemies[6][1] -= 1
                            enemies[6][2] += 1
                            if cek_double(enemies[6][1],enemies[6][2]):
                                enemies[6][1] += 1
                                enemies[6][2] -= 1
                        elif x2 == 0 and y2 > 0:
                            enemies[6][2] += 1
                            if cek_double(enemies[6][1],enemies[6][2]):
                                enemies[6][2] -= 1
                        elif x2 == 0 and y2 < 0:
                            enemies[6][2] -= 1
                            if cek_double(enemies[6][1],enemies[6][2]):
                                enemies[6][2] += 1
                        elif x2 > 0 and y2 == 0:
                            enemies[6][1] += 1
                            if cek_double(enemies[6][1],enemies[6][2]):
                                enemies[6][1] -= 1
                        elif x2 < 0 and y2 == 0:
                            enemies[6][1] -= 1
                            if cek_double(enemies[6][1],enemies[6][2]):
                                enemies[6][1] += 1
                        elif x2 == 0 and y2 == 0:
                            lose()
                        
                        maps[enemies[6][1]][enemies[6][2]] = "E"
                        if player[0] == enemies[6][1] and player[1] == enemies[6][2]:
                            lose()

                elif index == 7:
                    global next_move1, next_move2
                    
                    def cek_wall(x,y,opx,opy):
                        if maps[x][y] == "#":
                            x -= opx
                            y -= opy
                            xawal, yawal = x,y
                            valid = False
                            go = "down"
                            while not valid:
                                if go == "down":
                                    if maps[x][y + opy] == "#" and maps[x+1][y] != "#":
                                        x += 1
                                    elif maps[x][y + opy] == " ":
                                        valid = True
                                    else:
                                        go = "up"

                                else:
                                    if maps[x][y + opy] == "#" and maps[x-1][y] != "#":
                                        x -= 1
                                    elif maps[x][y + opy] == " ":
                                        valid = True
                            return go,xawal,yawal
                        return "",x,y
                    
                    def is_done(x, y, moves):
                        if moves == 'left' or moves == 'right':
                            if maps[x-1][y] == " " or maps[x+1][y] == " ":
                                return ''
                        elif moves == 'up':
                            if maps[x][y+1] == " " and maps[x+1][y+1] == "#":
                                return True, 'right'
                            if maps[x][y-1] == " " and maps[x+1][y-1] == "#":
                                return True, 'left'
                            return False, ''
                        elif moves == 'down':
                            if maps[x][y+1] == " " and maps[x-1][y+1] == "#":
                                return True, 'right'
                            if maps[x][y-1] == " " and maps[x-1][y-1] == "#":
                                return True, 'left'
                            return False, ''
                    
                    if enemies[7][3]:

                        if maps[enemies[7][1]-1][enemies[7][2]] == "!":
                            maps[enemies[7][1]-1][enemies[7][2]] = " "
                        maps[enemies[7][1]][enemies[7][2]] = " "
                        x1,y1 = player[0] - enemies[7][1], player[1] - enemies[7][2]
                        xx1,yy1 = enemies[7][1], enemies[7][2]

                        if next_move1 == "up":
                            xx1 -= 1
                            if cek_double(xx1,yy1):
                                xx1 += 1
                            if is_done(xx1,yy1,'up')[0]:
                                next_move1 = is_done(xx1,yy1,'up')[1]
                        elif next_move1 == "down":
                            xx1 += 1
                            if cek_double(xx1,yy1):
                                xx1 -= 1
                            if is_done(xx1,yy1,'down')[0]:
                                next_move1 = is_done(xx1,yy1,'down')[1]
                        elif next_move1 == 'left':
                            yy1 -= 1
                            if cek_double(xx1,yy1):
                                yy1 += 1
                            next_move1 = is_done(xx1,yy1,'left')
                        elif next_move1 == 'right':
                            yy1 += 1
                            if cek_double(xx1,yy1):
                                yy1 -= 1
                            next_move1 = is_done(xx1,yy1,'right')
                        elif x1<0 and y1<0:
                            xx1 -= 1
                            yy1 -= 1
                            if cek_double(xx1,yy1):
                                xx1 += 1
                                yy1 += 1
                            next_move1, xx1, yy1 = cek_wall(xx1,yy1,-1,-1)
                        elif x1>0 and y1>0:
                            xx1 += 1
                            yy1 += 1
                            if cek_double(xx1,yy1):
                                xx1 -= 1
                                yy1 -= 1
                            next_move1, xx1, yy1 = cek_wall(xx1,yy1,1,1)
                        elif x1>0 and y1<0:
                            xx1 += 1
                            yy1 -= 1
                            if cek_double(xx1,yy1):
                                xx1 -= 1
                                yy1 += 1
                            next_move1, xx1, yy1 = cek_wall(xx1,yy1,1,-1)
                        elif x1<0 and y1>0:
                            xx1 -= 1
                            yy1 += 1
                            if cek_double(xx1,yy1):
                                xx1 += 1
                                yy1 -= 1
                            next_move1, xx1, yy1 = cek_wall(xx1,yy1,-1,1)
                        elif x1 == 0 and y1 > 0:
                            yy1 += 1
                            if cek_double(xx1,yy1):
                                yy1 -= 1
                            next_move1, xx1, yy1 = cek_wall(xx1,yy1,0,1)
                        elif x1 == 0 and y1 < 0:
                            yy1 -= 1
                            if cek_double(xx1,yy1):
                                yy1 += 1
                            next_move1, xx1, yy1 = cek_wall(xx1,yy1,0,-1)
                        elif x1 > 0 and y1 == 0:
                            xx1 += 1
                            if cek_double(xx1,yy1):
                                xx1 -= 1
                            next_move1, xx1, yy1 = cek_wall(xx1,yy1,1,0)
                        elif x1 < 0 and y1 == 0:
                            xx1 -= 1
                            if cek_double(xx1,yy1):
                                xx1 += 1
                            next_move1, xx1, yy1 = cek_wall(xx1,yy1,-1,0)
                        elif x1 == 0 and y1 == 0:
                            lose()

                        enemies[7][1], enemies[7][2] = xx1,yy1 
                        maps[enemies[7][1]][enemies[7][2]] = "E"                        
                        if player[0] == enemies[7][1] and player[1] == enemies[7][2]:
                            lose()

                    if enemies[8][3]:

                        if maps[enemies[8][1]-1][enemies[8][2]] == "!":
                            maps[enemies[8][1]-1][enemies[8][2]] = " "
                        maps[enemies[8][1]][enemies[8][2]] = " "
                        x2,y2 = player[0] - enemies[8][1], player[1] - enemies[8][2]
                        xx2,yy2 = enemies[8][1], enemies[8][2]

                        if next_move2 == "up":
                            xx2 -= 1
                            if cek_double(xx2,yy2):
                                xx2 += 1
                            if is_done(xx2,yy2,'up')[0]:
                                next_move2 = is_done(xx2,yy2,'up')[1]
                        elif next_move2 == "down":
                            xx2 += 1
                            if cek_double(xx2,yy2):
                                xx2 -= 1
                            if is_done(xx2,yy2,'down')[0]:
                                next_move2 = is_done(xx2,yy2,'down')[1]
                        elif next_move2 == 'left':
                            yy2 -= 1
                            if cek_double(xx2,yy2):
                                yy2 += 1
                            next_move2 = is_done(xx2,yy2,'left')
                        elif next_move2 == 'right':
                            yy2 += 1
                            if cek_double(xx2,yy2):
                                yy2 -= 1
                            next_move2 = is_done(xx2,yy2,'right')
                        elif x2<0 and y2<0:
                            xx2 -= 1
                            yy2 -= 1
                            if cek_double(xx2,yy2):
                                xx2 += 1
                                yy2 += 1
                            next_move2, xx2, yy2 = cek_wall(xx2,yy2,-1,-1)
                        elif x2>0 and y2>0:
                            xx2 += 1
                            yy2 += 1
                            if cek_double(xx2,yy2):
                                xx2 -= 1
                                yy2 -= 1
                            next_move2, xx2, yy2 = cek_wall(xx2,yy2,1,1)
                        elif x2>0 and y2<0:
                            xx2 += 1
                            yy2 -= 1
                            if cek_double(xx2,yy2):
                                xx2 -= 1
                                yy2 += 1
                            next_move2, xx2, yy2 = cek_wall(xx2,yy2,1,-1)
                        elif x2<0 and y2>0:
                            xx2 -= 1
                            yy2 += 1
                            if cek_double(xx2,yy2):
                                xx2 += 1
                                yy2 -= 1
                            next_move2, xx2, yy2 = cek_wall(xx2,yy2,-1,1)
                        elif x2 == 0 and y2 > 0:
                            yy2 += 1
                            if cek_double(xx2,yy2):
                                yy2 -= 1
                            next_move2, xx2, yy2 = cek_wall(xx2,yy2,0,1)
                        elif x2 == 0 and y2 < 0:
                            yy2 -= 1
                            if cek_double(xx2,yy2):
                                yy2 += 1
                            next_move2, xx2, yy2 = cek_wall(xx2,yy2,0,-1)
                        elif x2 > 0 and y2 == 0:
                            xx2 += 1
                            if cek_double(xx2,yy2):
                                xx2 -= 1
                            next_move2, xx2, yy2 = cek_wall(xx2,yy2,1,0)
                        elif x2 < 0 and y2 == 0:
                            xx2 -= 1
                            if cek_double(xx2,yy2):
                                xx2 += 1
                            next_move2, xx2, yy2 = cek_wall(xx2,yy2,-1,0)
                        elif x2 == 0 and y2 == 0:
                            lose()

                        enemies[8][1], enemies[8][2] = xx2,yy2
                        maps[enemies[8][1]][enemies[8][2]] = "E"
                        if player[0] == enemies[8][1] and player[1] == enemies[8][2]:
                            lose()

            if anyone_triggered != -1:
                if anyone_triggered < 6 or anyone_triggered >= 10:
                    targeting_move(anyone_triggered)
                    if maps[enemies[anyone_triggered - 1][1]-1][enemies[anyone_triggered - 1][2]] == " ":
                        maps[enemies[anyone_triggered - 1][1]-1][enemies[anyone_triggered - 1][2]] = "!"
                    for i in range(12):
                        if i != anyone_triggered - 1 and enemies[i][3]:
                            random_move(i,i)
                    
                elif anyone_triggered == 6 or anyone_triggered == 8:
                    targeting_move(anyone_triggered)
                    if enemies[anyone_triggered - 1][3]:
                        if maps[enemies[anyone_triggered - 1][1]-1][enemies[anyone_triggered - 1][2]] == " ":
                            maps[enemies[anyone_triggered - 1][1]-1][enemies[anyone_triggered - 1][2]] = "!"
                    if enemies[anyone_triggered][3]:
                        if maps[enemies[anyone_triggered][1]-1][enemies[anyone_triggered][2]] == " ":
                            maps[enemies[anyone_triggered][1]-1][enemies[anyone_triggered][2]] = "!"
                    for i in range(12):
                        if i != anyone_triggered - 1 and i != anyone_triggered and enemies[i][3]:
                            random_move(i,i)
            else:
                for i in range(12):
                    if enemies[i][3]:
                        if maps[enemies[i][1]-1][enemies[i][2]] == "!":
                            maps[enemies[i][1]-1][enemies[i][2]] = " "
                        random_move(i,i)


        def move(action):
            global kill_count, maps
            if action == "up":
                key = cek_keys("cek")
                door = cek_doors("cek")
                if key == "~" and maps[player[0]-1][player[1]] == ' ':
                    maps[player[0]-1][player[1]] = "P"
                    maps[player[0]][player[1]] = "~"
                    player[0] -= 1
                elif door == "▒" and maps[player[0]-1][player[1]] == ' ':
                    maps[player[0]-1][player[1]] = "P"
                    maps[player[0]][player[1]] = "▒"
                    player[0] -= 1
                elif maps[player[0]-1][player[1]] == ' ':
                    maps[player[0]-1][player[1]] = "P"
                    maps[player[0]][player[1]] = " "
                    player[0] -= 1
                elif maps[player[0]-1][player[1]] == '▒':
                    maps[player[0]-1][player[1]] = "P"
                    maps[player[0]][player[1]] = " "
                    player[0] -= 1
                elif maps[player[0]-1][player[1]] == 'E':
                    lose()
                elif maps[player[0]-1][player[1]] == '~':
                    maps[player[0]-1][player[1]] = "P"
                    maps[player[0]][player[1]] = " "
                    player[0] -= 1
                    
            elif action == "down":
                key = cek_keys("cek")
                door = cek_doors("cek")
                if key == "~" and maps[player[0]+1][player[1]] == ' ':
                    maps[player[0]+1][player[1]] = "P"
                    maps[player[0]][player[1]] = "~"
                    player[0] += 1
                elif door == "▒" and maps[player[0]+1][player[1]] == ' ':
                    maps[player[0]+1][player[1]] = "P"
                    maps[player[0]][player[1]] = "▒"
                    player[0] += 1
                elif maps[player[0]+1][player[1]] == ' ':
                    maps[player[0]+1][player[1]] = "P"
                    maps[player[0]][player[1]] = " "
                    player[0] += 1
                elif maps[player[0]+1][player[1]] == '▒':
                    maps[player[0]+1][player[1]] = "P"
                    maps[player[0]][player[1]] = " "
                    player[0] += 1
                elif maps[player[0]+1][player[1]] == 'E':
                    lose()
                elif maps[player[0]+1][player[1]] == '~':
                    maps[player[0]+1][player[1]] = "P"
                    maps[player[0]][player[1]] = " "
                    player[0] += 1
                
            elif action == "left":
                key = cek_keys("cek")
                door = cek_doors("cek")
                if key == "~" and maps[player[0]][player[1]-1] == ' ':
                    maps[player[0]][player[1]-1] = "P"
                    maps[player[0]][player[1]] = "~"
                    player[1] -= 1
                elif maps[player[0]][player[1]-1] == '▒' and player[0] == 1 and player[1] - 1 == 0:
                    maps[player[0]][player[1]-1] = "P"
                    maps[player[0]][player[1]] = " "
                    player[1] -= 1
                    start_menu()
                elif door == "▒" and maps[player[0]][player[1]-1] == ' ':
                    maps[player[0]][player[1]-1] = "P"
                    maps[player[0]][player[1]] = "▒"
                    player[1] -= 1
                elif maps[player[0]][player[1]-1] == ' ':
                    maps[player[0]][player[1]-1] = "P"
                    maps[player[0]][player[1]] = " "
                    player[1] -= 1
                elif maps[player[0]][player[1]-1] == '▒':
                    maps[player[0]][player[1]-1] = "P"
                    maps[player[0]][player[1]] = " "
                    player[1] -= 1
                elif maps[player[0]][player[1]-1] == 'E':
                    lose()
                elif maps[player[0]][player[1]-1] == '~':
                    maps[player[0]][player[1]-1] = "P"
                    maps[player[0]][player[1]] = " "
                    player[1] -= 1

            elif action == "right":
                key = cek_keys("cek")
                door = cek_doors("cek")
                if key == "~" and maps[player[0]][player[1]+1] == ' ':
                    maps[player[0]][player[1]+1] = "P"
                    maps[player[0]][player[1]] = "~"
                    player[1] += 1
                elif maps[player[0]][player[1]+1] == '▒' and player[0] == doors[2][1] and player[1] + 1 == doors[2][2]:
                    maps[player[0]][player[1]+1] = "P"
                    maps[player[0]][player[1]] = " "
                    player[1] += 1
                    win_yeay()
                elif door == "▒" and maps[player[0]][player[1]+1] == ' ':
                    maps[player[0]][player[1]+1] = "P"
                    maps[player[0]][player[1]] = "▒"
                    player[1] += 1
                elif maps[player[0]][player[1]+1] == ' ':
                    maps[player[0]][player[1]+1] = "P"
                    maps[player[0]][player[1]] = " "
                    player[1] += 1
                elif maps[player[0]][player[1]+1] == '▒':
                    maps[player[0]][player[1]+1] = "P"
                    maps[player[0]][player[1]] = " "
                    player[1] += 1
                elif maps[player[0]][player[1]+1] == 'E':
                    lose()
                elif maps[player[0]][player[1]+1] == '~':
                    maps[player[0]][player[1]+1] = "P"
                    maps[player[0]][player[1]] = key
                    player[1] += 1
                
            elif action == "take":
                cek_keys("take")

            elif action == "attack":
                if maps[player[0]+1][player[1]] == " ":
                    maps[player[0]+1][player[1]] = "@"
                if maps[player[0]-1][player[1]] == " ":
                    maps[player[0]-1][player[1]] = "@"
                if maps[player[0]][player[1]+1] == " ":
                    maps[player[0]][player[1]+1] = "@"
                if maps[player[0]][player[1]-1] == " ":
                    maps[player[0]][player[1]-1] = "@"
                
                def kill(x,y):
                    global kill_count, maps
                    kill_count += 1
                    if maps[x-1][y] == "!":
                        maps[x-1][y] = " "
                    for i in range(12):
                        if enemies[i][1] == x and enemies[i][2] == y:
                            enemies[i][3] = False
                            

                if maps[player[0]+1][player[1]] == "E": 
                    maps[player[0]+1][player[1]] = "@"
                    kill(player[0]+1,player[1])
                if maps[player[0]-1][player[1]] == "E":
                    maps[player[0]-1][player[1]] = "@"
                    kill(player[0]-1,player[1])
                if maps[player[0]][player[1]+1] == "E":
                    maps[player[0]][player[1]+1] = "@"
                    kill(player[0],player[1]+1)
                if maps[player[0]][player[1]-1] == "E":
                    maps[player[0]][player[1]-1] = "@"
                    kill(player[0],player[1]-1)

                os.system("cls||clear")
                for i in range(27):
                    for j in range(70):
                        print(maps[i][j],end="")
                    if i == 2:
                        print("       --===[ DUNGEON OF HOPELESS ]===--", end="")
                    elif i == 4:
                        print("           W", end="")
                    elif i == 5:
                        print("         A S D       [Spacebar]", end="")
                    elif i == 6:
                        print("        Movement       Attack", end="")
                    elif i == 8:
                        print("          [F]         [ENTER]", end="")
                    elif i == 9:
                        print("       Take a key    Open Gate", end="")
                    elif i == 12 and inventory_keys[0] != "":
                        print(f"       Keys : {inventory_keys[0]} {inventory_keys[1]} {inventory_keys[2]}", end="")
                    elif i == 13 and kill_count != 0:
                        print(f"       Kill Count : {kill_count}", end="")
                    print()


                if maps[player[0]+1][player[1]] == "@":
                    maps[player[0]+1][player[1]] = " "
                if maps[player[0]-1][player[1]] == "@":
                    maps[player[0]-1][player[1]] = " "
                if maps[player[0]][player[1]+1] == "@":
                    maps[player[0]][player[1]+1] = " "
                if maps[player[0]][player[1]-1] == "@":
                    maps[player[0]][player[1]-1] = " "

            elif action == "open":
                cek_doors("open")
            
        ch = msvcrt.getch()
        if ch in b'\x00':
            ch = msvcrt.getch()
        if ch == b'w':
            move("up")
        elif ch == b'a':
            move("left")
        elif ch == b's':
            move("down")
        elif ch == b'd':
            move("right")
        elif ch == b'f':
            move("take")
        elif ch == b' ':
            move("attack")
        elif ch == b'\r':
            move("open")

        enemy_movement()



"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Game ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""




"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Introduction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

def introduction():
    os.system("cls||clear")
    print("--=== How To Play ===--".center(60," ") + Fore.LIGHTCYAN_EX + """

[W]        : Move Up
[S]        : Move Down
[A]        : Move Left
[D]        : Move Right
[SPACEBAR] : Attack
[F]        : Take Item
[ENTER]    : Open Gate
""" + Fore.LIGHTGREEN_EX +
"""
P --> Player
E --> Enemy
~ --> Key
| --> Closed Gate
▒ --> Opened Gate
""" + Fore.WHITE + 
"""
Tips to play :
There is some tips to play this game :
 - To kill enemy, u must stand next to the enemy to kill it
 - To taking key, u must stand on the key
 - To Open the gate, u must have the right key and stand next to the gate to open it
 - For full guide to play this game, open FULLGUIDE.pdf""")
    print(Fore.YELLOW + "\n[!] Press Any Key To Go Back To The Main Menu [!]" + Fore.WHITE)
    msvcrt.getch()
    start_menu()

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Introduction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""




"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

def start_menu():
    pilih = 0
    valid = False
    
    while not valid:

        try:
            os.system("cls||clear")
            print(print_menu)
            print('>>>', end=" ")
            pilih = msvcrt.getch()
            valid = validate("menu", pilih)
        except ValueError:
            print("[!] Input Tidak Valid [!]")
            time.sleep(1)
    
    if pilih == b'\x1b':
        os.system("cls||clear")
        print(print_menu)
        print()
        print(Fore.LIGHTGREEN_EX + "[!] Closing Program in 3.. [!]" + Fore.WHITE)
        time.sleep(1)
        os.system("cls||clear")
        print(print_menu)
        print()
        print(Fore.YELLOW + "[!] Closing Program in 2.. [!]" + Fore.WHITE)
        time.sleep(1)
        os.system("cls||clear")
        print(print_menu)
        print()
        print(Fore.LIGHTRED_EX + "[!] Closing Program in 1.. [!]" + Fore.WHITE)
        time.sleep(1)
        os.system("cls||clear")
        print(print_menu)
        print()
        print(Fore.LIGHTBLUE_EX + "[!] Thank You For Playing [!]")
        time.sleep(1)
        os.system("cls||clear")
        exit()
    elif pilih == b'1':
        play_game()
    elif pilih == b'2':
        introduction()
    
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""


start_menu()