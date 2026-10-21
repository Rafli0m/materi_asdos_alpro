# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 33: Total Tabungan Celengan
# ==============================================================================

"""
CERITA SOAL:
Budi menabung uang setiap hari sebesar Rp5.000 selama 7 hari berturut-turut. Ia ingin menghitung akumulasi saldo tabungannya hari demi hari.
"""

# 1. Inisialisasi variabel hari = 1 dan total_tabungan = 0
hari = 1
total_tabungan = 0

# 2. Gunakan perulangan while hari <= 7
while hari <= 7:
    # 3. Tambahkan 5000 ke total_tabungan dan cetak saldo hari tersebut dengan f-string
    total_tabungan += 5000
    print(f"Hari ke-{hari}: Saldo Tabungan = Rp{total_tabungan:,}")
    # 4. Tambahkan nilai hari sebanyak 1 pada setiap iterasi
    hari += 1

