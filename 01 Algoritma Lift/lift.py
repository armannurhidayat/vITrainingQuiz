print("| ================== Algoritma Lift ================== |")
orang = int(input("Jumlah orang yang masuk kedalam lift : "))
index = 1
dataList = []

while index < int(orang+1):
    dataList.append(int(input("Tujuan lantai orang ke-{}".format(index) + ": ")))
    index = index+1

posisiLantai = int(input("\nPosisi lantai sekarang : "))
print("\n{} Orang berada di dalam lift".format(orang))
print("Lift bergerak...")
print("| ==================================================== |\n")

dataList.sort()
result = filter(lambda x: x > posisiLantai, dataList) 
print("Lift bergerak naik ke lantai : {}".format(result))

dataList.reverse()
result = filter(lambda x: x < posisiLantai, dataList) 
print("Lift bergerak turun ke lantai : {}".format(result))