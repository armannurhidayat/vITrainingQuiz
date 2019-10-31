def pascal(jumlahBaris):
    baris = [[1]]
    for _x in range(jumlahBaris - 1):
        diZip = zip([0] + baris[-1], baris[-1] + [0])
        addList = map(sum, diZip)
        baris.append(list(addList))
    return baris

def main(jumlahBaris):
    for row in pascal(jumlahBaris):
        print("{}".format(row))


if __name__ == "__main__":
    jumlahBaris = int(input("Masukan jumlah baris : "))
    main(jumlahBaris)