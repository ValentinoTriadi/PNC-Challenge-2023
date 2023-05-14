from random import randint
import os,time
id = 100
is_registered = False
username = ""
password = ""
nama = ""
is_login = False
is_batery_initialized = False
batery_capacity = 0
batery_level = 0
batery_use = 0

def print_function(tanggal, bulan, tahun):
    os.system("cls||clear")
    # Tanggal
    print("Tanggal\t\t: %02d-%02d-%04d" % (tanggal, bulan, tahun))
    
    # Login
    if is_login:
        print("ID\t\t: {0}_{1}".format(nama,id))
        print("Nama\t\t: {0}".format(nama))

    # Battery
    if is_batery_initialized:
        print(f"Battery Level\t: {batery_level}")
        print(f"Max Bar\t\t: {batery_capacity}")
        print(f"Used Time\t: {batery_use}")

    # Menu
    print('''
[1] Register
[2] Login
[3] Inisialisasi Kapasitas Baterai
[4] Aktifkan Mesin
[5] Isi Daya
[6] Tampil Indikator Baterai
[7] Reset Data
[0] Keluar dari program''')

def validate(type,var1,var2,var3):
    if type == "date":
        valid = True
        if var3 < 1:
            print("Tahun Tidak Valid")
            valid = False
        if (var2 > 12 or var2 < 1):
            print("Bulan Tidak Valid")
            valid = False
        if var1 > 31 or var1 < 1:
            print("Tanggal Tidak Valid")
            valid = False
        else:
            if (1 <= var2 <= 7 and var2 % 2 == 0) and var2 != 2:
                if var1 > 30:
                    print("Tanggal Tidak Valid")
                    valid = False
            elif(7 < var2 <= 12 and var2 % 2 == 1):
                if var1 > 30:
                    print("Tanggal Tidak Valid")
                    valid = False
            elif (var1 == 29 and var3 % 4 == 0 and var3 % 100 != 0) and var2 == 2:
                print("Tanggal Tidak Valid")
                valid = False
            elif var1 > 29 and var2 == 2:
                print("Tanggal Tidak Valid")
                valid = False
        return valid
    
    if type == "menu":
        if var1 not in range(8):
            print("[!] Menu ini tidak ada [!]")
            time.sleep(1)
            return False
        return True
    
    if type == "user":
        if var1 == "" or var1 == "-":
            print("[!] Username Tidak Boleh Kosong [!]")
            time.sleep(1)
            return False
        return True

    if type == "pass":
        if var2 == "" or var2 == "-":
            print("[!] Password Tidak Boleh Kosong [!]")
            time.sleep(1)
            return False
        if var2 == var1:
            print("[!] Password dan Username Tidak Boleh Sama [!]")
            time.sleep(1)
            return False
        return True
    
    if type == "login":
        if var1 != username or var2 != password:
            print("[!] Username atau Password Salah [!]")
            time.sleep(1)
            return False
        return True
    
    if type == "kapasitas":
        if var1 < 1:
            print("[!] Minimal Terdapat 1 Bar [!]")
            time.sleep(1)
            return False
        elif var1 >30:
            print("[!] Maximal Terdapat 30 Bar [!]")
            time.sleep(1)
            return False
        return True
    
    if type == "use":
        if var1 > var2:
            print("[!] Battery Kurang [!]")
            time.sleep(1)
            return False
        elif var1 <= 0:
            print("[!] Waktu Penggunaan Tidak Boleh Nol/Negatif [!]")
            time.sleep(1)
            return False
        return True

    if type == "after_use":
        if var1 >= 24:
            var2[0] += 1
            if validate("date",var2[0],var2[1],var2[2]):
                return var1-24, var2
            else:
                if (1 <= var2[1] <= 7 and var2[1] % 2 == 0) and var2[1] != 2:
                    if var2[0] > 30:
                        var2[0] -= 30
                        var2[1] += 1
                        return var1-24, var2
                elif (7 < var2[1] <= 12 and var2[1] % 2 == 1):
                    if var2[0] > 30:
                        var2[0] -= 30
                        var2[1] += 1
                        return var1-24, var2
                elif (1 <= var2[1] <= 7 and var2[1] % 2 != 0):
                    if var2[0] > 31:
                        var2[0] -= 31
                        var2[1] += 1
                        return var1-24, var2
                elif (7 < var2[1] < 12 and var2[1] % 2 != 1):
                    if var2[0] > 31:
                        var2[0] -= 31
                        var2[1] += 1
                        return var1-24, var2
                elif (var2[0] == 29 and var2[2] % 4 == 0 and var2[2] % 100 != 0) and var2[1] == 2:
                    var2[0] -= 28
                    var2[1] += 1
                    return var1-24, var2
                elif var2[0] > 29 and var2[1] == 2:
                    var2[0] -= 29
                    var2[1] += 1
                    return var1-24, var2
                elif var2[0] > 31 and var2[1] == 12:
                    var2[0] -= 31
                    var2[1] = 1
                    var2[2] += 1
                    return var1-24, var2
        return var1, var2
        
    if type == "jumlah_isi":
        if var1 < 0:
            print("[!] Jumlah Daya Tidak Boleh Negatif [!]")
            time.sleep(1)
            return False
        elif var1 + var3 > var2:
            print("[!] Jumlah Daya Melebihi Kapasitas [!]")
            time.sleep(1)
            return False
        return True

