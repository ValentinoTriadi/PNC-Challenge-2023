import os, msvcrt, time
from colorama import Fore

"""======================================================= Variable Description ======================================================="""
# standard_small, standard_large, premier_small, premier_large : array of room map

# data_standard_small, data_standard_large, data_premier_small, data_premier_large : array [0 -> room map
#                                                                                           1 -> vertical length
#                                                                                           2 -> horizontal length
#                                                                                           3 -> total seat unoccupied]

# data_penonton_standard_small, data_penonton_standard_large, data_penonton_premier_small, data_penonton_premier_large : [Seat Number, Name, Date] [Seat Number, Name, Date] ...
#                                                                                                                        [Seat Number, Name, Date] [Seat Number, Name, Date] ...
#                                                                                                                        [Seat Number, Name, Date] [Seat Number, Name, Date] ...
#                                                                                                                        [Seat Number, Name, Date] [Seat Number, Name, Date] ...
#                                                                                                                        ...

# data_film = list of film

"""======================================================= Variable Description ======================================================="""


standard_small = [
["[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]"],
["[][]", "====", "====", "====", "====", "====", "====", "====", "[][]"],
["[][]", "[A1]", "[A2]", "[A3]", "    ", "[A4]", "[A5]", "[A6]", "[][]"],
["[][]", "[B1]", "[B2]", "[B3]", "    ", "[B4]", "[B5]", "[B6]", "[][]"],
["[][]", "[C1]", "[C2]", "[C3]", "    ", "[C4]", "[C5]", "[C6]", "[][]"],
["[][]", "[D1]", "[D2]", "[D3]", "    ", "[D4]", "[D5]", "[D6]", "[][]"],
["[][]", "[E1]", "[E2]", "[E3]", "    ", "[E4]", "[E5]", "[E6]", "[][]"],
["[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]"]
]
data_standard_small = [standard_small, 8, 9, 30]
data_penonton_standard_small = [[[f"[{chr(65+i)}{j+1}]","",""] for j in range(6)] for i in range(5)] # Array [0..5] of array [0..6] of array [0..3] of string

premier_small =[
["[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]"],
["[][]", "====", "====", "====", "====", "====", "====", "====", "====", "[][]"],
["[][]", "[A1]", "[A2]", "    ", "[A3]", "[A4]", "    ", "[A5]", "[A6]", "[][]"],
["[][]", "[B1]", "[B2]", "    ", "[B3]", "[B4]", "    ", "[B5]", "[B6]", "[][]"],
["[][]", "[C1]", "[C2]", "    ", "[C3]", "[C4]", "    ", "[C5]", "[C6]", "[][]"],
["[][]", "[D1]", "[D2]", "    ", "[D3]", "[D4]", "    ", "[D5]", "[D6]", "[][]"],
["[][]", "[E1]", "[E2]", "    ", "[E3]", "[E4]", "    ", "[E5]", "[E6]", "[][]"],
["[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]"]
]
data_premier_small = [premier_small, 8, 10, 30]
data_penonton_premier_small = [[[f"[{chr(65+i)}{j+1}]","",""] for j in range(6)] for i in range(5)] # Array [0..5] of array [0..6] of array [0..3] of string

standard_large = [
["[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]"],
["[][]", "====", "====", "====", "====", "====", "====", "====", "[][]"],
["[][]", "[A1]", "[A2]", "[A3]", "    ", "[A4]", "[A5]", "[A6]", "[][]"],
["[][]", "[B1]", "[B2]", "[B3]", "    ", "[B4]", "[B5]", "[B6]", "[][]"],
["[][]", "[C1]", "[C2]", "[C3]", "    ", "[C4]", "[C5]", "[C6]", "[][]"],
["[][]", "[D1]", "[D2]", "[D3]", "    ", "[D4]", "[D5]", "[D6]", "[][]"],
["[][]", "[E1]", "[E2]", "[E3]", "    ", "[E4]", "[E5]", "[E6]", "[][]"],
["[][]", "[F1]", "[F2]", "[F3]", "    ", "[F4]", "[F5]", "[F6]", "[][]"],
["[][]", "[G1]", "[G2]", "[G3]", "    ", "[G4]", "[G5]", "[G6]", "[][]"],
["[][]", "[H1]", "[H2]", "[H3]", "    ", "[H4]", "[H5]", "[H6]", "[][]"],
["[][]", "[I1]", "[I2]", "[I3]", "    ", "[I4]", "[I5]", "[I6]", "[][]"],
["[][]", "[J1]", "[J2]", "[J3]", "    ", "[J4]", "[J5]", "[J6]", "[][]"],
["[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]"]
]
data_standard_large = [standard_large, 13, 9, 60]
data_penonton_standard_large = [[[f"[{chr(65+i)}{j+1}]","",""] for j in range(6)] for i in range(10)] # Array [0..10] of array [0..6] of array [0..3] of string

