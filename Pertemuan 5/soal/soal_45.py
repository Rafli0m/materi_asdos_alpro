# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 45: Cetak Pola Karakter Berulang
# ==============================================================================

"""
CERITA SOAL:
Pengguna ingin mencetak karakter pagar ("#") sebanyak N baris sesuai jumlah yang ia inginkan ke layar terminal.
"""

# 1. Minta input jumlah baris (int) ke dalam variabel jumlah_baris
jumlah_baris = int(input("Masukkan jumlah baris pagar (#): "))

# 2. Inisialisasi variabel baris = 1
baris = 1

# 3. Gunakan while baris <= jumlah_baris untuk mencetak karakter "#"
while baris <= jumlah_baris:
    print("#")
    # 4. Tambahkan nilai baris sebanyak 1 pada setiap iterasi
    baris += 1

