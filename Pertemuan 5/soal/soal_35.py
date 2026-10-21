# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 35: Batas Percobaan PIN Kartu
# ==============================================================================

"""
CERITA SOAL:
Mesin transaksi memberikan kesempatan maksimal 3 kali kepada pengguna untuk memasukkan PIN yang benar sebelum sistem terkunci.
"""

# 1. Inisialisasi variabel percobaan = 1
percobaan = 1

# 2. Gunakan while percobaan <= 3 untuk meminta input PIN teks dari pengguna
while percobaan <= 3:
    pin = str(input(f"Percobaan {percobaan}/3: Masukkan PIN Anda: "))
    
    # 3. Jika PIN bernilai "9999", tampilkan pesan sukses dan keluar dengan break
    if pin == "9999":
        print("PIN Benar! Akses berhasil diberikan.")
        break
    
    # 4. Jika salah dan percobaan mencapai 3, tampilkan pesan "Kartu diblokir"
    if percobaan == 3:
        print("Kartu diblokir")
        
    # 5. Tingkatkan nilai percobaan setiap kali tebakan salah
    percobaan += 1

