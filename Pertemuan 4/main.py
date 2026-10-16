# ==============================================================================
# PERTEMUAN 4: PERULANGAN MENGGUNAKAN WHILE (WHILE LOOP)
# ==============================================================================
# Perulangan (looping) digunakan untuk mengeksekusi sekumpulan instruksi 
# secara berulang-ulang selama kondisi yang ditentukan bernilai True.
#
# 3 BAGIAN PENTING DALAM WHILE LOOP:
# 1. INISIALISASI : Menentukan nilai awal variabel penghitung (counter).
# 2. KONDISI      : Syarat kapan perulangan harus terus berjalan.
# 3. INCREMENT    : Perubahan nilai counter agar perulangan pada akhirnya berhenti.
#                   (AWAS: Jika lupa membuat increment, program akan terjebak 
#                    dalam 'Infinite Loop' / perulangan tak hingga yang membuat crash!)
# ==============================================================================

print("=== MENCETAK POLA SEGITIGA BINTANG DENGAN WHILE LOOP ===")

# 1. Inisialisasi: Nilai awal counter
angka = 0

# 2. Kondisi: Loop akan terus berputar selama nilai 'angka' kurang dari 10
while angka < 10:
    # 3. Increment: Menambahkan nilai angka sebesar 1 di setiap putaran
    # 'angka += 1' sama artinya dengan 'angka = angka + 1'
    angka += 1
    
    # Python memiliki fitur unik: kita bisa mengalikan String dengan Integer!
    # Contoh: "*" * 3 akan menghasilkan "***"
    print("*" * angka)

# Kode di luar indentasi while akan dieksekusi setelah loop selesai
print("========================================================")
print(f"Perulangan selesai! Nilai akhir variabel angka adalah: {angka}")

# CATATAN EDUKASI - TABEL PENELUSURAN (TRACE TABLE):
# Putaran ke-1 : angka = 1  -> Cetak: *
# Putaran ke-2 : angka = 2  -> Cetak: **
# Putaran ke-3 : angka = 3  -> Cetak: ***
# ...
# Putaran ke-10: angka = 10 -> Cetak: **********
# Putaran ke-11: Cek kondisi (10 < 10) bernilai False -> Loop BERHENTI!