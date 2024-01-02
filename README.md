# LuckyZip

LuckyZip adalah perangkat lunak sederhana yang dikembangkan dengan menggunakan bahasa pemrograman Python. Fungsinya secara khusus dirancang untuk melakukan ekstraksi pada file zip yang dilindungi dengan kata sandi. Alat ini menggunakan metode serangan kamus, di mana pendekatannya mengandalkan sebuah daftar kata sandi sebagai sumber kombinasi.

Dalam operasinya, LuckyZip secara berurutan mencoba setiap kata sandi dari daftar kata-kata yang telah tersedia. Proses ini dilakukan secara sistematis untuk membuka file zip yang dilindungi oleh kata sandi. Pendekatan ini memungkinkan LuckyZip untuk menguji ribuan bahkan jutaan kombinasi kata sandi dengan tujuan membuka file zip yang terkunci.

## Fitur

- **Memecahkan kata sandi tanpa repot:** Gunakan Wordlist favoritmu untuk memecahkan kata sandi file ZIP dengan cepat.
- **Lihat Progresnya:** Pantau prosesnya dengan jelas menggunakan tqdm.

- **Mendukung banyak sistem operasi:** Contohnya Android, Linux (berbasis Debian/Ubuntu) dan Windows
  
## Instalasi

Pastikan Anda memiliki Python yang terinstal. Untuk memulai, ikuti langkah-langkah berikut:

```bash
# klon repositori
$ git clone https://github.com/rofidoang03/LuckyZip.git

# pindah ke direktori luckyzip
$ cd LuckyZip

# install dependensi
$ pip3 install -r requirements.txt
```

## Penggunaan

```
python lucky-zip.py -f [lokasi/file_zip] -w [lokasi/wordlist]
```
Ganti `[lokasi/file_zip]` dengan lokasi file ZIP Anda dan `[lokasi/wordlist]` dengan lokasi wordlist yang ingin digunakan.

## Kontribusi dan Dukungan

- **Berpartisipasi:** Kami mengundang kontribusi! Silakan fork repositori ini, lakukan perubahan, dan ajukan pull request.
- **Laporkan Masalah:** Jika ada masalah atau saran, silakan buat isu di GitHub

## Etika dan Hukum

Gunakan LuckyZip dengan bertanggung jawab dan hanya untuk membuka file zip yang Anda memiliki izinnya. Penggunaan yang tidak etis tidak dianjurkan dan dapat memiliki konsekuensi hukum.
