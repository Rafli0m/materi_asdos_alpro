# ==============================================================================
# PERTEMUAN 3: APLIKASI KALKULATOR SEDERHANA (STUDI KASUS PERCABANGAN)
# ==============================================================================
# Program kalkulator ini memanfaatkan struktur kontrol if-elif-else untuk 
# mengeksekusi operasi matematika berdasarkan nomor menu yang dipilih pengguna.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. MENAMPILKAN MENU PILIHAN KEPADA PENGGUNA
# ------------------------------------------------------------------------------
print("="*12, "KALKULATOR SEDERHANA", "="*12)
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian   (*)")
print("4. Pembagian   (/)")
print("="*46)

# Meminta input menu dalam bentuk string agar aman dibandingkan dengan "1", "2", dst.
menu = input("Silahkan pilih operasi perhitungan (1-4): ")

# ------------------------------------------------------------------------------
# 2. LOGIKA PERCABANGAN BERDASARKAN MENU YANG DIPILIH
# ------------------------------------------------------------------------------
if menu == "1":
    print("\n--- Operasi Penjumlahan ---")
    angka1 = float(input("Masukkan angka pertama : "))
    angka2 = float(input("Masukkan angka kedua   : "))
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")

elif menu == "2":
    print("\n--- Operasi Pengurangan ---")
    angka1 = float(input("Masukkan angka pertama : "))
    angka2 = float(input("Masukkan angka kedua   : "))
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil}")

elif menu == "3":
    print("\n--- Operasi Perkalian ---")
    angka1 = float(input("Masukkan angka pertama : "))
    angka2 = float(input("Masukkan angka kedua   : "))
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil}")

elif menu == "4":
    print("\n--- Operasi Pembagian ---")
    angka1 = float(input("Masukkan angka pertama : "))
    angka2 = float(input("Masukkan angka kedua   : "))
    
    # BEST PRACTICE EDUKASI: Validasi pembagian dengan angka nol
    # Dalam matematika dan komputer, suatu bilangan TIDAK BISA dibagi nol (ZeroDivisionError)
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil}")
    else:
        print("Error: Angka pembagi kedua tidak boleh nol (0)!")

else:
    # Blok else dieksekusi jika pengguna memasukkan selain "1", "2", "3", "4"
    print("\n[Peringatan] Menu yang Anda inputkan tidak valid! Harap pilih angka 1 sampai 4.")

print("="*46)