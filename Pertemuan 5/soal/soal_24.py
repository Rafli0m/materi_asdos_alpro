# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 24: Identifikasi Jenis Bilangan
# ==============================================================================

"""
CERITA SOAL:
Program matematika dasar perlu mengidentifikasi apakah bilangan yang dimasukkan pengguna bernilai positif, negatif, atau tepat nol.
"""

# 1. Minta input bilangan bulat (int) ke dalam variabel angka
angka = int(input("Masukkan sebuah bilangan bulat: "))

# 2. Gunakan if-elif-else untuk memeriksa apakah angka > 0, angka < 0, atau angka == 0
if angka > 0:
    kategori = "Positif"
elif angka < 0:
    kategori = "Negatif"
else:
    kategori = "Tepat Nol"

# 3. Tampilkan kategori bilangan tersebut ke layar dengan f-string
print(f"Bilangan {angka} adalah bilangan {kategori}.")

