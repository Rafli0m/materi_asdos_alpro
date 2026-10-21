# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 25: Validasi Penarikan Tunai ATM
# ==============================================================================

"""
CERITA SOAL:
Nasabah ingin menarik uang tunai dari ATM. Saldo rekening saat ini adalah Rp500.000. Penarikan hanya dapat diproses jika nominal yang ditarik tidak melebihi saldo.
"""

# 1. Tetapkan variabel saldo = 500000
saldo = 500000
print(f"Saldo awal Anda: Rp{saldo:,}")

# 2. Minta input nominal penarikan (int) ke dalam variabel tarik
tarik = int(input("Masukkan nominal penarikan: Rp"))

# 3. Jika tarik <= saldo, hitung sisa saldo dan tampilkan pesan transaksi berhasil beserta sisa saldo
if tarik <= saldo:
    saldo -= tarik
    print(f"Transaksi berhasil! Penarikan Rp{tarik:,} sukses.")
    print(f"Sisa saldo Anda: Rp{saldo:,}")
# 4. Jika tarik > saldo, tampilkan pesan "Saldo tidak mencukupi"
else:
    print("Saldo tidak mencukupi")

