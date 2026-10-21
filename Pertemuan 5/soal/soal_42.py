# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 42: Penghitung Jumlah Data Input
# ==============================================================================

"""
CERITA SOAL:
Petugas sensus memasukkan data umur warga satu demi satu. Penginputan data akan berakhir jika petugas memasukkan angka -1.
"""

# 1. Inisialisasi variabel jumlah_orang = 0
jumlah_orang = 0

# 2. Gunakan while True untuk menerima input data umur (int)
while True:
    umur = int(input("Masukkan data umur warga (masukkan -1 untuk selesai): "))
    
    # 3. Jika input bernilai -1, hentikan perulangan dengan break
    if umur == -1:
        break
        
    # 4. Jika input bukan -1, tambahkan jumlah_orang sebanyak 1
    jumlah_orang += 1

# 5. Tampilkan total orang yang berhasil dicatat setelah loop selesai
print(f"Total orang yang berhasil dicatat setelah loop selesai: {jumlah_orang} orang")

