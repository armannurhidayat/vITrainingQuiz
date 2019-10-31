angka = int(input("Masukkan angka: "))

if angka > 1:
    for i in range(2, angka):
        if (angka % i) == 0:
            print(str(angka) + " bukan prima")
            break
    else:
        print(str(angka) + " adalah prima")
else:
    print(str(angka) + " bukan prima")