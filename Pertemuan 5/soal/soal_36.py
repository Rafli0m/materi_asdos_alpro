# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 36: Akumulator Kasir Belanja
# ==============================================================================

"""
CERITA SOAL:
Kasir toko kelontong memasukkan harga barang satu per satu dan menjumlahkannya. Input akan berhenti ketika kasir memasukkan harga 0.
"""

# 1. Inisialisasi variabel total_belanja = 0
total_belanja = 0

# 2. Gunakan while True untuk menerima input harga barang (int)
while True:
    harga = int(input("Masukkan harga barang (masukkan 0 jika selesai): Rp"))
    
    # 3. Jika harga bernilai 0, hentikan perulangan dengan break
    if harga == 0:
        break
        
    # 4. Jika harga lebih dari 0, tambahkan ke total_belanja
    if harga > 0:
        total_belanja += harga

# 5. Setelah perulangan selesai, tampilkan total belanja akhir
print(f"Total belanja akhir: Rp{total_belanja:,}")

