# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# TOPIK: Fungsi dengan Return (Nilai Kembalian)
# ==============================================================================

"""
PENJELASAN UNTUK MAHASISWA:
1. 'return' digunakan untuk mengembalikan hasil proses dari dalam fungsi ke baris pemanggil.
2. Perbedaan dengan print():
   - print() hanya menampilkan tulisan ke layar, nilainya tidak bisa disimpan atau dihitung lagi.
   - return mengembalikan nilai, sehingga hasilnya bisa disimpan ke dalam variabel atau dipakai untuk perhitungan lain.
"""

# ------------------------------------------------------------------------------
# 1. KODE UTAMA: Fungsi Menghitung Luas Persegi Panjang dengan Return
# ------------------------------------------------------------------------------

def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas  # Mengembalikan nilai variabel luas

# Memanggil fungsi dan menyimpan hasil kembaliannya ke variabel 'hasil_luas'
hasil_luas = luas_persegi_panjang(25, 10)

# Menampilkan hasil yang telah disimpan
print("Luas persegi panjang adalah:", hasil_luas)


# ------------------------------------------------------------------------------
# 2. CONTOH LAIN 1: Fungsi Menghitung Keliling Persegi
# ------------------------------------------------------------------------------

def keliling_persegi(sisi):
    keliling = 4 * sisi
    return keliling

# Memanggil fungsi
hasil_keliling = keliling_persegi(6)
print("Keliling persegi (sisi 6):", hasil_keliling)


# ------------------------------------------------------------------------------
# 3. CONTOH LAIN 2: Fungsi Konversi Suhu Celcius ke Fahrenheit
# ------------------------------------------------------------------------------

def celcius_ke_fahrenheit(suhu_c):
    suhu_f = (suhu_c * 1.8) + 32
    return suhu_f

# Memanggil fungsi konversi
hasil_suhu = celcius_ke_fahrenheit(30)
print("30 derajat Celcius dalam Fahrenheit adalah:", hasil_suhu)
