# ==============================================================================
# PRAKTIKUM ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5
# Soal 3: Pembagian Permen
# ==============================================================================

"""
CERITA SOAL:
Ibu membawa 25 butir permen untuk dibagikan secara adil kepada 4 orang anaknya. Ibu ingin tahu berapa permen yang didapat setiap anak dan berapa butir sisa permen yang tidak terbagi.
"""

# 1. Buat variabel total_permen bernilai 25 dan jumlah_anak bernilai 4
total_permen = 25
jumlah_anak = 4

# 2. Hitung permen per anak menggunakan pembagian bulat (//) ke dalam variabel permen_per_anak
permen_per_anak = total_permen // jumlah_anak

# 3. Hitung sisa permen menggunakan modulus (%) ke dalam variabel sisa_permen
sisa_permen = total_permen % jumlah_anak

# 4. Tampilkan nilai permen_per_anak dan sisa_permen ke layar
print(f"Total permen    : {total_permen} butir")
print(f"Jumlah anak     : {jumlah_anak} orang")
print(f"Permen per anak : {permen_per_anak} butir")
print(f"Sisa permen     : {sisa_permen} butir")

