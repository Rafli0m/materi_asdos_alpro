# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 60: Hitung Biaya Sewa Lapangan Futsal
# ==============================================================================

"""
CERITA SOAL:
Pengelola gedung olahraga menerapkan tarif sewa lapangan futsal berdasarkan jumlah jam sewa dan tarif dasar per jamnya.
"""

# 1. Buat fungsi dengan return hitung_sewa_lapangan(durasi_jam, tarif_per_jam)
# 2. Menerima dua parameter integer: durasi_jam dan tarif_per_jam
def hitung_sewa_lapangan(durasi_jam: int, tarif_per_jam: int) -> int:
    # 3. Hitung total biaya dengan mengalikan kedua parameter tersebut
    total_biaya = durasi_jam * tarif_per_jam
    # 4. Kembalikan (return) total biaya sewa yang didapat
    return total_biaya

# Pengujian fungsi
durasi = 3
tarif = 120000
total = hitung_sewa_lapangan(durasi, tarif)
print(f"Durasi Sewa   : {durasi} Jam")
print(f"Tarif per Jam : Rp{tarif:,}")
print(f"Total Sewa    : Rp{total:,}")

