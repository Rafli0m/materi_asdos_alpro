# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 40: Pengurangan Stok Barang Otomatis
# ==============================================================================

"""
CERITA SOAL:
Sebuah gudang memiliki persediaan awal 15 karung beras. Setiap kali truk pengantar datang, persediaan berkurang 3 karung hingga beras habis.
"""

# 1. Inisialisasi variabel stok_beras = 15
stok_beras = 15
print(f"Persediaan awal di gudang: {stok_beras} karung beras")

# 2. Gunakan while stok_beras > 0
while stok_beras > 0:
    # 3. Kurangi stok_beras sebesar 3 pada setiap iterasi dan cetak sisa stok saat ini
    stok_beras -= 3
    print(f"Truk datang... Sisa persediaan beras saat ini: {stok_beras} karung")

# 4. Setelah stok bernilai 0, cetak pesan "Stok beras habis"
print("Stok beras habis")

