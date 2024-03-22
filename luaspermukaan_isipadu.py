#Atur cara mengira jumlah luas permukaan dan isipadu tangki air berbentuk silinder
#Isytihar pemalar
pi=3.142

#Input
jejari=float(input("Masukkan jejari:"))
tinggi=float(input("Masukkan tinggi:"))

#Proses
jumlahluaspermukaan=(2*pi*jejari*tinggi)+(2*pi*jejari*jejari)
isipadu=pi*jejari*jejari*tinggi

#Output
print("Jumlah luas permukaan silinder ialah",round(jumlahluaspermukaan,2))
print("Isipadu silinder ialah",round(isipadu,2))
