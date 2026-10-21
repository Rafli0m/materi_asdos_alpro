# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 20: Diskon Belanja Supermarket
# ==============================================================================

"""
CERITA SOAL:
Supermarket memberikan potongan harga langsung sebesar Rp15.000 jika total belanja pelanggan mencapai Rp100.000 atau lebih.
"""

# 1. Minta input total belanja (int) ke dalam variabel total_belanja
total_belanja = int(input("Masukkan total belanja: Rp"))

# 2. Jika total_belanja >= 100000, kurangi total belanja dengan 15000
if total_belanja >= 100000:
    total_belanja -= 15000
    print("Selamat! Anda mendapatkan potongan langsung Rp15.000.")

# 3. Tampilkan total pembayaran akhir menggunakan f-string
print(f"Total pembayaran akhir: Rp{total_belanja:,}")

