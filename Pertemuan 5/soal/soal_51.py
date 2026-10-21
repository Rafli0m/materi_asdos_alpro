# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 51: Sapaan Personal Mahasiswa
# ==============================================================================

"""
CERITA SOAL:
Sistem portal akademik ingin menyapa setiap mahasiswa yang login dengan menyebutkan nama lengkapnya di layar.
"""

# 1. Buat fungsi dengan parameter sapa_mahasiswa(nama)
# 2. Fungsi menerima satu parameter nama bertipe string dan tidak mengembalikan nilai
def sapa_mahasiswa(nama: str):
    # 3. Cetak kalimat sambutan hangat yang menyertakan nama mahasiswa menggunakan f-string
    print(f"Halo, Selamat Datang di Portal Akademik, {nama}! Semoga harimu menyenangkan.")

# Contoh pemanggilan fungsi
sapa_mahasiswa("Rafli Maulana")

