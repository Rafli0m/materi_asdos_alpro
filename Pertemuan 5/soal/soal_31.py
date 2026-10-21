# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 31: Hitung Mundur Peluncuran
# ==============================================================================

"""
CERITA SOAL:
Pusat sains membuat simulasi hitung mundur peluncuran roket sederhana dari angka 5 sampai 1, diakhiri dengan seruan peluncuran.
"""

# 1. Inisialisasi variabel hitung = 5
hitung = 5

# 2. Gunakan perulangan while hitung >= 1 untuk mencetak nilai hitung
while hitung >= 1:
    print(f"Hitungan mundur: {hitung}")
    # 3. Kurangi nilai hitung sebanyak 1 pada setiap iterasi
    hitung -= 1

# 4. Setelah perulangan selesai, cetak teks "Roket Meluncur!"
print("Roket Meluncur!")

