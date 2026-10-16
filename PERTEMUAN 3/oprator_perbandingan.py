# ==============================================================================
# PERTEMUAN 3: OPERATOR PERBANDINGAN / RELASIONAL (COMPARISON OPERATORS)
# ==============================================================================
# Operator perbandingan digunakan untuk membandingkan dua buah nilai.
# Hasil dari evaluasi perbandingan SELALU berupa nilai Boolean: True atau False.
# ==============================================================================

# PENTING DIKETAHUI PEMULA:
# Fungsi input() di Python SELALU menghasilkan data bertipe String (teks).
# Jika ingin membandingkan nilai matematika/angka, kita HARUS mengonversinya
# (type casting) menjadi integer (int) atau float (float).
#
# AWAS JEBAKAN:
# Jika membandingkan string: "10" < "5" hasilnya True, karena Python 
# membandingkan karakter pertama ('1' vs '5') secara urutan alfabet/ASCII!
# Oleh karena itu, kita harus mengonversinya ke integer:

x_str = input("Masukkan angka pertama : ")
y_str = input("Masukkan angka kedua   : ")

# Konversi string ke integer agar perbandingan numerik akurat
x = int(x_str)
y = int(y_str)

print("\n" + "="*50)
print(f"Data yang diuji: x = {x} (tipe: {type(x).__name__}), y = {y} (tipe: {type(y).__name__})")
print("="*50)

# 1. Lebih Besar Dari (>)
# Bernilai True jika nilai x lebih besar daripada y
print(f"Apakah {x} >  {y}  (Lebih besar)          ? -> {x > y}")

# 2. Lebih Kecil Dari (<)
# Bernilai True jika nilai x lebih kecil daripada y
print(f"Apakah {x} <  {y}  (Lebih kecil)          ? -> {x < y}")

# 3. Sama Dengan (==)
# Ingat: Gunakan '==' untuk membandingkan, sedangkan '=' untuk mengisi variabel!
print(f"Apakah {x} == {y}  (Sama dengan)          ? -> {x == y}")

# 4. Lebih Besar atau Sama Dengan (>=)
# Bernilai True jika x lebih besar atau nilainya sama persis dengan y
print(f"Apakah {x} >= {y}  (Lebih besar/sama)     ? -> {x >= y}")

# 5. Lebih Kecil atau Sama Dengan (<=)
# Bernilai True jika x lebih kecil atau nilainya sama persis dengan y
print(f"Apakah {x} <= {y}  (Lebih kecil/sama)     ? -> {x <= y}")

# 6. Tidak Sama Dengan (!=)
# Bernilai True jika nilai x BERBEDA dengan nilai y
print(f"Apakah {x} != {y}  (Tidak sama dengan)    ? -> {x != y}")

print("==================================================")