premier_large =[
["[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]"],
["[][]", "====", "====", "====", "====", "====", "====", "====", "====", "[][]"],
["[][]", "[A1]", "[A2]", "    ", "[A3]", "[A4]", "    ", "[A5]", "[A6]", "[][]"],
["[][]", "[B1]", "[B2]", "    ", "[B3]", "[B4]", "    ", "[B5]", "[B6]", "[][]"],
["[][]", "[C1]", "[C2]", "    ", "[C3]", "[C4]", "    ", "[C5]", "[C6]", "[][]"],
["[][]", "[D1]", "[D2]", "    ", "[D3]", "[D4]", "    ", "[D5]", "[D6]", "[][]"],
["[][]", "[E1]", "[E2]", "    ", "[E3]", "[E4]", "    ", "[E5]", "[E6]", "[][]"],
["[][]", "[F1]", "[F2]", "    ", "[F3]", "[F4]", "    ", "[F5]", "[F6]", "[][]"],
["[][]", "[G1]", "[G2]", "    ", "[G3]", "[G4]", "    ", "[G5]", "[G6]", "[][]"],
["[][]", "[H1]", "[H2]", "    ", "[H3]", "[H4]", "    ", "[H5]", "[H6]", "[][]"],
["[][]", "[I1]", "[I2]", "    ", "[I3]", "[I4]", "    ", "[I5]", "[I6]", "[][]"],
["[][]", "[J1]", "[J2]", "    ", "[J3]", "[J4]", "    ", "[J5]", "[J6]", "[][]"],
["[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]", "[][]"]
]
data_premier_large = [premier_large, 13, 10, 60]
data_penonton_premier_large = [[[f"[{chr(65+i)}{j+1}]","",""] for j in range(6)]for i in range(10)] # Array [0..10] of array [0..6] of array [0..3] of string

data_film = ["Spongebob SquarePants", "Angry Birds", "One Piece", "Boboboi", "Kungfu Panda 3", "The Avengers"]

play_ke = 0
film_ke = 0
current_film1 = data_film[film_ke*2]
current_film2 = data_film[film_ke*2+1]
current_room = data_standard_large
data_penonton_current_room = data_penonton_standard_large

cursor_position = [2,1]
jumping_space = 0 # Total space-line 
temp_seat = "[A1]"
book = False

alphabet = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)] + [" "]

def print_room():
    global temp_seat
    os.system("cls||clear")
    
    for i in range(current_room[1]-3): # Change seat number with cursor
        for j in range(6):
            if current_room[0][cursor_position[0]][cursor_position[1]] == data_penonton_current_room[i][j][0]:
                if data_penonton_current_room[i][j][1] == "":
                    current_room[0][cursor_position[0]][cursor_position[1]] = "[" + Fore.LIGHTGREEN_EX + "**" + Fore.WHITE + "]"
                else:
                    current_room[0][cursor_position[0]][cursor_position[1]] = "[" + Fore.LIGHTRED_EX + "##" + Fore.WHITE + "]"
                temp_seat = data_penonton_current_room[i][j][0]

    if current_room == data_standard_large or current_room == data_standard_small:
        print(Fore.WHITE + f"=====[{current_film1}]=====".center(current_room[2]*4," "))
    elif current_room == data_premier_large or current_room == data_premier_small:
        print(Fore.WHITE + f"=====[{current_film2}]=====".center(current_room[2]*4," "))
    print()
    for i in range(current_room[1]):
        for j in range(current_room[2]):
            if isOccupied(current_room[0][i][j]):
                print(Fore.LIGHTBLACK_EX + current_room[0][i][j], end="")
            elif i == 0 or i == current_room[1]-1 or j == 0 or j == current_room[2]-1:
                print(Fore.LIGHTCYAN_EX + current_room[0][i][j], end="")
            else:
                print(Fore.WHITE + current_room[0][i][j], end = "")

        if i == 2:
            print(Fore.LIGHTGREEN_EX + "\t[Enter] Pesan/Lihat Detail",end="")
        elif i == 3:
            print(Fore.LIGHTGREEN_EX + "\t[P] Play Film",end="")
        elif i == 4:
            print(Fore.LIGHTGREEN_EX + "\t[F] Find Seat",end="")
        print()
    print()
    print()
    print()

