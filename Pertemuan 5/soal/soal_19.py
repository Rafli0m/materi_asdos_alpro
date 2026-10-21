# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 19: Kategori Tiket Wahana Bermain
# ==============================================================================

"""
CERITA SOAL:
Wahana permainan taman hiburan memberlakukan tarif tiket berbeda: pengunjung dengan tinggi badan di bawah 120 cm membayar tarif anak Rp25.000, sedangkan tinggi 120 cm ke atas membayar tarif dewasa Rp40.000.
"""

# 1. Minta input tinggi badan dalam cm (int) ke dalam variabel tinggi_badan
tinggi_badan = int(input("Masukkan tinggi badan (cm): "))

# 2. Gunakan percabangan if-else untuk menentukan harga tiket
if tinggi_badan < 120:
    kategori = "Anak-anak"
    harga_tiket = 25000
else:
    kategori = "Dewasa"
    harga_tiket = 40000

# 3. Tampilkan kategori dan harga tiket yang harus dibayar menggunakan f-string
print(f"Kategori Pengunjung : {kategori}")
print(f"Harga Tiket         : Rp{harga_tiket:,}")

