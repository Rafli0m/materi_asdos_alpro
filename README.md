# Materi Praktikum Algoritma & Pemrograman (ALPRO)

Repository ini berisi kode sumber modul praktikum dan penyelesaian tugas/challenge untuk mata kuliah **Algoritma dan Pemrograman (ALPRO)**. Seluruh kode telah dirapikan, ditata sesuai alur berpikir komputasional (**Input -> Proses -> Output**), serta dilengkapi komentar edukatif baris-per-baris agar mudah dipelajari oleh praktikan pemula.

---

## 📚 Struktur Materi

### 🔹 [PERTEMUAN 2: Variabel, Tipe Data, & Aritmatika Dasar](./PERTEMUAN%202/)
- `main.py`: Pengenalan 4 tipe data dasar Python (`str`, `int`, `float`, `bool`), fungsi `print()`, pengecekan tipe dengan `type()`, dan format modern f-string.
- `aritmatika.py`: Implementasi 7 operator aritmatika (`+`, `-`, `*`, `/`, `//`, `%`, `**`) beserta penjelasannya.
- `luaspersegi.py`: Pola dasar algoritma (Input, Proses rumus, Output) pada bangun datar persegi panjang.
- `luaslingkaran.py`: Penggunaan variabel konstanta `pi`, operator eksponen (`**`), dan penamaan variabel deskriptif.

### 🔹 [PERTEMUAN 3: Operator Logika, Perbandingan, & Percabangan](./PERTEMUAN%203/)
- `oprator_perbandingan.py`: Evaluasi perbandingan numerik (`>`, `<`, `==`, `>=`, `<=`, `!=`) serta penjelasan tipe data string vs numerik pada input.
- `oprator_logika.py`: Penggunaan dan tabel logika untuk operator `and`, `or`, dan `not`.
- `percabangan.py`: Struktur kontrol keputusan bertingkat (`if - elif - else`) dan konsep penting indentasi Python.
- `kalkulator.py`: Aplikasi kalkulator sederhana interaktif dengan validasi pembagian nol.
- `c.py`: Implementasi solusi untuk studi kasus [challens.pdf](./PERTEMUAN%203/challens.pdf) (menghitung luas lingkaran, segitiga, dan persegi panjang).

### 🔹 [Pertemuan 4: Perulangan (While Loop) & Studi Kasus](./Pertemuan%204/)
- `main.py`: Anatomi perulangan `while` (inisialisasi, kondisi, increment) untuk mencetak pola bintang segitiga beserta tabel penelusuran (*trace table*).
- `kalkulator.py`: Kalkulator berulang menggunakan konstruksi `while True` dan instruksi `break`.
- `challenge_keliling.py`: Solusi resmi studi kasus [challengs.pdf](./Pertemuan%204/challengs.pdf) (menghitung keliling persegi dan persegi panjang secara interaktif).

### 🔹 [Pertemuan 5: Fungsi (Function), Parameter, Return, & Studi Kasus](./Pertemuan%205/)
- `fungsi.py`: Pengenalan fungsi dasar tanpa parameter (`def`), blok kode, aturan indentasi, dan konsep *reusability*.
- `fungsi_dengan_parameter.py`: Fungsi berparameter dinamis, perbedaan mendasar parameter vs argumen, serta contoh multi-parameter.
- `fungsi_dengan_return.py`: Konsep nilai kembalian (`return`) vs `print()`, menampung hasil ke variabel, dan operasi lanjutan.
- `if_dalam_fungsi.py`: Integrasi struktur percabangan (`if - elif - else`) di dalam fungsi, evaluasi kondisi bertingkat, dan perbaikan logika kelulusan.
- `challenge.py`: Solusi resmi studi kasus [challenge.pdf](./Pertemuan%205/challenge.pdf) (menghitung total biaya bensin SPBU menggunakan fungsi dengan return).
- `soal/`: Kumpulan 60 berkas Python mandiri terpisah ([`soal_01.py`](./Pertemuan%205/soal/soal_01.py) s.d. [`soal_60.py`](./Pertemuan%205/soal/soal_60.py)) yang mencakup materi aritmatika dasar, percabangan `if-else`, perulangan `while`, fungsi prosedural, dan fungsi return value, disertai modul pembahasan di [PANDUAN_DAN_PEMBAHASAN_SOAL.md](./Pertemuan%205/soal/PANDUAN_DAN_PEMBAHASAN_SOAL.md).

---

## 🚀 Cara Menjalankan Program

Pastikan Anda telah menginstal **Python 3.x** di komputer Anda.

1. Clone repositori ini:
   ```bash
   git clone https://github.com/Rafli0m/materi_asdos_alpro.git
   ```
2. Masuk ke direktori repositori:
   ```bash
   cd materi_asdos_alpro
   ```
3. Jalankan file Python yang diinginkan, contoh:
   ```bash
   python "PERTEMUAN 2/main.py"
   python "PERTEMUAN 3/kalkulator.py"
   python "Pertemuan 4/challenge_keliling.py"
   python "Pertemuan 5/fungsi.py"
   python "Pertemuan 5/challenge.py"
   python "Pertemuan 5/soal/soal_01.py"
   ```

---
*Dibuat untuk materi asistensi praktikum Algoritma & Pemrograman (ALPRO).*
