# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 58: Hitung Harga Setelah Diskon
# ==============================================================================

"""
CERITA SOAL:
Kasir toko pakaian memerlukan fungsi matematika yang menghitung harga bersih suatu barang setelah dipotong persentase diskon.
"""

# 1. Buat fungsi dengan return hitung_harga_diskon(harga_asli, persen_diskon)
# 2. Menerima parameter harga_asli (int/float) dan persen_diskon (float dalam desimal, misal 0.2 untuk 20%)
def hitung_harga_diskon(harga_asli: float, persen_diskon: float) -> float:
    # 3. Hitung potongan harga (harga_asli * persen_diskon), lalu kurangkan dari harga_asli
    potongan = harga_asli * persen_diskon
    harga_akhir = harga_asli - potongan
    # 4. Kembalikan (return) harga akhir setelah diskon
    return harga_akhir

# Pengujian fungsi
harga = 200000
diskon = 0.20  # 20%
harga_bayar = hitung_harga_diskon(harga, diskon)
print(f"Harga Asli   : Rp{harga:,}")
print(f"Diskon       : {int(diskon * 100)}%")
print(f"Harga Bersih : Rp{harga_bayar:,.0f}")

