# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 44: Menu Layanan Mandiri Bank
# ==============================================================================

"""
CERITA SOAL:
Mesin antrean bank menampilkan menu interaktif pilihan layanan (1: Setor Tunai, 2: Informasi Saldo, 3: Selesai) yang akan terus muncul sampai nasabah memilih nomor 3.
"""

# 1. Gunakan while True
while True:
    # 2. Cetak pilihan menu 1, 2, dan 3, kemudian minta input menu dari pengguna
    print("\n--- MENU LAYANAN MANDIRI BANK ---")
    print("1: Setor Tunai")
    print("2: Informasi Saldo")
    print("3: Selesai")
    
    pilihan = input("Pilih nomor layanan (1/2/3): ").strip()
    
    # 3. Jika menu "1", cetak keterangan layanan setor tunai
    if pilihan == "1":
        print("Keterangan: Anda memilih layanan Setor Tunai. Masukkan uang Anda.")
    # 4. Jika menu "2", cetak keterangan informasi saldo
    elif pilihan == "2":
        print("Keterangan: Anda memilih Informasi Saldo. Saldo Anda Rp2.500.000.")
    # 5. Jika menu "3", cetak ucapan terima kasih dan keluar menggunakan break
    elif pilihan == "3":
        print("Terima kasih telah menggunakan layanan mandiri bank kami.")
        break
    # 6. Jika pilihan lain, cetak "Pilihan tidak valid"
    else:
        print("Pilihan tidak valid")

