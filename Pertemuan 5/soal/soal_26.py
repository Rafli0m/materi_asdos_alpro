# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 26: Menu Pilihan Minuman
# ==============================================================================

"""
CERITA SOAL:
Kedai minuman memiliki menu sederhana: nomor 1 untuk Es Kopi (Rp10.000) dan nomor 2 untuk Es Teh (Rp5.000).
"""

print("--- MENU KEDAI MINUMAN ---")
print("1. Es Kopi (Rp10.000)")
print("2. Es Teh  (Rp5.000)")

# 1. Minta input nomor pilihan menu (str) ke dalam variabel pilihan
pilihan = str(input("Pilih nomor menu (1/2): "))

# 2. Gunakan if-elif-else:
if pilihan == "1":
    print("Rincian: Es Kopi - Harga: Rp10.000")
elif pilihan == "2":
    print("Rincian: Es Teh - Harga: Rp5.000")
else:
    print("Menu tidak tersedia")

