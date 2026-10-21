# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# CHALLENGE: Perhitungan Biaya Pengisian Bensin SPBU
# ==============================================================================

"""
Sebuah SPBU melayani pengisian bahan bakar kendaraan dengan total biaya yang dihitung 
dari jumlah liter bensin yang dibeli dan harga dasar per liternya.

Spesifikasi:
• Buat fungsi dengan return hitung_biaya_bensin(jumlah_liter, harga_per_liter).
• Menerima dua parameter integer: jumlah_liter dan harga_per_liter.
• Hitung total biaya dengan mengalikan kedua parameter tersebut.
• Kembalikan (return) total biaya pembelian yang didapat.
"""

# 1. Buat fungsi dengan return hitung_biaya_bensin(jumlah_liter, harga_per_liter)
# 2. Menerima dua parameter integer: jumlah_liter dan harga_per_liter
def hitung_biaya_bensin(jumlah_liter, harga_per_liter):
    # 3. Hitung total biaya dengan mengalikan kedua parameter tersebut
    total_biaya = jumlah_liter * harga_per_liter
    # 4. Kembalikan (return) total biaya pembelian yang didapat
    return total_biaya


# Contoh pengujian / pemanggilan fungsi
jumlah_liter = 10
harga_per_liter = 10000

total = hitung_biaya_bensin(jumlah_liter, harga_per_liter)
print("Jumlah liter      :", jumlah_liter, "liter")
print("Harga per liter   : Rp", harga_per_liter)
print("Total biaya bensin: Rp", total)
