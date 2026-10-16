# ==============================================================================
# PERTEMUAN 2: OPERATOR ARITMATIKA DASAR DI PYTHON
# ==============================================================================
# Operator aritmatika digunakan untuk melakukan operasi matematika dasar.
# ==============================================================================

# Nilai awal / Operand
angka1 = 24
angka2 = 5

print("==================================================")
print(f"Nilai angka 1 = {angka1}")
print(f"Nilai angka 2 = {angka2}")
print("==================================================")

# 1. Penjumlahan (+)
# Menjumlahkan dua bilangan
penjumlahan = angka1 + angka2
print(f"1. Penjumlahan      ({angka1} + {angka2})  = {penjumlahan}")

# 2. Pengurangan (-)
# Mengurangkan bilangan pertama dengan bilangan kedua
pengurangan = angka1 - angka2
print(f"2. Pengurangan      ({angka1} - {angka2})  = {pengurangan}")

# 3. Perkalian (*)
# Mengalikan dua bilangan
perkalian = angka1 * angka2
print(f"3. Perkalian        ({angka1} * {angka2})  = {perkalian}")

# 4. Pembagian Desimal (/)
# Pembagian biasa yang SELALU menghasilkan bilangan desimal (float)
pembagian = angka1 / angka2
print(f"4. Pembagian (/)    ({angka1} / {angka2})  = {pembagian}")

# 5. Pembagian Bulat / Floor Division (//)
# Membagi dua angka dan membulatkan ke bawah (membuang bagian desimal)
floor_division = angka1 // angka2
print(f"5. Pembagian Bulat (//) ({angka1} // {angka2}) = {floor_division}")

# 6. Modulus / Sisa Bagi (%)
# Menghasilkan sisa dari hasil pembagian bulat.
# Contoh: 24 dibagi 5 adalah 4 dengan sisa 4 (karena 5 * 4 = 20, 24 - 20 = 4).
# Modulus sangat sering dipakai untuk cek bilangan ganjil/genap (angka % 2 == 0).
modulus = angka1 % angka2
print(f"6. Modulus / Sisa Bagi (%) ({angka1} % {angka2}) = {modulus}")

# 7. Perpangkatan / Eksponen (**)
# Memangkatkan angka1 sebesar angka2 (24 dipangkatkan 5)
pangkat = angka1 ** angka2
print(f"7. Pangkat (**)     ({angka1} ** {angka2}) = {pangkat}")
print("==================================================")