# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 18: Ambang Kelulusan Ujian Teori
# ==============================================================================

"""
CERITA SOAL:
Sistem penilaian kursus komputer menetapkan bahwa peserta ujian dinyatakan lulus jika mendapatkan nilai minimal 70.
"""

# 1. Minta input nilai ujian berupa angka desimal (float) ke dalam variabel nilai_ujian
nilai_ujian = float(input("Masukkan nilai ujian teori: "))

# 2. Jika nilai_ujian >= 70.0, tampilkan "Status: Lulus" beserta nilainya
if nilai_ujian >= 70.0:
    print(f"Status: Lulus (Nilai: {nilai_ujian})")
# 3. Jika di bawah 70.0, tampilkan "Status: Tidak Lulus" beserta nilainya
else:
    print(f"Status: Tidak Lulus (Nilai: {nilai_ujian})")

