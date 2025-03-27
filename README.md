

```markdown
# 🎬 Pemeriksa Cookies Netflix

Selamat datang di **Pemeriksa Cookies Netflix**! Ini adalah aplikasi web berbasis Flask yang memungkinkan Anda mengunggah dan memvalidasi file cookies bergaya Netscape untuk menguji akses ke akun Netflix.

## ✨ Fitur

- 🔍 **Validasi Cookies:** Unggah beberapa file cookies untuk memeriksa apakah mereka dapat digunakan untuk login ke Netflix.
- ⚡ **Antarmuka Mudah Digunakan:** Antarmuka web yang sederhana dan intuitif.
- 📊 **Hasil Instan:** Dapatkan hasil validasi dengan cepat dan mudah.

## 🚀 Prasyarat

Pastikan Anda memiliki perangkat lunak berikut terpasang:

- Python 3.x
- Flask
- Requests

## 🔧 Instalasi

Ikuti langkah-langkah berikut untuk mengatur proyek ini di mesin lokal Anda:

1. **Kloning repositori ini:**

   ```bash
   git clone https://github.com/afifanant/netflix-cookies-checker.git
   cd netflix-cookies-checker
   ```

2. **Buat lingkungan virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate # Pada Windows gunakan `venv\Scripts\activate`
   ```

3. **Instal dependensi:**

   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Penggunaan

1. **Jalankan aplikasi Flask:**

   ```bash
   python app.py
   ```

2. **Akses aplikasi:**

   Buka browser Anda dan navigasikan ke `http://localhost:8080` untuk mengakses aplikasi.

3. **Unggah File Cookies:**

   Gunakan antarmuka web untuk mengunggah file cookies dan lihat hasil validasinya.

4. **Demo Online:**

   Coba aplikasi ini secara online di [Pemeriksa Cookies Netflix Online](https://afifanant.pythonanywhere.com/).

## 🛠️ Cara Kerja

- **Parsing Cookies:** Aplikasi memparsing cookies dalam format Netscape dan menyimpannya dalam `RequestsCookieJar`.
- **Validasi:** Cookies digunakan untuk mengakses halaman penelusuran Netflix dan menentukan login yang berhasil berdasarkan respons yang diterima.
- **Tampilan Hasil:** Hasil validasi ditampilkan dengan jelas, menunjukkan status login masing-masing file.

## 🤝 Kontribusi

Kami menyambut kontribusi dari siapa saja! Jika Anda memiliki saran atau perbaikan, mohon buka isu atau kirimkan pull request.

## 📄 Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat [LICENSE](LICENSE) untuk informasi lebih lanjut.

## 👨‍💻 Penulis

Dikembangkan oleh Afif Ananta.

---

Terima kasih telah menggunakan Pemeriksa Cookies Netflix! Jika Anda memiliki pertanyaan atau masalah, jangan ragu untuk menghubungi saya.
```

### Catatan:

- Pastikan untuk mengganti `nama-pengguna-anda` dengan nama pengguna GitHub Anda yang sebenarnya dalam tautan repositori.
- Anda dapat menambahkan lebih banyak emoji atau elemen gaya lain sesuai keinginan untuk membuat README lebih menarik.
- Buat file `requirements.txt` jika belum ada, dengan menjalankan `pip freeze > requirements.txt` dalam lingkungan virtual Anda.
