print("Kalkulator simpel")
total=None
angka1=int(input("Masukkan angka pertama:"))
operasi=input("Masukkan operator:")
angka2=int(input("Masukkan angka kedua:"))
if(operasi=="+"):
    total=angka1+angka2
elif(operasi=="-"):
    total=angka1-angka2
elif(operasi=="*"):
    total=angka1*angka2
elif(operasi=="/"):
    total=angka1/angka2
else:
    print("Maaf operator tidak tersedia untuk sementara atau karakter yang diketik bukan operator.")

if(total!=None):
    print(total)
else:
    print("Jalankan program lagi")