# ==============================================================================
# PERTEMUAN 4: TUGAS / CHALLENGE - MENGHITUNG KELILING BANGUN DATAR
# ==============================================================================
# KETENTUAN SOAL ('challengs.pdf'):
# 1. Gunakan perulangan 'while' agar program terus berjalan berulang.
# 2. Gunakan percabangan 'if-elif-else' untuk mengatur pilihan menu.
# 3. Menampilkan 3 pilihan menu:
#    - Menu 1: Keliling Persegi (Rumus: 4 * sisi)
#    - Menu 2: Keliling Persegi Panjang (Rumus: 2 * (panjang + lebar))
#    - Menu 3: Keluar dari program (menggunakan perintah 'break')
# 4. Jika input selain 1, 2, atau 3, tampilkan peringatan bahwa pilihan tidak valid,
#    lalu program otomatis kembali memunculkan menu utama.
# 5. Gunakan tipe data integer (int) atau float untuk input angka.
# ==============================================================================

# Ketentuan 1: Perulangan while True agar program tidak berhenti sampai dipilih menu keluar
while True:
    print("\n" + "="*10, "MENU HITUNG KELILING BANGUN DATAR", "="*10)
    print("1. Menghitung Keliling Persegi")
    print("2. Menghitung Keliling Persegi Panjang")
    print("3. Keluar dari Program")
    print("="*55)

    # Meminta input menu
    menu = input("Silahkan pilih menu (1-3): ")

    # Ketentuan 2 & 3: Percabangan if-elif-else
    if menu == "1":
        print("\n--- Hitung Keliling Persegi ---")
        # Ketentuan 5: Menggunakan float agar dapat menerima bilangan bulat maupun desimal
        sisi = float(input("Masukkan panjang sisi : "))
        
        # Rumus: 4 * sisi
        keliling = 4 * sisi
        print(f"Keliling Persegi (4 x {sisi}) = {keliling:.2f}")

    elif menu == "2":
        print("\n--- Hitung Keliling Persegi Panjang ---")
        # Ketentuan 5: Input ukuran panjang dan lebar
        panjang = float(input("Masukkan panjang : "))
        lebar = float(input("Masukkan lebar   : "))
        
        # Rumus: 2 * (panjang + lebar)
        # Tanda kurung penting agar penjumlahan dihitung terlebih dahulu sebelum dikalikan 2
        keliling = 2 * (panjang + lebar)
        print(f"Keliling Persegi Panjang (2 x ({panjang} + {lebar})) = {keliling:.2f}")

    elif menu == "3":
        # Ketentuan 3: Keluar dari program dengan perintah 'break'
        print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")
        break

    else:
        # Ketentuan 4: Peringatan jika nomor menu tidak valid
        print("\n[Peringatan] Pilihan tidak valid! Silahkan pilih angka 1, 2, atau 3.")
        # Program akan otomatis memutar kembali ke awal loop while dan menampilkan menu utama
