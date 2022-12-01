#Tempat menonton
print("Halo Selamat datang di bioskop!")
print("Dimanakah kamu ingin menonton?")
print("1. XXI Empire")
print("2. XXI Amplaz")
print("3. XXI JCM")
input("Masukkan pilihanmu: ")

#Judul Film
print("Mau nonton film apa? Ada film:")
print("1. Frozen")
print("2. Keramat")
print("3. KKN di Desa Penari")
input("Pilih nomor film: ")

#Tipe layar
print("Mau nonton layar bioskop apa?")
print("1. Reguler")
print("2. Dolby almos")
print("3. Premiere")
input("pilih nomor tipe layar: ")
input("Berapa banyak tiket? ")
#Jam penayangan
print("Mau nonton jam berapa:")
print("1. 12.35")
print("2. 14.45")
print("3. 16.55")
print("4. 19.05")
pilihan =int(input("Masukkan pilihan anda: "))
print("pilihan :", type(pilihan))
if pilihan== 1:
    print(input("Oke berhasil!, Silahkan dinikmati di jam 12.35"))
elif pilihan==2:
     print(input("Oke berhasil!, Silahkan dinikmati di jam 14.45"))
elif pilihan==3:
     print(input("Oke berhasil!, Silahkan dinikmati di jam 16.55"))  
elif pilihan==4:
     print(input("Oke berhasil!, Silahkan dinikmati di jam 19.05"))  

#Test case 2
print("Halo Selamat datang di bioskop!")
print("Dimanakah kamu ingin menonton?")
print("1. XXI Empire")
print("2. XXI Amplaz")
print("3. XXI JCM")
pilihan =int(input("Masukkan pilihan anda: "))
print("pilihan :", type(pilihan))
if pilihan== 1:
    print(input("XXI Empire"))
elif pilihan==2:
     print(input("XXI Amplaz"))
elif pilihan==3:
     print(input("XXI JCM"))  
elif pilihan==4:
     print(input("Pilihan tidak tersedia"))  

#Test Case 3
print("Halo Selamat datang di bioskop!")
print("Dimanakah kamu ingin menonton?")
print("1. XXI Empire")
print("2. XXI Amplaz")
print("3. XXI JCM")
input("Masukkan pilihanmu: ")

print("Mau nonton film apa? Ada film:")
print("1. Frozen")
print("2. Keramat")
print("3. KKN di Desa Penari")
input("Pilih nomor film: ")
pilihan =int(input("Masukkan pilihan anda: "))
print("pilihan :", type(pilihan))
if pilihan== 1:
    print(input("Frozen"))
elif pilihan==2:
     print(input("Keramat"))
elif pilihan==3:
     print(input("KKN di Desa Penari"))  
elif pilihan==4:
     print(input("Pilihan tidak tersedia"))  
