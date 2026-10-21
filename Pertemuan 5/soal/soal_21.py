# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 21: Konversi Predikat Nilai Kuliah
# ==============================================================================

"""
CERITA SOAL:
Dosen ingin mengonversi nilai angka mahasiswa ke dalam predikat huruf dengan aturan: nilai 85 ke atas mendapat 'A', nilai 70 sampai 84 mendapat 'B', nilai 55 sampai 69 mendapat 'C', dan di bawah 55 mendapat 'D'.
"""

# 1. Minta input nilai angka (float) ke dalam variabel nilai
nilai = float(input("Masukkan nilai angka mahasiswa: "))

# 2. Gunakan struktur if-elif-else untuk menentukan predikat huruf
if nilai >= 85:
    predikat = 'A'
elif nilai >= 70:
    predikat = 'B'
elif nilai >= 55:
    predikat = 'C'
else:
    predikat = 'D'

# 3. Tampilkan predikat nilai yang diperoleh menggunakan f-string
print(f"Nilai {nilai} memperoleh predikat huruf '{predikat}'.")

