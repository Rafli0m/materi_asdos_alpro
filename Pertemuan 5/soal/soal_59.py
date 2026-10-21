# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 59: Penentuan Status Kelulusan Nilai
# ==============================================================================

"""
CERITA SOAL:
Bagian kurikulum membutuhkan fungsi logika untuk mengevaluasi apakah seorang siswa berhak lulus berdasarkan batas nilai minimal 75.
"""

# 1. Buat fungsi dengan return cek_kelulusan(nilai)
# 2. Menerima parameter nilai bertipe float atau integer
def cek_kelulusan(nilai: float) -> str:
    # 3. Jika nilai >= 75, kembalikan string "LULUS"
    if nilai >= 75:
        return "LULUS"
    # 4. Jika nilai < 75, kembalikan string "TIDAK LULUS"
    else:
        return "TIDAK LULUS"

# Pengujian fungsi
siswa_a = 82
siswa_b = 68
print(f"Nilai {siswa_a} => Status: {cek_kelulusan(siswa_a)}")
print(f"Nilai {siswa_b} => Status: {cek_kelulusan(siswa_b)}")

