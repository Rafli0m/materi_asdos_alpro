# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 39: Konfirmasi Pengulangan Hitung
# ==============================================================================

"""
CERITA SOAL:
Program menghitung perkalian dua angka yang terus berjalan berulang kali sampai pengguna mengetik "n" pada pertanyaan konfirmasi.
"""

# 1. Gunakan while True
while True:
    # 2. Di dalam perulangan, minta input dua angka bulat dan cetak hasil perkaliannya
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua  : "))
    hasil = angka1 * angka2
    print(f"Hasil perkalian: {angka1} x {angka2} = {hasil}")
    
    # 3. Tanyakan konfirmasi kepada pengguna: "Hitung lagi? [y/n] : "
    konfirmasi = input("Hitung lagi? [y/n] : ").strip().lower()
    
    # 4. Jika pengguna memasukkan "n", hentikan perulangan menggunakan break
    if konfirmasi == "n":
        print("Program selesai. Terima kasih!")
        break

