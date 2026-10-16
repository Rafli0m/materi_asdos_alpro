# ==============================================================================
# PERTEMUAN 3: OPERATOR LOGIKA (LOGICAL OPERATORS)
# ==============================================================================
# Operator logika digunakan untuk menggabungkan dua atau lebih kondisi boolean.
# Di Python, terdapat 3 operator logika utama:
# 1. and : Bernilai True HANYA JIKA seluruh kondisi bernilai True.
# 2. or  : Bernilai True JIKA SALAH SATU (atau kedua) kondisi bernilai True.
# 3. not : Membalik nilai logika (True menjadi False, False menjadi True).
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. CONTOH INPUT DATA UNTUK PENGUJIAN
# ------------------------------------------------------------------------------
x = int(input("Masukkan angka pertama (x) : "))
y = int(input("Masukkan angka kedua   (y) : "))

print("\n" + "="*50)
print(f"Nilai yang dimasukkan: x = {x}, y = {y}")
print("="*50)

# Misal kita memiliki dua kondisi:
# Kondisi 1: Apakah x lebih besar dari y? (x > y)
# Kondisi 2: Apakah x sama dengan y?      (x == y)
kondisi1 = x > y
kondisi2 = x == y

print(f"Kondisi 1: (x > y)  -> {kondisi1}")
print(f"Kondisi 2: (x == y) -> {kondisi2}")
print("--------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. OPERATOR AND
# ------------------------------------------------------------------------------
# Aturan AND: True and True = True. Selain itu semuanya bernilai False.
hasil_and = kondisi1 and kondisi2
print(f"Hasil (x > y) AND (x == y) : {hasil_and}")
print("-> Catatan: Hanya True jika x lebih besar DAN sekaligus sama dengan y.")

# ------------------------------------------------------------------------------
# 3. OPERATOR OR
# ------------------------------------------------------------------------------
# Aturan OR: Cukup salah satu kondisi True, hasilnya pasti bernilai True.
hasil_or = kondisi1 or kondisi2
print(f"Hasil (x > y) OR  (x == y) : {hasil_or}")
print("-> Catatan: Bernilai True jika x lebih besar ATAU x sama dengan y (artinya x >= y).")

# ------------------------------------------------------------------------------
# 4. OPERATOR NOT
# ------------------------------------------------------------------------------
# Aturan NOT: Membalik nilai. not True = False, not False = True.
hasil_not = not kondisi1
print(f"Hasil NOT (x > y)          : {hasil_not}")
print(f"-> Catatan: Membalikkan hasil kondisi 1 ({kondisi1} dibalik menjadi {hasil_not}).")

print("==================================================")