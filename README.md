# LuckyZIP 

LuckyZIP adalah perangkat lunak sederhana yang dikembangkan dengan menggunakan bahasa pemrograman Python. Fungsinya secara khusus dirancang untuk melakukan ekstraksi pada file zip yang dilindungi kata sandi. Alat ini menggunakan metode serangan kamus, di mana pendekatannya mengandalkan sebuah daftar kata sandi sebagai sumber kombinasi.

Dalam operasinya, LuckyZIP secara berurutan mencoba setiap kata sandi dari daftar kata-kata yang telah tersedia. Proses ini dilakukan secara sistematis untuk membuka file zip yang dilindungi oleh kata sandi. Pendekatan ini memungkinkan LuckyZIP untuk menguji ribuan bahkan jutaan kombinasi kata sandi dengan tujuan membuka file zip yang terkunci.

# Fitur

- Buka kunci file ZIP dengan cepat menggunakan Wordlist favorit Anda
- Memantau kemajuannya secara terperinci dengan tqdm. 
- Kompatibel dengan berbagai sistem operasi, termasuk Android (Termux) dan Linux (berbasis Debian/Ubuntu).
- mendukung dua mode, yaitu CLI (Command Line Interface) dan GUI (Graphical User Interface).

# Instalasi

## Android

> Untuk sistem operasi Android hanya dapat menjalankan mode CLI (Command Line Interface).

Salin dan tempelkan perintah berikut
  
```bash
pkg update -y ; pkg upgrade -y ; pkg install git -y ; pkg install python3 -y ; git clone https://github.com/rofidoang03/LuckyZIP ; cd LuckyZIP ; bash instal.sh
```

## Linux

> Pastikan Anda telah masuk ke dalam mode root
  
Salin dan tempelkan perintah berikut

```
apt-get update -y ; apt-get upgrade -y ; apt-get install git -y ; apt-get install python3-pip -y ; git clone https://github.com/rofidoang03/LuckyZIP ; cd LuckyZIP ; bash instal.sh
```

# Penggunaan

## CLI

```
python lucky-zip.py -f [lokasi/file_zip] -w [lokasi/wordlist]
```

Ganti `[lokasi/file_zip]` dengan lokasi file ZIP Anda dan `[lokasi/wordlist]` dengan lokasi wordlist yang ingin digunakan.

## GUI

```
lucky-zip-gui
```

# Screenshot

## Android
  
![img](https://github.com/rofidoang03/LuckyZIP/blob/main/ss_android.jpg)

## Linux

![img](https://github.com/rofidoang03/LuckyZIP/blob/main/ss_linux_1.png)

![img](https://github.com/rofidoang03/LuckyZIP/blob/main/ss_linux_2.png)

# Kontribusi dan Dukungan

**Berpartisipasi:** Kami mengundang kontribusi! Silakan fork repositori ini, lakukan perubahan, dan ajukan pull request.
  
**Laporkan Masalah:** Jika ada masalah atau saran, silakan buat isu di GitHub.
