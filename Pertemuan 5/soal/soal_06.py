# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 6: Konversi Menit ke Jam
# ==============================================================================

"""
CERITA SOAL:
Sebuah film dokumenter memiliki durasi total 145 menit. Penonton ingin mengetahui durasi tersebut dalam format jam dan sisa menit.
"""

# 1. Buat variabel total_menit bernilai 145
total_menit = 145

# 2. Hitung jumlah jam menggunakan pembagian bulat dengan 60 (// 60) ke dalam variabel jam
jam = total_menit // 60

# 3. Hitung sisa menit menggunakan operator modulus dengan 60 (% 60) ke dalam variabel sisa_menit
sisa_menit = total_menit % 60

# 4. Tampilkan nilai jam dan sisa_menit ke layar
print(f"Durasi total : {total_menit} menit")
print(f"Konversi     : {jam} jam {sisa_menit} menit")

