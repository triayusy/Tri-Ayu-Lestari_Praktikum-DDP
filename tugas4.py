#1
a = ["B 2345 ZX", "Beat", "60", "Hitam"]
print (a)


#2
a.append ("3.000.000")
print (a)
a.append ("2")
print (a)

a.insert (3, "Honda")
print (a)
a.insert (4, "Sepeda Motor")
print (a)

#3
ket = '''selamat datang di aplikasi menghitung
masukan pilihan:
1. untuk menghitung luas persegi
2. untuk menghitung luas lingkaran
3. untuk menghitung luas segitiga
'''

pilihan = input (ket)

match pilihan:
    case "1":
        print ("kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input ("masukan sisi ?"))
        luasP = sisi * sisi
        print ("luas persegi yang sisinya ", sisi, "adalah " ,luasP)
    case "2":
        print ("kamu memilih 2 untuk menghitung luas lingkaran")
        jari2 = float(input ("masukan jari2 ?"))
        luasL = 3.14 * jari2 * jari2
        print ("luas lingkaran yang jari2nya ", jari2, "adalah ",int(luasL))
    case "3":
        print ("kamu memilih 2 untuk menghitung luas segitiga")
        alas = int(input ("masukan alas ?"))
        tinggi = int(input ("masukan tinggi ?"))
        luasS = 0,5 * alas * tinggi
        print ("luas segitiga yang alasnya ", alas, "dan tingginya ", tinggi, "adalah", int(luasS))
    case _:
        print("salah memilih pilihan")