# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 28: Promo Gratis Ongkir Belanja Online
# ==============================================================================

"""
CERITA SOAL:
Toko daring memberikan gratis ongkir jika total belanja minimal Rp50.000 dan pembeli memiliki status member ("y").
"""

# 1. Minta input total belanja (int) dan status member ("y" atau "n")
total_belanja = int(input("Masukkan total belanja: Rp"))
status_member = str(input("Apakah memiliki status member? (y/n): ")).strip().lower()

# 2. Gunakan operator logika and: jika total_belanja >= 50000 and status_member == "y", tampilkan "Mendapatkan promo gratis ongkir"
if total_belanja >= 50000 and status_member == "y":
    print("Mendapatkan promo gratis ongkir")
# 3. Jika tidak memenuhi, tampilkan "Ongkos kirim normal"
else:
    print("Ongkos kirim normal")

