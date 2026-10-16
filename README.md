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
   ```

---
*Dibuat untuk materi asistensi praktikum Algoritma & Pemrograman (ALPRO).*
