# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 22: Autentikasi Sandi Brankas
# ==============================================================================

"""
CERITA SOAL:
Sebuah brankas elektronik sederhana membutuhkan verifikasi PIN angka rahasia ("1234") sebelum membuka pintu.
"""

# 1. Minta input PIN dari pengguna sebagai teks (str) ke dalam variabel input_pin
input_pin = str(input("Masukkan PIN Brankas: "))

# 2. Jika input_pin == "1234", tampilkan pesan "Akses diterima, pintu terbuka"
if input_pin == "1234":
    print("Akses diterima, pintu terbuka")
# 3. Jika salah, tampilkan pesan "Akses ditolak, PIN salah"
else:
    print("Akses ditolak, PIN salah")