def starting_point():
    global start
    os.system("cls||clear")
    print("Selamat Datang")
    try:
        tanggal, bulan, tahun = map(int, input("Silakan Masukan Tanggal : ").split("-"))
    except ValueError:
        print("[!] Format Tidak Sesuai [!]\n[!] Format : dd-mm-yyyy [!]")
        time.sleep(1)
        return starting_point()
    valid = validate("date",tanggal,bulan,tahun)

    if not valid :
        time.sleep(1)
        return starting_point()
    else:
        start = True
        date = [tanggal, bulan, tahun]
        return date

def input_menu():
    valid = False
    while not valid:
        print_function(date[0], date[1], date[2])
        pilih = 0
        try:
            pilih = int(input("Input Menu : "))
        except ValueError:
            print("[!] Input Tidak Valid [!]")
            time.sleep(1)
            return input_menu()
        valid = validate("menu",pilih,0,0)
    return pilih


def register(date):
    global username, password, nama, id, is_registered
    if not is_registered:
        valid = False
        while not valid:
            print_function(date[0], date[1], date[2])
            print("Input Menu : 1\n")
            user = input("Username\t: ")
            valid = validate("user",user,0,0)
        username = user

        valid = False
        while not valid:
            print_function(date[0], date[1], date[2])
            print("Input Menu : 1\n")
            print("Username\t: {0}".format(user))
            passs = input("Password\t: ")
            valid = validate("pass",user,passs,0)
        password = passs

        nama = input("Nama\t\t: ")
        print("ID\t\t: {0}_{1}\n".format(nama,id))
        print("[*] Berhasil Register [*]")
        time.sleep(2)
        is_registered = True 
    else:
        print_function(date[0], date[1], date[2])
        print("Input Menu : 1\n")
        print("[!] Sudah Registrasi [!]")
        time.sleep(1)

    main(date)

def login(date):
    global is_login
    if not is_registered:
        print("\n[!] Belum Register [!]")
        time.sleep(1)
    elif is_login:
        print("\n[!] Sudah Login [!]")
        time.sleep(1)
    elif not is_login:
        valid = False
        while not valid:
            print_function(date[0], date[1], date[2])
            print("Input Menu : 2\n")
            user = input("Username\t: ")
            passs = input("Password\t: ")
            valid = validate("login",user,passs,0)
        is_login = True
    main(date)

