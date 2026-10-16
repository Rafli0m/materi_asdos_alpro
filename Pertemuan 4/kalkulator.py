# ==============================================================================
# PERTEMUAN 4: KALKULATOR DENGAN PERULANGAN (WHILE TRUE & BREAK)
# ==============================================================================
# Program ini mendemonstrasikan implementasi 'while True'.
# 'while True' membuat program terus berjalan tanpa henti sampai kita memanggil
# perintah 'break' untuk keluar secara paksa dari perulangan.
# ==============================================================================

while True:
    print("\n" + "="*12, "KALKULATOR BERULANG", "="*12)
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian   (*)")
    print("4. Pembagian   (/)")
    print("5. Keluar dari Program")
    print("="*45)

    menu = input("Pilih Menu (1-5): ")

    # Pengecekan jika pengguna langsung memilih menu keluar (Menu 5)
    if menu == "5":
        print("\nTerima kasih telah menggunakan kalkulator. Sampai jumpa!")
        # 'break' berfungsi menghentikan perulangan while secara langsung
        break

    # Pengecekan untuk operasi perhitungan (Menu 1 s.d 4)
    elif menu in ["1", "2", "3", "4"]:
        # Menerima input angka (gunakan float agar mendukung bilangan desimal)
        angka1 = float(input("Masukkan angka pertama : "))
        angka2 = float(input("Masukkan angka kedua   : "))

        if menu == "1":
            hasil = angka1 + angka2
            print(f"Hasil Penjumlahan : {angka1} + {angka2} = {hasil}")

        elif menu == "2":
            hasil = angka1 - angka2
            print(f"Hasil Pengurangan : {angka1} - {angka2} = {hasil}")

        elif menu == "3":
            hasil = angka1 * angka2
            print(f"Hasil Perkalian   : {angka1} * {angka2} = {hasil}")

        elif menu == "4":
            # Validasi agar tidak terjadi error pembagian dengan nol
            if angka2 != 0:
                hasil = angka1 / angka2
                print(f"Hasil Pembagian   : {angka1} / {angka2} = {hasil}")
            else:
                print("[Error] Pembagian dengan nol (0) tidak diperbolehkan!")

    else:
        # Jika input tidak sesuai pilihan 1-5
        print("[Peringatan] Menu tidak tersedia! Silahkan masukkan angka 1 sampai 5.")

    # Opsi konfirmasi apakah ingin melanjutkan ke perhitungan berikutnya
    pilihan = input("\nApakah ingin menghitung lagi? (y/n) = ")
    if pilihan.lower() == "n":
        print("\nTerima kasih telah menggunakan kalkulator!")
        break