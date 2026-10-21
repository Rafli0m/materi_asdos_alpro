# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 38: Menghitung Target Dana Sosial
# ==============================================================================

"""
CERITA SOAL:
Panitia bakti sosial mengumpulkan donasi hingga mencapai target minimal Rp100.000. Program terus meminta nominal donasi baru hingga target terpenuhi.
"""

# 1. Inisialisasi variabel dana_terkumpul = 0
dana_terkumpul = 0

# 2. Gunakan perulangan while dana_terkumpul < 100000
while dana_terkumpul < 100000:
    # 3. Minta input nominal donasi (int) dan tambahkan ke dana_terkumpul
    donasi = int(input("Masukkan nominal donasi: Rp"))
    dana_terkumpul += donasi
    # 4. Tampilkan total dana terkumpul saat ini
    print(f"Total dana terkumpul saat ini: Rp{dana_terkumpul:,}")

# 5. Setelah perulangan berhenti, tampilkan pesan bahwa target donasi telah tercapai
print("Target donasi telah tercapai (Minimal Rp100.000)!")