def baterai(date,command):
    global batery_capacity, batery_level, batery_use, is_batery_initialized
    if command == "kapasitas":
        if not is_registered:
            print("\n[!] Belum Register [!]")
            time.sleep(1)
        elif not is_login:
            print("\n[!] Belum Login [!]")
            time.sleep(1)
        elif is_batery_initialized:
            print("\n[!] Sudah Terinisialisasi [!]")
            time.sleep(1)
        else:
            valid = False
            while not valid:
                print_function(date[0], date[1], date[2])
                print("Input Menu : 3\n")
                kapasitas = int(input("Input Kapasitas Baterai : "))
                valid = validate("kapasitas", kapasitas,0,0)
            batery_capacity = kapasitas
            batery_level = randint(1,batery_capacity)
            is_batery_initialized = True
            print("\n[*] Level Baterai : {0}".format(batery_level))
            print("[*] Inisialisasi Kapasitas Berhasil [*]")
            time.sleep(2)

    elif command == "isi":
        if not is_registered:
            print("\n[!] Belum Register [!]")
            time.sleep(1)
        elif not is_login:
            print("\n[!] Belum Login [!]")
            time.sleep(1)
        elif not is_batery_initialized:
            print("\n[!] Silakan Inisialisasi Kapasitas Baterai Terlebih Dahulu [!]")
            time.sleep(1)
        else:
            valid = False
            while not valid:
                print_function(date[0], date[1], date[2])
                print("Input Menu : 5\n")
                jumlah_isi = int(input("Input Jumlah Daya yang Ingin Diisi : "))
                valid = validate("jumlah_isi",jumlah_isi,batery_capacity,batery_level)
            batery_level += jumlah_isi
            print("\n[*] Berhasil Tambah Daya [*]")
            time.sleep(2)

    elif command == "tampil":
        if not is_registered:
            print("\n[!] Belum Register [!]")
            time.sleep(1)
        elif not is_login:
            print("\n[!] Belum Login [!]")
            time.sleep(1)
        elif not is_batery_initialized:
            print("\n[!] Silakan Inisialisasi Kapasitas Baterai Terlebih Dahulu [!]")
            time.sleep(1)
        else:
            from colorama import Fore
            print_function(date[0], date[1], date[2])
            print("Input Menu : 6\n")
            persen = int(round((batery_level/batery_capacity)*100))
            print("Kapasitas Baterai yang tersisa: {0}%\n".format(persen))
            if persen <= 20:
                color = Fore.RED
            elif persen <= 60:
                color = Fore.YELLOW
            elif persen > 60:
                color = Fore.GREEN
                
            print_ascii = ""
            print_ascii += "#"*(batery_capacity*5 + 4) + "\n"
            print_ascii += "#   " + color + "**** "*(batery_level) + "     "*(batery_capacity-batery_level) + Fore.WHITE + "##\n"
            print_ascii += "#  " + color + "**** "*(batery_level) + "     "*(batery_capacity-batery_level) + Fore.WHITE + " ##\n"
            print_ascii += "# " + color + "**** "*(batery_level) + "     "*(batery_capacity-batery_level) + Fore.WHITE + "  ##\n"
            print_ascii += "#"*(batery_capacity*5 + 4) + "\n"
            print(print_ascii)
            input()
    main(date)

def mesin(date):
    global batery_use, batery_level
    if not is_registered:
        print("\n[!] Belum Register [!]")
        time.sleep(1)
    elif not is_login:
        print("\n[!] Belum Login [!]")
        time.sleep(1)
    elif not is_batery_initialized:
        print("\n[!] Silakan Inisialisasi Kapasitas Baterai Terlebih Dahulu [!]")
        time.sleep(1)
    else:
        valid = False
        while not valid:
            print_function(date[0], date[1], date[2])
            print("Input Menu : 4\n")
            use = int(input("Input Banyak Waktu Penggunaan Mesin : "))
            valid = validate("use", use, batery_level, 0)
        batery_use += use
        batery_level -= use
        batery_use, date = validate("after_use",batery_use,date,0)
        print("\n[*] Berhasil Mengaktifkan Mesin Dengan Mengkonsumsi {0} Daya [*]".format(use))
        time.sleep(1)
    main(date)

def reset(date):
    global username, password, nama, id, batery_capacity, batery_level, batery_use, is_batery_initialized, is_registered, is_login
    if not is_registered:
        print("\n[!] Anda Belum Register [!]")
        time.sleep(1)
    elif not is_login:
        print("\n[!] Anda Belum Login [!]")
        time.sleep(1)
    else:
        id += 1
        is_registered = False
        username = ""
        password = ""
        nama = ""
        is_login = False
        is_batery_initialized = False
        batery_capacity = 0
        batery_level = 0
        batery_use = 0
        print("\n[*] Berhasil Logout [*]")
    main(date)

def main(date):
    print_function(date[0], date[1], date[2])
    pilih = input_menu()
    if pilih == 1:
        register(date)
    elif pilih == 2:
        login(date)
    elif pilih == 3:
        baterai(date,"kapasitas")
    elif pilih == 4:
        mesin(date)
    elif pilih == 5:
        baterai(date,"isi")
    elif pilih == 6:
        baterai(date,"tampil")
    elif pilih == 7:
        reset(date)
    elif pilih == 0:
        exit()

date = starting_point()
main(date)