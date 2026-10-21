# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 27: Penilaian Batas Lulus Kehadiran
# ==============================================================================

"""
CERITA SOAL:
Mahasiswa diperbolehkan mengikuti ujian akhir semester jika persentase kehadirannya minimal 75%.
"""

# 1. Minta input persentase kehadiran (float) ke dalam variabel kehadiran
kehadiran = float(input("Masukkan persentase kehadiran (%): "))

# 2. Jika kehadiran >= 75.0, tampilkan pesan diizinkan mengikuti ujian
if kehadiran >= 75.0:
    print(f"Kehadiran {kehadiran}%: Mahasiswa DIIZINKAN mengikuti ujian akhir semester.")
# 3. Jika di bawah 75.0, tampilkan pesan dilarang mengikuti ujian karena kehadiran kurang
else:
    print(f"Kehadiran {kehadiran}%: Mahasiswa DILARANG mengikuti ujian karena kehadiran kurang (< 75%).")

