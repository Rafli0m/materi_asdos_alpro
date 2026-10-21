# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 17: Penentuan Bilangan Ganjil atau Genap
# ==============================================================================

"""
CERITA SOAL:
Seorang guru SD ingin membantu muridnya memeriksa apakah suatu angka yang dimasukkan tergolong bilangan ganjil atau genap.
"""

# 1. Minta input sebuah bilangan bulat ke dalam variabel bilangan
bilangan = int(input("Masukkan sebuah bilangan bulat: "))

# 2. Periksa sisa bagi bilangan tersebut dengan 2 (bilangan % 2)
# 3. Tampilkan pesan f-string yang menyatakan apakah bilangan tersebut bernilai genap atau ganjil
if bilangan % 2 == 0:
    print(f"Bilangan {bilangan} adalah bilangan GENAP.")
else:
    print(f"Bilangan {bilangan} adalah bilangan GANJIL.")

