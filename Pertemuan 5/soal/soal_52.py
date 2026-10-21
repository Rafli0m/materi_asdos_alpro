# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 52: Cetak Rincian Transaksi Pulsa
# ==============================================================================

"""
CERITA SOAL:
Konter pulsa membutuhkan fungsi untuk mencetak ringkasan transaksi setelah pembeli memilih nominal pulsa.
"""

# 1. Buat fungsi dengan parameter cetak_transaksi(nomor_hp, nominal)
# 2. Fungsi menerima 2 parameter: nomor_hp (string) dan nominal (integer), tanpa return
def cetak_transaksi(nomor_hp: str, nominal: int):
    # 3. Tampilkan format rincian nomor tujuan dan nominal pulsa ke layar
    print("------ RINCIAN TRANSAKSI PULSA ------")
    print(f"Nomor Tujuan  : {nomor_hp}")
    print(f"Nominal Pulsa : Rp{nominal:,}")
    print("Status        : BERHASIL")
    print("-------------------------------------")

# Contoh pemanggilan fungsi
cetak_transaksi("081234567890", 50000)