def validate(text, type):
    if type == "nama":
        if text == "" :
            print("[!] Nama pemesan harus diisi")
            time.sleep(1.5)
            return False, text

        if text == " "*len(text):
            print("[!] Nama pemesan tidak boleh spasi saja")
            time.sleep(1.5)
            return False, text
        
        if text[0] == " ":
            print("[!] Nama pemesan tidak boleh diawali spasi")
            time.sleep(1.5)
            return False, text
        
        isAlphabet = True
        for i in range(len(text)):
            if text[i] not in alphabet:
                isAlphabet = False
        if not isAlphabet:
            print("[!] Terdapat sesuatu diluar ketentuan nama")
            time.sleep(1.5)
            return False, text
        else:
            return True, text
        
    elif type == "date":
        def cek_format_date(text):
            cek = text.split("-")
            if len(cek) != 3:
                return False
            else:
                if len(cek[0]) != 2:
                    return False
                if len(cek[1]) != 2:
                    return False
                if len(cek[2]) != 4:
                    return False
                
            return True



        if cek_format_date(text):
            var1,var2,var3 = map(int, text.split("-"))
            valid = True
            if var3 < 1:
                valid = False
            if (var2 > 12 or var2 < 1):
                valid = False
            if var1 > 31 or var1 < 1:
                valid = False
            else:
                if (1 <= var2 <= 7 and var2 % 2 == 0) and var2 != 2:
                    if var1 > 30:
                        valid = False
                elif(7 < var2 <= 12 and var2 % 2 == 1):
                    if var1 > 30:
                        valid = False
                elif (var1 == 29 and var3 % 100 == 0) and var2 == 2:
                    valid = False
                elif (var1 == 29 and var3 % 4 == 0) and var2 == 2:
                    valid = True
                elif (var1 == 29 and var3 % 4 != 0) and var2 == 2:
                    valid = False
            return valid, text
        return False, text

