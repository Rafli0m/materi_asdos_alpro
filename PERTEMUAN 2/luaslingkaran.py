# ==============================================================================
# PERTEMUAN 2: MENGHITUNG LUAS LINGKARAN
# ==============================================================================
# Program ini menghitung luas lingkaran berdasarkan jari-jari (r).
# Rumus Matematika: Luas = pi * r^2
# ==============================================================================

# ------------------------------------------------------------------------------
# TAHAP 1: INPUT DATA
# ------------------------------------------------------------------------------
# Jari-jari lingkaran (r)
jari_jari = 5

# Nilai konstanta pi
# Biasanya bernilai 3.14 atau 22/7
pi = 3.14

# ------------------------------------------------------------------------------
# TAHAP 2: PROSES PERHITUNGAN
# ------------------------------------------------------------------------------
# Best Practice: Gunakan variabel 'pi' yang sudah dideklarasikan di atas,
# bukan menuliskan angka 3.14 secara berulang (hardcode).
#
# Kita dapat menuliskan kuadrat dalam dua cara:
# Cara A: luas = pi * jari_jari * jari_jari
# Cara B: luas = pi * (jari_jari ** 2)  -> menggunakan operator eksponen (**)
luas = pi * (jari_jari ** 2)

# ------------------------------------------------------------------------------
# TAHAP 3: MENAMPILKAN OUTPUT
# ------------------------------------------------------------------------------
print("=== PROGRAM MENGHITUNG LUAS LINGKARAN ===")
print(f"Jari-jari (r) = {jari_jari} cm")
print(f"Nilai Pi      = {pi}")
print("-----------------------------------------")
print(f"Rumus         : Luas = pi * r^2")
print(f"Hasil Luas    : {luas} cm^2")
print("=========================================")