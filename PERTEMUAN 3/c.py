# ==============================================================================
# PERTEMUAN 3: TUGAS / CHALLENGE - MENGHITUNG LUAS BANGUN DATAR
# ==============================================================================
# Sesuai kriteria soal 'challens.pdf':
# 1. Menu Interaktif untuk Lingkaran, Segitiga, dan Persegi Panjang.
# 2. Struktur Kontrol (Percabangan): Menggunakan if-elif-else.
# 3. Tipe Data Input:
#    - Pilihan menu dikonversi menjadi integer (int).
#    - Ukuran (jari-jari, alas, tinggi, panjang, lebar) dikonversi ke desimal (float).
# 4. Rumus Perhitungan:
#    - Lingkaran        : Luas = pi * r * r (pi = 3.14)
#    - Segitiga         : Luas = 0.5 * alas * tinggi
#    - Persegi Panjang  : Luas = panjang * lebar
# 5. Penanganan Error   : Menampilkan peringatan jika menu selain 1, 2, atau 3.
# ==============================================================================

# Menggunakan perulangan while True agar program dapat diulang jika pengguna ingin menghitung lagi
while True:
    print("\n" + "="*12, "PILIH MENU PERHITUNGAN", "="*12)
    print("1. Menghitung Luas Lingkaran")
    print("2. Menghitung Luas Segitiga")
    print("3. Menghitung Luas Persegi Panjang")
    print("="*48)

    # Kriteria 3a: Input pilihan menu dikonversi ke tipe data integer (int)
    try:
        menu = int(input("Silahkan pilih menu (1-3): "))
    except ValueError:
        print("[Peringatan] Harap masukkan angka bulat yang valid!")
        continue

    # Kriteria 2 & 4: Struktur percabangan dan rumus perhitungan
    if menu == 1:
        print("\n--- Perhitungan Luas Lingkaran ---")
        pi = 3.14
        # Kriteria 3b: Input ukuran dikonversi ke desimal (float)
        r = float(input("Masukkan Jari-jari (r) : "))
        hasil = pi * (r ** 2)
        print(f"Luas Lingkaran (pi * r^2) adalah : {hasil:.2f}")

    elif menu == 2:
        print("\n--- Perhitungan Luas Segitiga ---")
        # Kriteria 3b: Input ukuran dikonversi ke desimal (float)
        alas = float(input("Masukkan Alas (a)   : "))
        tinggi = float(input("Masukkan Tinggi (t) : "))
        hasil = 0.5 * alas * tinggi
        print(f"Luas Segitiga (0.5 * a * t) adalah : {hasil:.2f}")

    elif menu == 3:
        print("\n--- Perhitungan Luas Persegi Panjang ---")
        # Kriteria 3b: Input ukuran dikonversi ke desimal (float)
        panjang = float(input("Masukkan Panjang (p) : "))
        lebar = float(input("Masukkan Lebar (l)   : "))
        hasil = panjang * lebar
        print(f"Luas Persegi Panjang (p * l) adalah : {hasil:.2f}")

    else:
        # Kriteria 5: Penanganan input menu selain 1, 2, atau 3
        print("\n[Peringatan] Input salah! Silahkan pilih menu 1, 2, atau 3.")

    # Menanyakan kepada pengguna apakah ingin mengulang program
    print("\n" + "-"*48)
    pilihan = input("Apakah Anda ingin mengulang program? (y/n): ")

    # Jika input BUKAN 'y' atau 'Y', hentikan perulangan dengan break
    if pilihan.lower() != 'y':
        print("\nTerima kasih telah menggunakan program perhitungan luas bangun datar!")
        break