def command(action):
    global jumping_space, current_room, data_penonton_current_room, cursor_position, temp_seat, current_film1, current_film2, play_ke, film_ke, data_penonton_standard_large, data_penonton_premier_large, data_penonton_standard_small, data_penonton_premier_small
    if action == "up":
        current_room[0][cursor_position[0]][cursor_position[1]] = temp_seat  # Write Back seat number

        if cursor_position[0] > 2: # If cursor still in range of the room
            cursor_position[0] -= 1

    elif action == "down":
        current_room[0][cursor_position[0]][cursor_position[1]] = temp_seat  # Write Back seat number

        if cursor_position[0] < current_room[1]-2: # If cursor still in range of the room
            cursor_position[0] += 1

    elif action == "left":
        current_room[0][cursor_position[0]][cursor_position[1]] = temp_seat  # Write Back seat number

        if cursor_position[1] == current_room[2]-1 and current_room[0][cursor_position[0]][cursor_position[1]] == "[>>]": # Cancel change room
            for i in range(1, current_room[1]-1):
                current_room[0][i][cursor_position[1]] = "[][]"

        if cursor_position[1] > 1: # If cursor still in range of the room
            cursor_position[1] -= 1
            if current_room[0][cursor_position[0]][cursor_position[1]] == "    ": # If cursor move through the space line
                jumping_space -= 1
                cursor_position[1] -= 1
        elif cursor_position[1] == 1 and current_room[0][cursor_position[0]][0] == "[][]" and (current_room == data_premier_large or current_room == data_premier_small): # If cursor wanna change room
            current_room[0][cursor_position[0]][cursor_position[1]] = temp_seat
            temp_seat = "[<<]"
            cursor_position[1] -= 1

            for i in range(1, current_room[1]-1):
                current_room[0][i][0] = "[<<]"

        elif cursor_position[1] == 0 and current_room[0][cursor_position[0]][0] == "[<<]": # If cursor actually changing room
            for i in range(1, current_room[1]-1):
                current_room[0][i][0] = "[][]"


            if play_ke % 2 == 0:
                if current_room == data_premier_large:
                    current_room = data_standard_large
                    data_penonton_current_room = data_penonton_standard_large
            else:
                if current_room == data_premier_small:
                    current_room = data_standard_small
                    data_penonton_current_room = data_penonton_standard_small

            jumping_space = 0 # Reset total space-line
            cursor_position[1] = current_room[2]-2  # Reset cursor position

    elif action == "right":
        current_room[0][cursor_position[0]][cursor_position[1]] = temp_seat  # Write Back seat number
        
        if cursor_position[1] == 0 and current_room[0][cursor_position[0]][0] == "[<<]": # Cancel change room
            for i in range(1, current_room[1]-1):
                current_room[0][i][0] = "[][]"

        if cursor_position[1] < current_room[2]-2: # If cursor still in range of the room
            cursor_position[1] += 1
            if current_room[0][cursor_position[0]][cursor_position[1]] == "    ": # If cursor move through the space line
                cursor_position[1] += 1
                jumping_space = 1

        elif cursor_position[1] == current_room[2]-2 and current_room[0][cursor_position[0]][cursor_position[1]+1] == "[][]" and (current_room == data_standard_large or current_room == data_standard_small): # If cursor wanna change room
            current_room[0][cursor_position[0]][cursor_position[1]] = temp_seat
            temp_seat = "[>>]"
            cursor_position[1] += 1
            for i in range(1, current_room[1]-1):
                current_room[0][i][cursor_position[1]] = "[>>]"

        elif cursor_position[1] == current_room[2]-1 and current_room[0][cursor_position[0]][cursor_position[1]] == "[>>]": # If cursor actually changing room
            for i in range(1, current_room[1]-1):
                current_room[0][i][cursor_position[1]] = "[][]"


            if play_ke % 2 == 0:
                if current_room == data_standard_large:
                    current_room = data_premier_large
                    data_penonton_current_room = data_penonton_premier_large
            else:
                if current_room == data_standard_small:
                    current_room = data_premier_small
                    data_penonton_current_room = data_penonton_premier_small

            jumping_space = 0 # Reset total space-line
            cursor_position[1] = 1 # Reset cursor position   

    elif action == "find":

        def find_seat(kelas, seat):
            global data_penonton_current_room, current_room, cursor_position, jumping_space, book
            if play_ke % 2 == 0:
                if kelas == "standard":
                    for i in range(10):
                        for j in range(6):
                            if data_penonton_standard_large[i][j][0] == f"[{seat}]":
                                current_room[0][cursor_position[0]][cursor_position[1]] = temp_seat
                                current_room = data_standard_large
                                data_penonton_current_room = data_penonton_standard_large
                                jumping_space = 0
                                x = i + 2 ; y = j + 1
                                if y > 3:
                                    jumping_space += 1
                                    y += 1
                                cursor_position = [x,y]
                                print(f"[~] Berhasil pindah ke seat [{seat}]")
                                book = True
                                time.sleep(2)
                                return
                else:
                    for i in range(10):
                        for j in range(6):
                            if data_penonton_premier_large[i][j][0] == f"[{seat}]":
                                current_room[0][cursor_position[0]][cursor_position[1]] = temp_seat
                                current_room = data_premier_large
                                data_penonton_current_room = data_penonton_premier_large
                                jumping_space = 0
                                x = i + 2 ; y = j + 1
                                if y > 2:
                                    jumping_space += 1
                                    y += 1
                                if y > 5:
                                    jumping_space += 1
                                    y += 1
                                cursor_position = [x,y]
                                print(f"[~] Berhasil pindah ke seat [{seat}]")
                                book = True
                                time.sleep(2)
                                return
            else:
                if kelas == "standard":
                    for i in range(5):
                        for j in range(6):
                            if data_penonton_standard_small[i][j][0] == f"[{seat}]":
                                current_room[0][cursor_position[0]][cursor_position[1]] = temp_seat
                                current_room = data_standard_small
                                data_penonton_current_room = data_penonton_standard_small
                                jumping_space = 0
                                x = i + 2 ; y = j + 1
                                if y > 3:
                                    jumping_space += 1
                                    y += 1
                                cursor_position = [x,y]
                                print(f"[~] Berhasil pindah ke seat [{seat}]")
                                book = True
                                time.sleep(2)
                                return
                else:
                    for i in range(5):
                        for j in range(6):
                            if data_penonton_premier_small[i][j][0] == f"[{seat}]":
                                current_room[0][cursor_position[0]][cursor_position[1]] = temp_seat
                                current_room = data_premier_small
                                data_penonton_current_room = data_penonton_premier_small
                                jumping_space = 0
                                x = i + 2 ; y = j + 1
                                if y > 2:
                                    jumping_space += 1
                                    y += 1
                                if y > 4:
                                    jumping_space += 1
                                    y += 1
                                cursor_position = [x,y]
                                print(f"[~] Berhasil pindah ke seat [{seat}]")
                                book = True
                                time.sleep(2)
                                return
            print("[!] Seat tidak ditemukan")
            time.sleep(2)


        print(Fore.WHITE)
        print("--=== Cari Seat ===--\n[1] Teater Standard\n[2] Teater Premiere")
        pilih = input("Masukkan teater yang diinginkan : ")
        if pilih == "1":
            seat = input("Masukkan Seat yang dicari : ")
            find_seat("standard",seat)

        elif pilih == "2":
            seat = input("Masukkan Seat yang dicari : ")
            find_seat("premier",seat)

        else:
            print("[!] Teater tidak ditemukan")
            time.sleep(2)

    elif action == "play":
        
        for i in range(1,current_room[2]-1):
            current_room[0][1][i] = "░░░░"

        current_film1 = "NOW PLAYING!!!"
        current_film2 = "NOW PLAYING!!!"

        for i in range(1,current_room[2]-1):
            for j in range(4):
                current_room[0][1][i] = "▒"*(j+1) + "░"*(3-j)
                print_room()
                time.sleep(0.05)

        if film_ke == 2:
            film_ke = 0
        else:
            film_ke += 1
        current_film1 = data_film[film_ke*2]
        current_film2 = data_film[film_ke*2+1]

        for i in range(1,current_room[2]-1):
            current_room[0][1][i] = "===="

        current_room[0][cursor_position[0]][cursor_position[1]] = temp_seat
        temp_seat = "[A1]"
        cursor_position = [2,1]
        jumping_space = 0

        if play_ke % 2 == 0:
            data_penonton_standard_large = [[[f"[{chr(65+i)}{j+1}]","",""] for j in range(6)] for i in range(10)]
            data_penonton_premier_large = [[[f"[{chr(65+i)}{j+1}]","",""] for j in range(6)] for i in range(10)]
            if current_room == data_penonton_standard_large:
                current_room = data_standard_small
                data_penonton_current_room = data_penonton_standard_small
            else:
                current_room = data_premier_small
                data_penonton_current_room = data_penonton_premier_small
        else:
            data_penonton_standard_small = [[[f"[{chr(65+i)}{j+1}]","",""] for j in range(6)] for i in range(5)]
            data_penonton_premier_small = [[[f"[{chr(65+i)}{j+1}]","",""] for j in range(6)] for i in range(5)]
            if current_room == data_penonton_standard_small:
                current_room = data_standard_large
                data_penonton_current_room = data_penonton_standard_large
            else:
                current_room = data_premier_large
                data_penonton_current_room = data_penonton_premier_large
        play_ke += 1

    elif action == "book":
        if play_ke % 2 == 0:
            for i in range(10):
                for j in range(6):
                    if data_penonton_current_room[i][j][0] == temp_seat:
                        if data_penonton_current_room[i][j][1] != "" and data_penonton_current_room[i][j][2] != "":
                            print_room()
                            print("--=== Data Pemesan ===--".center(current_room[2]*4, " "))
                            print(f"Nama Pemesan  : {data_penonton_current_room[i][j][1]}")
                            print(f"Tanggal Pesan : {data_penonton_current_room[i][j][2]}")
                            input()

                        if data_penonton_current_room[i][j][1] == "":
                            valid = False
                            while not valid:
                                print_room()
                                print("--=== Input Data Pemesan ===--")
                                nama = input("Masukkan nama pemesan : ")
                                valid = validate(nama, "nama")[0]
                                if valid:
                                    data_penonton_current_room[i][j][1] = validate(nama, "nama")[1]
                        if data_penonton_current_room[i][j][2] == "":
                            valid = False
                            while not valid:
                                print_room()
                                print("--=== Input Data Pemesan ===--")
                                print(f"Masukkan nama pemesan : {data_penonton_current_room[i][j][1]}")
                                tanggal = input("Masukkan tanggal pemesanan : ")
                                valid = validate(tanggal, "date")[0]
                                if valid:
                                    data_penonton_current_room[i][j][2] = validate(tanggal, "date")[1]
                                    print("\n[+] Pemesanan Berhasil !")
                                    input()

                                    if current_room[0][cursor_position[0]][cursor_position[1]] == "[" + Fore.LIGHTGREEN_EX + "**" + Fore.WHITE + "]":
                                        current_room[0][cursor_position[0]][cursor_position[1]] = "[" + Fore.LIGHTRED_EX + "##" + Fore.WHITE + "]"

                                else:
                                    print("[!] Tanggal tidak valid")
                                    time.sleep(1.5)
                                
        else:
            for i in range(5):
                for j in range(6):
                    if data_penonton_current_room[i][j][0] == temp_seat:
                        if data_penonton_current_room[i][j][1] != "" and data_penonton_current_room[i][j][2] != "":
                            print_room()
                            print("--=== Data Pemesan ===--".center(current_room[2]*4, " "))
                            print(f"Nama Pemesan  : {data_penonton_current_room[i][j][1]}")
                            print(f"Tanggal Pesan : {data_penonton_current_room[i][j][2]}")
                            input()

                        if data_penonton_current_room[i][j][1] == "":
                            valid = False
                            while not valid:
                                print_room()
                                print("--=== Input Data Pemesan ===--")
                                nama = input("Masukkan nama pemesan : ")
                                valid = validate(nama, "nama")[0]
                                if valid:
                                    data_penonton_current_room[i][j][1] = validate(nama, "nama")[1]
                        if data_penonton_current_room[i][j][2] == "":
                            valid = False
                            while not valid:
                                print_room()
                                print("--=== Input Data Pemesan ===--")
                                print(f"Masukkan nama pemesan : {data_penonton_current_room[i][j][1]}")
                                tanggal = input("Masukkan tanggal pemesanan : ")
                                valid = validate(tanggal, "date")[0]
                                if valid:
                                    data_penonton_current_room[i][j][2] = validate(tanggal, "date")[1]
                                    print("\n[+] Pemesanan Berhasil !")
                                    input()
                                    if current_room[0][cursor_position[0]][cursor_position[1]] == "[" + Fore.LIGHTGREEN_EX + "**" + Fore.WHITE + "]":
                                        current_room[0][cursor_position[0]][cursor_position[1]] = "[" + Fore.LIGHTRED_EX + "##" + Fore.WHITE + "]"
                                else:
                                    print("[!] Tanggal tidak valid")
                                    time.sleep(1.5)
                                    



