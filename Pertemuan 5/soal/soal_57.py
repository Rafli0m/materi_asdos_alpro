# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 57: Hitung Luas Persegi Panjang
# ==============================================================================

"""
CERITA SOAL:
Tukang bangunan membutuhkan fungsi pembantu untuk menghitung luas dinding ruangan sebelum mengecat.
"""

# 1. Buat fungsi dengan return hitung_luas_persegi_panjang(panjang, lebar)
# 2. Menerima dua parameter numerik: panjang dan lebar
def hitung_luas_persegi_panjang(panjang: float, lebar: float) -> float:
    # 3. Hitung luas dengan rumus panjang * lebar
    luas = panjang * lebar
    # 4. Kembalikan (return) nilai luas tersebut
    return luas

# Pengujian fungsi
p = 15.0
l = 8.0
luas_dinding = hitung_luas_persegi_panjang(p, l)
print(f"Panjang: {p} m, Lebar: {l} m => Luas: {luas_dinding} m2")

