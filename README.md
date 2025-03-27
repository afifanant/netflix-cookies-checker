

# 🎬 **Netflix Cookies Checker**  

Selamat datang di **Netflix Cookies Checker** — aplikasi berbasis Flask yang memungkinkan Anda memvalidasi file cookie bergaya Netscape untuk menguji akses ke akun Netflix dengan cepat dan akurat.  

---  

## ✨ **Fitur Unggulan**  

✔️ **Validasi Cookie Cepat** – Unggah beberapa file cookie untuk menguji apakah dapat digunakan untuk login ke Netflix.  
✔️ **Antarmuka Modern & Intuitif** – Dirancang dengan UI yang bersih dan ramah pengguna.  
✔️ **Hasil Real-Time** – Dapatkan hasil validasi secara instan dengan indikator keberhasilan yang jelas.  

---  

## 📸 **Tampilan Antarmuka**  

Cuplikan layar dari aplikasi:  

### 🏠 **Halaman Utama**  
![Halaman Utama](https://raw.githubusercontent.com/afifanant/netflix-cookies-checker/main/ss-1.png)  

### ✅ **Hasil Validasi**  
![Hasil Validasi](https://raw.githubusercontent.com/afifanant/netflix-cookies-checker/main/ss-2.png)  


---  

## 🚀 **Prasyarat**  

Sebelum memulai, pastikan sistem Anda telah terinstal perangkat lunak berikut:  

- **Python 3.x**  
- **Flask**  
- **Requests**  

---  

## 🔧 **Instalasi**  

Ikuti langkah-langkah berikut untuk menyiapkan proyek di mesin lokal Anda:  

### 1. **Klon repositori**  
```bash
git clone https://github.com/afifanant/netflix-cookies-checker.git
cd netflix-cookies-checker
```  

### 2. **Buat lingkungan virtual**  
```bash
python -m venv venv
source venv/bin/activate   # Untuk Windows: venv\Scripts\activate
```  

### 3. **Instal dependensi**  
```bash
pip install -r requirements.txt
```  

---  

## 🏃 **Cara Menjalankan**  

1. **Jalankan aplikasi Flask:**  
```bash
python app.py
```  

2. **Akses aplikasi:**  
Buka browser dan masukkan: [`http://localhost:8080`](http://localhost:8080)  

3. **Unggah File Cookie:**  
Gunakan antarmuka untuk mengunggah file cookie dan lihat status validasinya secara real-time.  

4. **Demo Online:**  
Coba aplikasi secara langsung di: [Netflix Cookie Checker Online](https://afifanant.pythonanywhere.com)  

---  

## ⚙️ **Bagaimana Cara Kerjanya?**  

1. **Parsing Cookie**  
   - Aplikasi membaca file cookie dalam format Netscape dan menyimpannya ke dalam `RequestsCookieJar`.  

2. **Validasi Login**  
   - Cookie yang diunggah digunakan untuk mengakses halaman Netflix dan mengonfirmasi status login berdasarkan respons dari server Netflix.  

3. **Tampilan Hasil**  
   - Status validasi akan ditampilkan dengan jelas, termasuk pesan kesalahan jika login gagal.  

---  

## 🤝 **Kontribusi**  

💡 Kami selalu menyambut kontribusi dari komunitas!  
- Jika Anda menemukan bug atau memiliki ide perbaikan, silakan buka *issue* atau kirimkan *pull request*.  
- Pastikan untuk mengikuti pedoman kontribusi sebelum mengirimkan perubahan.  

---  

## 📄 **Lisensi**  

Proyek ini dilisensikan di bawah **Lisensi MIT**. Lihat [LICENSE](LICENSE) untuk detail selengkapnya.  

---  

## 👨‍💻 **Pengembang**  

Dikembangkan oleh **Afif Ananta**.  
Jika Anda memiliki pertanyaan atau masalah, jangan ragu untuk menghubungi saya melalui GitHub atau email.  

---  

💼 **Netflix Cookie Checker** — Solusi cepat dan efektif untuk memvalidasi cookie Netflix Anda. 🚀  

---

### 🔥 **Instal sekarang dan mulai uji cookie Netflix Anda dengan mudah!**  

---
