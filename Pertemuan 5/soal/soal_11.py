# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 11: Potongan Diskon Kaos
# ==============================================================================

"""
CERITA SOAL:
Sebuah toko pakaian memberikan diskon 15% untuk sehelai kaos seharga Rp120.000. Pembeli ingin menghitung nominal potongan harga yang didapatkan.
"""

# 1. Buat variabel harga_kaos bernilai 120000 dan persen_diskon bernilai 0.15
harga_kaos = 120000
persen_diskon = 0.15

# 2. Hitung nilai potongan diskon dengan rumus harga_kaos * persen_diskon ke dalam variabel potongan_harga
potongan_harga = harga_kaos * persen_diskon

# 3. Tampilkan nilai potongan_harga ke layar
print(f"Harga kaos     : Rp{harga_kaos:,}")
print(f"Persen diskon  : {int(persen_diskon * 100)}%")
print(f"Potongan harga : Rp{potongan_harga:,.0f}")

