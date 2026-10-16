# ==============================================================================
# PERTEMUAN 2: MENGHITUNG LUAS PERSEGI PANJANG
# ==============================================================================
# Pola dasar pembuatan program algoritma terdiri dari 3 tahap:
# 1. INPUT   : Menyiapkan data yang dibutuhkan
# 2. PROSES  : Mengolah data dengan rumus matematika / logika
# 3. OUTPUT  : Menampilkan hasil olahan kepada pengguna
# ==============================================================================

# ------------------------------------------------------------------------------
# TAHAP 1: INPUT DATA (Inisialisasi Variabel)
# ------------------------------------------------------------------------------
# Kita menentukan ukuran panjang dan lebar bangun datar
panjang = 100
lebar = 5

# ------------------------------------------------------------------------------
# TAHAP 2: PROSES (Perhitungan Rumus)
# ------------------------------------------------------------------------------
# Rumus Luas Persegi Panjang = panjang * lebar
# Catatan edukasi: Jika persegi sama sisi, rumusnya adalah luas = sisi * sisi (sisi ** 2)
luas = panjang * lebar

# ------------------------------------------------------------------------------
# TAHAP 3: OUTPUT (Menampilkan Hasil)
# ------------------------------------------------------------------------------
print("=== PROGRAM MENGHITUNG LUAS PERSEGI PANJANG ===")
print(f"Panjang = {panjang} cm")
print(f"Lebar   = {lebar} cm")
print("-----------------------------------------------")
print(f"Luas Persegi Panjang (p x l) = {luas} cm^2")
print("===============================================")