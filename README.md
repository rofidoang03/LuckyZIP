# LuckyZIP 

LuckyZIP adalah perangkat lunak sederhana yang dikembangkan dengan menggunakan bahasa pemrograman Python. Fungsinya secara khusus dirancang untuk melakukan ekstraksi pada file zip yang dilindungi kata sandi. Alat ini menggunakan metode serangan kamus, di mana pendekatannya mengandalkan sebuah daftar kata sandi sebagai sumber kombinasi.

Dalam operasinya, LuckyZIP secara berurutan mencoba setiap kata sandi dari daftar kata-kata yang telah tersedia. Proses ini dilakukan secara sistematis untuk membuka file zip yang dilindungi oleh kata sandi. Pendekatan ini memungkinkan LuckyZIP untuk menguji ribuan bahkan jutaan kombinasi kata sandi dengan tujuan membuka file zip yang terkunci.

## Fitur

**Memecahkan kata sandi tanpa kesulitan:** Manfaatkan Wordlist favorit Anda untuk membuka kunci file ZIP dengan cepat.

**Pantau kemajuannya:** Amati prosesnya secara terperinci menggunakan tqdm.

**Kompatibel dengan beragam sistem operasi:** Seperti Android, Linux (berbasis Debian/Ubuntu), dan Windows.

**Tersedia dua mode:** CLI (Command Line Interface) dan GUI (Graphical User Interface).

## Instalasi Android

> Untuk sistem operasi Android hanya dapat menjalankan mode CLI (Command Line Interface).

Salin dan tempelkan perintah berikut

```bash
pkg update -y ; pkg upgrade -y ; pkg install git -y ; pkg install python3 -y ; git clone https://github.com/rofidoang03/LuckyZIP ; cd LuckyZIP ; bash instal.sh
```

## Penggunaan

```
python lucky-zip.py -f [lokasi/file_zip] -w [lokasi/wordlist]
```
Ganti `[lokasi/file_zip]` dengan lokasi file ZIP Anda dan `[lokasi/wordlist]` dengan lokasi wordlist yang ingin digunakan.

## Screenshot

- ## Android
  ![img](https://github.com/rofidoang03/LuckyZIP/blob/main/ss_android.jpg)

## Kontribusi dan Dukungan

- **Berpartisipasi:** Kami mengundang kontribusi! Silakan fork repositori ini, lakukan perubahan, dan ajukan pull request.
- **Laporkan Masalah:** Jika ada masalah atau saran, silakan buat isu di GitHub.
