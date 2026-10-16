# ==============================================================================
# PERTEMUAN 3: STRUKTUR KONTROL PERCABANGAN (IF - ELIF - ELSE)
# ==============================================================================
# Percabangan digunakan untuk membuat keputusan dalam program berdasarkan 
# suatu kondisi tertentu (apakah bernilai True atau False).
#
# CARA KERJA DI PYTHON:
# 1. 'if'   : Mengevaluasi kondisi pertama.
# 2. 'elif' : Singkatan dari "else if". Dijalankan HANYA jika kondisi 'if' di atasnya bernilai False.
# 3. 'else' : Pilihan terakhir/cadangan jika SELURUH kondisi if/elif di atas bernilai False.
#
# PENTING TENTANG INDENTASI:
# Python menggunakan spasi/indentasi (umumnya 4 spasi atau 1 tab) untuk 
# menentukan baris mana yang merupakan bagian di dalam blok if/elif/else.
# ==============================================================================

# Input angka dari pengguna dan langsung konversi ke tipe integer (int)
x = int(input("Masukkan sembarang angka : "))

print("\n--- Hasil Evaluasi Percabangan ---")

# Evaluasi dilakukan bertahap dari atas ke bawah:
if x > 10:
    # Blok ini dieksekusi jika angka bernilai 11, 12, 13, dst.
    print(f"Nilai {x} lebih besar dari 10")
    
elif x >= 5:
    # Blok ini dieksekusi jika kondisi di atas False (x <= 10) DAN x >= 5.
    # Artinya rentang nilainya adalah antara 5 sampai 10.
    print(f"Nilai {x} berada di rentang 5 sampai 10")
    
elif x >= 3:
    # Blok ini dieksekusi jika x < 5 DAN x >= 3.
    # Artinya nilainya adalah 3 atau 4.
    print(f"Nilai {x} berada di rentang 3 sampai 4")
    
else:
    # Blok ini dieksekusi jika SEMUA kondisi di atas tidak terpenuhi (x < 3).
    print(f"Nilai {x} berada di bawah 3")

print("----------------------------------")
print("Program selesai dieksekusi.")