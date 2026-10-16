# ==============================================================================
# PERTEMUAN 2: PENGENALAN VARIABEL & TIPE DATA DASAR DI PYTHON
# ==============================================================================
# Variabel adalah "wadah" di dalam memori komputer yang digunakan untuk 
# menyimpan nilai/data. Di Python, kita tidak perlu mendeklarasikan tipe data 
# secara manual (Python otomatis mendeteksi tipe datanya - dinamik typing).
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. DEKLARASI VARIABEL DENGAN BERBAGAI TIPE DATA
# ------------------------------------------------------------------------------

# Tipe data String (str): Digunakan untuk teks/karakter, diapit tanda petik (" atau ')
nama = "Rafli Maulana"

# Tipe data Integer (int): Digunakan untuk bilangan bulat (positif, nol, atau negatif)
npm = 5230411091
smester = 7

# Tipe data Float (float): Digunakan untuk bilangan desimal/pecahan (menggunakan titik '.')
target_ipk = 3.9

# Tipe data Boolean (bool): Hanya bernilai True (Benar) atau False (Salah)
# Huruf pertama harus kapital (True / False)
status_mahasiswa = True


# ------------------------------------------------------------------------------
# 2. MENAMPILKAN OUTPUT MENGGUNAKAN print()
# ------------------------------------------------------------------------------
print("=== MENAMPILKAN NILAI VARIABEL (CARA BIASA) ===")
print("Halo semuanya")
print(nama)
print(npm)
print(smester)
print(target_ipk)
print(status_mahasiswa)

print("\n" + "="*50 + "\n")

# ------------------------------------------------------------------------------
# 3. TIPS PRAKTIS: MENGGUNAKAN F-STRING AGAR OUTPUT LEBIH RAPI & INFORMATIF
# ------------------------------------------------------------------------------
# F-string (formatted string literals) diawali huruf 'f' sebelum tanda petik.
# Kita bisa menyisipkan variabel langsung di dalam kurung kurawal {nama_variabel}.
print("=== MENAMPILKAN INFORMASI DENGAN F-STRING ===")
print(f"Nama Lengkap     : {nama} (Tipe data: {type(nama).__name__})")
print(f"NPM              : {npm} (Tipe data: {type(npm).__name__})")
print(f"Semester Saat Ini: {smester} (Tipe data: {type(smester).__name__})")
print(f"Target IPK       : {target_ipk} (Tipe data: {type(target_ipk).__name__})")
print(f"Mahasiswa Aktif? : {status_mahasiswa} (Tipe data: {type(status_mahasiswa).__name__})")