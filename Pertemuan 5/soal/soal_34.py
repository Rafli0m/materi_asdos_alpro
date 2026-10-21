# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 34: Tebak Angka Rahasia
# ==============================================================================

"""
CERITA SOAL:
Sebuah permainan sederhana meminta pengguna menebak angka rahasia (misal angka 7). Program akan terus meminta tebakan sampai pengguna berhasil menebak angka tersebut.
"""

# 1. Tetapkan angka rahasia pada variabel angka_rahasia = 7
angka_rahasia = 7

# 2. Gunakan while True untuk meminta input tebakan (int) dari pengguna
while True:
    tebakan = int(input("Tebak angka rahasia (1-10): "))
    
    # 3. Jika tebakan sama dengan angka_rahasia, tampilkan pesan selamat lalu hentikan perulangan dengan break
    if tebakan == angka_rahasia:
        print("Selamat! Tebakan Anda benar!")
        break
    # 4. Jika salah, tampilkan pesan bahwa tebakan masih salah
    else:
        print("Tebakan masih salah. Coba lagi!")

