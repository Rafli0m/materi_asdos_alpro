# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 54: Format Label Undangan
# ==============================================================================

"""
CERITA SOAL:
Panitia seminar mencetak label tamu undangan yang berisi nama tamu dan instansi asalnya.
"""

# 1. Buat fungsi dengan parameter cetak_undangan(nama_tamu, instansi)
# 2. Menerima 2 parameter bertipe string tanpa mengembalikan nilai
def cetak_undangan(nama_tamu: str, instansi: str):
    # 3. Tampilkan format kartu undangan dengan garis pembatas di atas dan bawahnya
    print("====================================================")
    print(f"Kepada Yth. : {nama_tamu}")
    print(f"Instansi    : {instansi}")
    print("====================================================")

# Contoh pemanggilan fungsi
cetak_undangan("Dr. Ir. Bambang Hermanto, M.T.", "Universitas Teknologi Yogyakarta")