def isOccupied(seat):
    for i in range(current_room[1]-3):
        for j in range(6):
            if seat == data_penonton_current_room[i][j][0] and data_penonton_current_room[i][j][1] != "":
                return True
    return False

def random_seat(size):
    from random import randint
    if size == "large":
        for i in range(30):
            valid = False
            while not valid:
                x = randint(0,9)
                y = randint(0,5)
                if data_penonton_premier_large[x][y][1] == "":
                    valid = True
                    data_penonton_premier_large[x][y][1] = "(Unknown Customer)"
                    data_penonton_premier_large[x][y][2] = "-"

            valid = False
            while not valid:
                x = randint(0,9)
                y = randint(0,5)
                if data_penonton_standard_large[x][y][1] == "":
                    valid = True
                    data_penonton_standard_large[x][y][1] = "(Unknown Customer)"
                    data_penonton_standard_large[x][y][2] = "-"
    else:
        for i in range(15):
            valid = False
            while not valid:
                x = randint(0,4)
                y = randint(0,5)
                if data_penonton_standard_small[x][y][1] == "":
                    valid = True
                    data_penonton_standard_small[x][y][1] = "(Unknown Customer)"
                    data_penonton_standard_small[x][y][2] = "-"

            valid = False
            while not valid:
                x = randint(0,4)
                y = randint(0,5)
                if data_penonton_premier_small[x][y][1] == "":
                    valid = True
                    data_penonton_premier_small[x][y][1] = "(Unknown Customer)"
                    data_penonton_premier_small[x][y][2] = "-"

def main():
    global book
            
    # Random isi setengah seat
    if play_ke % 2 == 0:
        random_seat("large")
    else:
        random_seat("small")
    play = False
    while not play:
        
        print_room()

        if not book:
            ch = msvcrt.getch()
            while ch not in [b'w',b'a',b's',b'd',b'f',b'p',b'\r']:
                ch = msvcrt.getch()
            if ch in b'\x00':
                ch = msvcrt.getch()
            if ch == b'w':
                command("up")
            elif ch == b'a':
                command("left")
            elif ch == b's':
                command("down")
            elif ch == b'd':
                command("right")
            elif current_room[0][1][0] != "[<<]" and current_room[0][1][current_room[2]-1] != "[>>]":
                if ch == b'f':
                    command("find")
                elif ch == b'p':
                    command("play")
                    play = True
                elif ch == b'\r':
                    command("book")
            else:
                pass
        else:
            book = False
            command("book")
    main()
main()
