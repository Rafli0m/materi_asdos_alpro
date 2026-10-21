# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 5: Sisa Uang Saku
# ==============================================================================

"""
CERITA SOAL:
Rian memiliki uang saku mingguan sebesar Rp150.000. Selama seminggu, ia telah mengeluarkan uang sebesar Rp85.000 untuk makan dan Rp20.000 untuk fotokopi materi kuliah.
"""

# 1. Buat variabel uang_saku bernilai 150000, biaya_makan bernilai 85000, dan biaya_fotokopi bernilai 20000
uang_saku = 150000
biaya_makan = 85000
biaya_fotokopi = 20000

# 2. Hitung sisa uang dengan mengurangkan uang saku dengan total pengeluaran ke dalam variabel sisa_uang
sisa_uang = uang_saku - (biaya_makan + biaya_fotokopi)

# 3. Tampilkan nilai sisa_uang ke layar
print(f"Uang saku awal : Rp{uang_saku:,}")
print(f"Biaya makan    : Rp{biaya_makan:,}")
print(f"Biaya fotokopi : Rp{biaya_fotokopi:,}")
print(f"Sisa uang saku : Rp{sisa_uang:,}")

