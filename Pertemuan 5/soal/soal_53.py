# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 53: Notifikasi Pengingat Rapat
# ==============================================================================

"""
CERITA SOAL:
Aplikasi kalender sekretariat membutuhkan fungsi cetak pengingat agenda pertemuan bagi pengurus organisasi.
"""

# 1. Buat fungsi dengan parameter ingatkan_agenda(nama_agenda, jam)
# 2. Fungsi menerima parameter nama_agenda (string) dan jam (string), tanpa return
def ingatkan_agenda(nama_agenda: str, jam: str):
    # 3. Tampilkan pesan pengingat agenda beserta jam pelaksanaannya menggunakan f-string
    print(f"[PENGINGAT AGENDA] Rapat '{nama_agenda}' akan dimulai pada pukul {jam} WIB. Harap hadir tepat waktu!")

# Contoh pemanggilan fungsi
ingatkan_agenda("Koordinasi Praktikum ALPRO", "14:00")

