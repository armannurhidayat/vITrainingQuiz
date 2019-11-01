baris = int(input("Masukan jumlah baris : "))
kolom = int(input("Masukan jumlah kolom : "))
mat = []

print("\n")

for i in range (0, baris):
    mat.append([])
for i in range (0, baris):
    for j in range(0, kolom):
        mat[i].append(j)
        mat[i][j] = 0
for i in range (0, baris):
    for j in range (0, kolom):
        mat[i][j] = int(input("Masukan angka baris ke-{} Kolom ke-{} : ".format(i+1, j+1)))

print(mat)

def Rearrange(mat):
    neg_count = list(filter(lambda x: x < 0, [mat[j][i]] ))
    pos_count = list(filter(lambda x: x >= 0, [mat[j][i]] ))
    print("Positive : ", pos_count)
    print("Negative : ", neg_count)


if __name__ == "__main__":
    Rearrange(mat)