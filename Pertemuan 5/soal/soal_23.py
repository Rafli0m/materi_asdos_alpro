# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 23: Peringatan Termometer Digital
# ==============================================================================

"""
CERITA SOAL:
Termometer digital di pintu masuk gedung akan memeriksa suhu badan pengunjung. Jika suhu 37.5 derajat Celsius atau lebih, pengunjung diminta beristirahat di pos kesehatan.
"""

# 1. Minta input suhu badan (float) ke dalam variabel suhu
suhu = float(input("Masukkan suhu badan (derajat Celcius): "))

# 2. Jika suhu >= 37.5, tampilkan pesan peringatan bahwa suhu tubuh tinggi
if suhu >= 37.5:
    print("Peringatan: Suhu tubuh tinggi! Pengunjung diminta beristirahat di pos kesehatan.")
# 3. Jika suhu < 37.5, tampilkan pesan bahwa suhu normal dan dipersilakan masuk
else:
    print("Suhu normal. Pengunjung dipersilakan masuk.")

