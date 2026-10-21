# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 55: Papan Skor Game Sederhana
# ==============================================================================

"""
CERITA SOAL:
Pengembang game konsol teks ingin menampilkan papan skor sementara pemain setiap kali menyelesaikan sebuah ronde.
"""

# 1. Buat fungsi dengan parameter tampilkan_skor(nama_pemain, poin)
# 2. Menerima parameter nama_pemain (string) dan poin (integer), tanpa return
def tampilkan_skor(nama_pemain: str, poin: int):
    # 3. Tampilkan nama pemain beserta total poin yang diraihnya
    print(f"Pemain: {nama_pemain} | Total Poin: {poin} Poin")

# Contoh pemanggilan fungsi
tampilkan_skor("PlayerOne", 1500)

