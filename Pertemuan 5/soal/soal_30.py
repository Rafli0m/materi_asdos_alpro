# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 30: Kalkulator Operasi Tambah dan Kurang
# ==============================================================================

"""
CERITA SOAL:
Program kalkulator sederhana dapat menghitung operasi penjumlahan atau pengurangan berdasarkan pilihan simbol dari pengguna.
"""

# 1. Minta input dua buah bilangan desimal (float) dan satu simbol operator ("+" atau "-")
bil1 = float(input("Masukkan bilangan pertama: "))
bil2 = float(input("Masukkan bilangan kedua: "))
operator = str(input("Masukkan operator (+ atau -): ")).strip()

# 2. Periksa operator dan cetak hasil
if operator == "+":
    hasil = bil1 + bil2
    print(f"Hasil: {bil1} + {bil2} = {hasil}")
elif operator == "-":
    hasil = bil1 - bil2
    print(f"Hasil: {bil1} - {bil2} = {hasil}")
else:
    print("operator tidak didukung")

