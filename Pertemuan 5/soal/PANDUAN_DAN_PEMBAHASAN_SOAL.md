# PANDUAN PRAKTIKUM & KUNCI JAWABAN LENGKAP
## ALGORITMA DAN PEMROGRAMAN - PERTEMUAN 5 (FUNGSI & LOGIKA)

---

## 📚 DAFTAR ISI & STRUKTUR FILE
1. [Struktur File Proyek](#struktur-file-proyek)
2. [Ringkasan Materi Pertemuan 5](#ringkasan-materi-pertemuan-5)
   - Fungsi Dasar (`fungsi.py`)
   - Fungsi dengan Parameter (`fungsi_dengan_parameter.py`)
   - Fungsi dengan Return Value (`fungsi_dengan_return.py`)
   - Logika Percabangan dalam Fungsi (`if_dalam_fungsi.py`)
3. [Pembahasan Challenge SPBU](#pembahasan-challenge-spbu)
4. [Kunci Jawaban & Pembahasan 60 Soal Praktikum](#kunci-jawaban--pembahasan-60-soal-praktikum)
   - [Modul 1: Variabel & Operator Aritmatika (Soal 1 - 15)](#modul-1-variabel--operator-aritmatika-soal-1---15)
   - [Modul 2: Struktur Percabangan If-Elif-Else (Soal 16 - 30)](#modul-2-struktur-percabangan-if-elif-else-soal-16---30)
   - [Modul 3: Perulangan While Loop (Soal 31 - 45)](#modul-3-perulangan-while-loop-soal-31---45)
   - [Modul 4: Fungsi Prosedural Tanpa Return (Soal 46 - 55)](#modul-4-fungsi-prosedural-tanpa-return-soal-46---55)
   - [Modul 5: Fungsi dengan Return Value (Soal 56 - 60)](#modul-5-fungsi-dengan-return-value-soal-56---60)

---

## 📁 STRUKTUR FILE PROYEK

```text
Pertemuan 5/
│
├── fungsi.py                         # Kode materi: Fungsi dasar tanpa parameter
├── fungsi_dengan_parameter.py        # Kode materi: Parameter & argumen
├── fungsi_dengan_return.py           # Kode materi: Return value vs print()
├── if_dalam_fungsi.py                # Kode materi: Percabangan di dalam fungsi
│
├── challenge.py                      # Implementasi & Uji Soal Challenge SPBU
├── challenge.pdf                     # Dokumen soal challenge
│
└── soal/
    ├── soal.pdf                      # Dokumen 60 soal latihan
    ├── soal_01.py                    # Soal 1: Luas Petak Kebun
    ├── soal_02.py                    # Soal 2: Keliling Meja Belajar
    ├── soal_03.py                    # Soal 3: Pembagian Permen
    │   ...                           # (Setiap soal memiliki file mandiri terpisah)
    ├── soal_59.py                    # Soal 59: Penentuan Status Kelulusan Nilai
    ├── soal_60.py                    # Soal 60: Hitung Biaya Sewa Lapangan Futsal
    └── PANDUAN_DAN_PEMBAHASAN_SOAL.md# Panduan belajar & kunci jawaban ini
```

---

## 💡 RINGKASAN MATERI PERTEMUAN 5

### 1. Fungsi Dasar (`fungsi.py`)
- **Definisi:** Fungsi dibuat dengan kata kunci `def`, diikuti nama fungsi, kurung `()`, dan titik dua `:`.
- **Aturan:** Kode di dalam fungsi harus memiliki indentasi (menjorok ke dalam).
- **Pemanggilan:** Fungsi baru akan dijalankan saat dipanggil dengan tanda kurung `nama_fungsi()`.

### 2. Fungsi dengan Parameter (`fungsi_dengan_parameter.py`)
- **Parameter:** Variabel penampung yang ditulis di tanda kurung fungsi saat pembuatan.
- **Argumen:** Nilai nyata yang dimasukkan saat fungsi dipanggil.
- **Tipe Argumen:** Positional Arguments (berurutan) dan Keyword Arguments (menyebutkan nama parameter).
- **Default Parameter:** Memberikan nilai awal pada parameter jika pemanggil tidak mengisinya.

### 3. Fungsi dengan Return Value (`fungsi_dengan_return.py`)
- **Perbedaan `return` vs `print()`:**
  - `print()` hanya menampilkan karakter ke layar terminal; nilainya tidak bisa disimpan atau dihitung lagi.
  - `return` mengembalikan nilai ke baris pemanggil, sehingga bisa disimpan ke variabel atau dijadikan input bagi fungsi lain.

### 4. Logika Percabangan di dalam Fungsi (`if_dalam_fungsi.py`)
- **Catatan Edukatif:** Mahasiswa sering keliru membuat kondisi batas. Contoh: jika cumlaude dicek `lamalulus >= 7`, maka mahasiswa semester 11 juga akan bernilai True. Batasan yang tepat secara logika adalah `lamalulus <= 8`.
- Menempatkan `if-elif-else` di dalam fungsi membuat fungsi cerdas dan mampu mengambil keputusan sesuai parameter yang diterima.

---

## ⛽ PEMBAHASAN CHALLENGE SPBU (`challenge.py`)

### Spesifikasi:
1. Nama fungsi: `hitung_biaya_bensin(jumlah_liter, harga_per_liter)`
2. Menerima dua parameter bertipe integer: `jumlah_liter` dan `harga_per_liter`.
3. Menghitung total biaya: `jumlah_liter * harga_per_liter`.
4. Mengembalikan (`return`) total biaya.

### Solusi Kode:
```python
def hitung_biaya_bensin(jumlah_liter: int, harga_per_liter: int) -> int:
    total_biaya = jumlah_liter * harga_per_liter
    return total_biaya
```

---

## 📝 KUNCI JAWABAN & PEMBAHASAN 60 SOAL

### MODUL 1: Variabel & Operator Aritmatika (Soal 1 - 15)
- **Soal 1 (Luas Kebun):** `sisi = 12`, `luas = sisi * sisi` -> Luas = 144 m².
- **Soal 2 (Keliling Meja):** `panjang = 120`, `lebar = 60`, `keliling = 2 * (panjang + lebar)` -> Keliling = 360 cm.
- **Soal 3 (Pembagian Permen):** `total_permen = 25`, `jumlah_anak = 4`. Gunakan `//` untuk pembagian bulat (6) dan `%` untuk sisa permen (1).
- **Soal 4 (Total Belanja Buku):** `jumlah_buku = 8`, `harga_satuan = 4500`, `total_bayar = 8 * 4500 = 36000`.
- **Soal 5 (Sisa Uang Saku):** `uang_saku = 150000`, `biaya_makan = 85000`, `biaya_fotokopi = 20000`, `sisa_uang = 150000 - 105000 = 45000`.
- **Soal 6 (Konversi Menit ke Jam):** `total_menit = 145`, `jam = 145 // 60 = 2`, `sisa_menit = 145 % 60 = 25`.
- **Soal 7 (Luas Layar Segitiga):** `alas = 4.0`, `tinggi = 6.0`, `luas_segitiga = 0.5 * alas * tinggi = 12.0`.
- **Soal 8 (Volume Kubus):** `rusuk = 90`, `volume_kubus = rusuk ** 3 = 729000 cm³`.
- **Soal 9 (Pembagian Rata Jeruk):** `total_panen = 50.0`, `jumlah_keranjang = 4`, `berat_per_keranjang = 50.0 / 4 = 12.5 kg`.
- **Soal 10 (Konversi Hari ke Jam & Detik):** `jumlah_hari = 3`, `total_jam = 3 * 24 = 72`, `total_detik = 72 * 3600 = 259200`.
- **Soal 11 (Potongan Diskon):** `harga_kaos = 120000`, `persen_diskon = 0.15`, `potongan_harga = 18000.0`.
- **Soal 12 (Iuran Listrik Kos):** `total_tagihan = 360000`, `jumlah_penghuni = 5`, `tagihan_per_orang = 360000 // 5 = 72000`.
- **Soal 13 (Volume Kotak Sepatu):** `panjang = 30`, `lebar = 18`, `tinggi = 12`, `volume_kotak = 30 * 18 * 12 = 6480 cm³`.
- **Soal 14 (Selisih Umur):** `umur_kakak = 21`, `umur_adik = 14`, `selisih_umur = 21 - 14 = 7`.
- **Soal 15 (Keliling Lingkaran):** `jari_jari = 14.0`, `pi = 3.14`, `keliling_roda = 2 * pi * jari_jari = 87.92 cm`.

---

### MODUL 2: Struktur Percabangan If-Elif-Else (Soal 16 - 30)
- **Soal 16 (Usia KTP):** `if usia >= 17:` berhak KTP, `else:` belum mencukupi.
- **Soal 17 (Ganjil/Genap):** `if bilangan % 2 == 0:` genap, `else:` ganjil.
- **Soal 18 (Ambang Kelulusan Ujian):** `if nilai_ujian >= 70.0:` "Status: Lulus", `else:` "Status: Tidak Lulus".
- **Soal 19 (Tiket Wahana):** `if tinggi_badan < 120:` Rp25.000 (Anak), `else:` Rp40.000 (Dewasa).
- **Soal 20 (Diskon Belanja Supermarket):** `if total_belanja >= 100000: total_belanja -= 15000`.
- **Soal 21 (Predikat Nilai Kuliah):** `>= 85 ('A')`, `>= 70 ('B')`, `>= 55 ('C')`, `else ('D')`.
- **Soal 22 (PIN Brankas):** `if input_pin == "1234":` Akses diterima, `else:` Akses ditolak.
- **Soal 23 (Termometer Digital):** `if suhu >= 37.5:` suhu tubuh tinggi, `else:` suhu normal.
- **Soal 24 (Jenis Bilangan):** `if angka > 0:` Positif, `elif angka < 0:` Negatif, `else:` Tepat Nol.
- **Soal 25 (Tarik Tunai ATM):** `if tarik <= saldo:` transaksi berhasil, `else:` Saldo tidak mencukupi.
- **Soal 26 (Menu Minuman):** `if pilihan == "1":` Es Kopi, `elif pilihan == "2":` Es Teh, `else:` Menu tidak tersedia.
- **Soal 27 (Kehadiran Ujian):** `if kehadiran >= 75.0:` diizinkan, `else:` dilarang.
- **Soal 28 (Gratis Ongkir Online):** `if total_belanja >= 50000 and status_member == "y":` Gratis ongkir, `else:` Normal.
- **Soal 29 (Tahun Kabisat):** `if tahun % 4 == 0:` Tahun kabisat, `else:` Bukan.
- **Soal 30 (Kalkulator Mini):** `if op == "+":` tambah, `elif op == "-":` kurang, `else:` operator tidak didukung.

---

### MODUL 3: Perulangan While Loop (Soal 31 - 45)
- **Soal 31 (Hitung Mundur):** `while hitung >= 1:` kurangi 1 tiap iterasi, akhiri dengan `"Roket Meluncur!"`.
- **Soal 32 (Kelipatan 4):** `angka = 4; while angka <= 40: print(angka); angka += 4`.
- **Soal 33 (Tabungan Celengan):** `hari = 1; total = 0; while hari <= 7: total += 5000; hari += 1`.
- **Soal 34 (Tebak Angka Rahasia):** `while True: if tebakan == 7: break`.
- **Soal 35 (Percobaan PIN):** `while percobaan <= 3: if pin == "9999": break; if percobaan == 3: print("Kartu diblokir")`.
- **Soal 36 (Kasir Belanja):** `while True: if harga == 0: break; total_belanja += harga`.
- **Soal 37 (Bilangan Ganjil Maju):** `bilangan = 1; while bilangan < 20: print(bilangan); bilangan += 2`.
- **Soal 38 (Target Donasi):** `while dana_terkumpul < 100000: dana_terkumpul += donasi`.
- **Soal 39 (Konfirmasi Perkalian):** `while True: hitung; konfirm = input(); if konfirm == 'n': break`.
- **Soal 40 (Pengurangan Stok Beras):** `while stok_beras > 0: stok_beras -= 3; if stok_beras == 0: print("Stok beras habis")`.
- **Soal 41 (Pengisian Galon):** `while isi_air < 19: isi_air += 2; detik += 1; if isi_air >= 19: print("Galon penuh")`.
- **Soal 42 (Pencatat Data Umur):** `while True: if umur == -1: break; jumlah_orang += 1`.
- **Soal 43 (Kelipatan Pangkat Dua):** `while nilai < 100: print(nilai); nilai *= 2`.
- **Soal 44 (Layanan Bank Mandiri):** `while True: if pilihan == "3": break`.
- **Soal 45 (Cetak Karakter Pagar):** `while baris <= jumlah_baris: print("#"); baris += 1`.

---

### MODUL 4: Fungsi Prosedural Tanpa Return (Soal 46 - 55)
- **Soal 46:** `tampilkan_header_kafe()` -> Mencetak nama & alamat Kopi Senja.
- **Soal 47:** `peringatan_baterai()` -> Mencetak teks peringatan baterai kritis.
- **Soal 48:** `tata_tertib_lab()` -> Mencetak 3 poin aturan lab komputer.
- **Soal 49:** `salam_perpisahan()` -> Mencetak terima kasih & informasi versi aplikasi.
- **Soal 50:** `cetak_garis()` -> Mencetak `*` sebanyak 30 kali (`"*" * 30`).
- **Soal 51:** `sapa_mahasiswa(nama)` -> Menerima string nama, mencetak sapaan portal akademik.
- **Soal 52:** `cetak_transaksi(nomor_hp, nominal)` -> Mencetak bukti transaksi pulsa.
- **Soal 53:** `ingatkan_agenda(nama_agenda, jam)` -> Mencetak pengingat rapat.
- **Soal 54:** `cetak_undangan(nama_tamu, instansi)` -> Mencetak format kartu undangan berbingkai.
- **Soal 55:** `tampilkan_skor(nama_pemain, poin)` -> Mencetak nama dan skor pemain.

---

### MODUL 5: Fungsi dengan Return Value (Soal 56 - 60)
- **Soal 56 (Konversi Celcius ke Fahrenheit):**  
  `def celcius_ke_fahrenheit(suhu_c): return (suhu_c * 1.8) + 32`
- **Soal 57 (Luas Persegi Panjang):**  
  `def hitung_luas_persegi_panjang(panjang, lebar): return panjang * lebar`
- **Soal 58 (Harga Diskon):**  
  `def hitung_harga_diskon(harga_asli, persen_diskon): return harga_asli - (harga_asli * persen_diskon)`
- **Soal 59 (Status Kelulusan):**  
  `def cek_kelulusan(nilai): return "LULUS" if nilai >= 75 else "TIDAK LULUS"`
- **Soal 60 (Sewa Lapangan Futsal):**  
  `def hitung_sewa_lapangan(durasi_jam, tarif_per_jam): return durasi_jam * tarif_per_jam`

---

## 🚀 CARA MENJALANKAN KODE DI TERMINAL

1. **Menjalankan Materi Fungsi Dasar:**
   ```bash
   python fungsi.py
   python fungsi_dengan_parameter.py
   python fungsi_dengan_return.py
   python if_dalam_fungsi.py
   ```

2. **Menjalankan Challenge SPBU:**
   ```bash
   python challenge.py
   ```

3. **Menjalankan Masing-Masing File Soal (1 s.d. 60):**
   Setiap soal kini berdiri sendiri sebagai satu file terpisah. Contoh:
   ```bash
   python soal/soal_01.py
   python soal/soal_16.py
   python soal/soal_31.py
   python soal/soal_46.py
   python soal/soal_60.py
   ```
