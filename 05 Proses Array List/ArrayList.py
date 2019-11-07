listku = []
string = "~~"

def main():
    baris = int(input("Masukan angka baris : "))
    kolom = int(input("Masukan angka kolom : "))
    
    for i in range(0, baris):
        for j in range(0, kolom):
            angka = int(input(f"masukan angka baris ke-{i+1} kolom ke-{j+1} : "))
            listku.append(str(angka) + string)


    string_list = [str(x) for x in listku]
    strjoin = ""
    print(strjoin.join(string_list))
    

if __name__ == "__main__":
    main()