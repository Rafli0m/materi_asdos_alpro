# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 16: Pengecekan Usia Pembuatan KTP
# ==============================================================================

"""
CERITA SOAL:
Petugas kelurahan membutuhkan program mini untuk memverifikasi apakah pemohon sudah cukup umur untuk membuat Kartu Tanda Penduduk (minimal 17 tahun).
"""

# 1. Minta input usia dari pengguna dan konversi ke integer ke dalam variabel usia
usia = int(input("Masukkan usia Anda: "))

# 2. Jika usia >= 17, tampilkan pesan bahwa pengguna sudah berhak membuat KTP menggunakan f-string
if usia >= 17:
    print(f"Usia Anda {usia} tahun. Anda SUDAH BERHAK membuat KTP.")
# 3. Jika kurang dari 17, tampilkan pesan bahwa usia belum mencukupi
else:
    print(f"Usia Anda {usia} tahun. Usia Anda BELUM MENCUKUPI untuk membuat KTP.")

