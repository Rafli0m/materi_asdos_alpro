# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 41: Simulasi Pengisian Galon Air
# ==============================================================================

"""
CERITA SOAL:
Sebuah galon air berkapasitas 19 liter diisi air dari kran dengan laju penambahan 2 liter setiap detik simulasi.
"""

# 1. Inisialisasi variabel isi_air = 0 dan detik = 0
isi_air = 0
detik = 0

# 2. Gunakan while isi_air < 19
while isi_air < 19:
    # 3. Tambahkan 2 pada isi_air dan 1 pada detik
    isi_air += 2
    detik += 1
    # 4. Tampilkan volume air pada detik berjalan menggunakan f-string
    print(f"Detik ke-{detik}: Volume air = {isi_air} liter")
    # 5. Jika volume melebihi atau sama dengan 19, tampilkan "Galon penuh"
    if isi_air >= 19:
        print("Galon penuh")

