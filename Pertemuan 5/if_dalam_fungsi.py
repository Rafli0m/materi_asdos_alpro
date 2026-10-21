# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# TOPIK: Percabangan (if-elif-else) di dalam Fungsi
# ==============================================================================

"""
PENJELASAN UNTUK MAHASISWA:
1. Struktur IF-ELIF-ELSE dapat ditaruh di dalam fungsi untuk mengambil keputusan berdasarkan nilai parameter yang diterima.
2. Setiap kondisi akan dicek secara berurutan dari atas ke bawah.
3. Catatan Logika: Untuk predikat Cumlaude, masa studi harus tepat waktu (misal: lamalulus <= 8 semester).
"""

# ------------------------------------------------------------------------------
# 1. KODE UTAMA: Fungsi Menghitung Status Kelulusan
# ------------------------------------------------------------------------------

def menghitung_kelulusan(nilai, lamalulus):
    # Kondisi 1: Cumlaude (IPK >= 3.5 dan lama lulus <= 8 semester)
    if nilai >= 3.5 and lamalulus <= 8: 
        print("Selamat! Anda Cumlaude dengan nilai", nilai)
    # Kondisi 2: Lulus Sangat Baik (IPK >= 3.0 dan lama lulus <= 10 semester)
    elif nilai >= 3.0 and lamalulus <= 10:
        print("Selamat! Anda lulus dengan nilai", nilai)
    # Kondisi 3: Lulus (IPK >= 2.5 dan lama lulus <= 14 semester)
    elif nilai >= 2.5 and lamalulus <= 14:
        print("Selamat! Akhirnya kamu lulus dengan nilai", nilai)
    # Kondisi lainnya: Tidak memenuhi syarat di atas
    else:
        print("Yassudahh, semangat berjuang lagi!")

# Memanggil fungsi dengan berbagai contoh data mahasiswa
print("--- Hasil Cek Kelulusan ---")
menghitung_kelulusan(4.0, 7)   # Memenuhi syarat Cumlaude
menghitung_kelulusan(3.4, 9)   # Memenuhi syarat Lulus
menghitung_kelulusan(4.0, 11)  # Nilai tinggi tapi lebih dari 8 semester


# ------------------------------------------------------------------------------
# 2. CONTOH LAIN 1: Fungsi Menentukan Bilangan Ganjil atau Genap
# ------------------------------------------------------------------------------

def cek_ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        print(bilangan, "adalah bilangan GENAP")
    else:
        print(bilangan, "adalah bilangan GANJIL")

print("\n--- Cek Ganjil / Genap ---")
cek_ganjil_genap(8)
cek_ganjil_genap(13)


# ------------------------------------------------------------------------------
# 3. CONTOH LAIN 2: Fungsi Menentukan Status Kelulusan Ujian
# ------------------------------------------------------------------------------

def cek_nilai_ujian(skor):
    if skor >= 75:
        print("Skor", skor, ": Selamat, Anda LULUS!")
    else:
        print("Skor", skor, ": Maaf, Anda TIDAK LULUS!")

print("\n--- Cek Kelulusan Ujian ---")
cek_nilai_ujian(85)
cek_nilai_ujian(60)
