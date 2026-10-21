# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 56: Konversi Suhu Celcius ke Fahrenheit
# ==============================================================================

"""
CERITA SOAL:
Petugas stasiun cuaca membutuhkan fungsi yang menghitung dan mengembalikan nilai konversi dari satuan derajat Celcius ke Fahrenheit.
"""

# 1. Buat fungsi dengan return celcius_ke_fahrenheit(suhu_c)
# 2. Menerima parameter suhu_c (float)
def celcius_ke_fahrenheit(suhu_c: float) -> float:
    # 3. Hitung nilai Fahrenheit dengan rumus (suhu_c * 1.8) + 32
    hasil_fahrenheit = (suhu_c * 1.8) + 32
    # 4. Kembalikan (return) hasil perhitungan tersebut
    return hasil_fahrenheit

# Pengujian fungsi
suhu_input = 100.0
hasil = celcius_ke_fahrenheit(suhu_input)
print(f"Suhu Celcius    : {suhu_input} C")
print(f"Hasil Fahrenheit: {hasil} F")

