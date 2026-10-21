# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 12: Iuran Listrik Kamar Kos
# ==============================================================================

"""
CERITA SOAL:
Tagihan listrik rumah kos bulan ini adalah Rp360.000. Biaya tersebut akan dibagi rata secara bulat kepada 5 orang penghuni kos.
"""

# 1. Buat variabel total_tagihan bernilai 360000 dan jumlah_penghuni bernilai 5
total_tagihan = 360000
jumlah_penghuni = 5

# 2. Hitung tagihan per orang menggunakan pembagian bulat (//) ke dalam variabel tagihan_per_orang
tagihan_per_orang = total_tagihan // jumlah_penghuni

# 3. Tampilkan nilai tagihan_per_orang ke layar
print(f"Total tagihan listrik : Rp{total_tagihan:,}")
print(f"Jumlah penghuni       : {jumlah_penghuni} orang")
print(f"Tagihan per orang     : Rp{tagihan_per_orang:,}")

