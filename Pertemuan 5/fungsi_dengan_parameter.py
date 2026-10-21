# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# TOPIK: Fungsi dengan Parameter
# ==============================================================================

"""
PENJELASAN UNTUK MAHASISWA:
1. PARAMETER adalah variabel yang ditulis di dalam tanda kurung saat fungsi dibuat (sebagai wadah input).
2. ARGUMEN adalah nilai nyata yang dikirimkan ke dalam fungsi saat fungsi dipanggil.
3. Dengan parameter, hasil output fungsi dapat berubah-ubah (dinamis) sesuai nilai yang kita masukkan.
"""

# ------------------------------------------------------------------------------
# 1. KODE UTAMA: Fungsi halo dengan 1 Parameter (nama)
# ------------------------------------------------------------------------------

# 'nama' di sini adalah parameter
def halo(nama):
    print("Halo semua, saya", nama)

# Memanggil fungsi dengan mengirim argumen "Rafli"
halo("Rafli")

# Kita juga bisa memanggil fungsi yang sama dengan argumen lain
halo("Budi")
halo("Siti")


# ------------------------------------------------------------------------------
# 2. CONTOH LAIN 1: Fungsi dengan 2 Parameter (Perkenalan Diri)
# ------------------------------------------------------------------------------

def perkenalan(nama, asal):
    print("Halo, nama saya", nama, "dan saya berasal dari", asal)

# Memanggil fungsi dengan 2 argumen
perkenalan("Rafli", "Jambi")
perkenalan("Andi", "Yogyakarta")


# ------------------------------------------------------------------------------
# 3. CONTOH LAIN 2: Fungsi Perhitungan Sederhana (Penjumlahan)
# ------------------------------------------------------------------------------

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print("Hasil penjumlahan:", angka1, "+", angka2, "=", hasil)

# Memanggil fungsi tambah
tambah(10, 5)
tambah(25, 75)
