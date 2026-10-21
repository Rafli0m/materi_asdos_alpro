# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 29: Cek Tahun Kelipatan Empat
# ==============================================================================

"""
CERITA SOAL:
Siswa ingin mengecek apakah suatu tahun merupakan tahun kabisat dasar, yaitu tahun yang habis dibagi 4.
"""

# 1. Minta input tahun (int) ke dalam variabel tahun
tahun = int(input("Masukkan tahun: "))

# 2. Gunakan kondisi tahun % 4 == 0 untuk memeriksa
# 3. Tampilkan keterangan apakah tahun tersebut merupakan tahun kabisat atau bukan menggunakan f-string
if tahun % 4 == 0:
    print(f"Tahun {tahun} merupakan TAHUN KABISAT (habis dibagi 4).")
else:
    print(f"Tahun {tahun} BUKAN tahun kabisat.")

