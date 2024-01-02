# LuckyZip

LuckyZip merupakan sebuah perangkat lunak sederhana yang dikembangkan menggunakan bahasa pemrograman Python. Fungsinya secara spesifik adalah untuk melakukan ekstraksi pada file zip yang dilindungi oleh kata sandi. Alat ini menggunakan metode yang dikenal sebagai metode dictionary attack, di mana pendekatannya adalah dengan memanfaatkan sebuah daftar kata sandi (wordlist) sebagai kumpulan kata sandi potensial.

Dalam prosesnya, LuckyZip mengambil setiap kata sandi dari daftar kata-kata yang telah disiapkan, dan secara berurutan mencoba setiap kombinasi kata sandi secara sistematis untuk mengekstrak file zip yang dilindungi oleh kata sandi tersebut. Pendekatan ini memungkinkan alat ini untuk mencoba ribuan, bahkan jutaan kombinasi kata sandi dalam upaya untuk mengekstrak file zip yang terkunci.

## Fitur

- **Memecahkan kata sandi tanpa repot:** Gunakan Wordlist favoritmu untuk memecahkan kata sandi file ZIP dengan cepat.
- **Lihat Progresnya:** Pantau prosesnya dengan jelas menggunakan tqdm.

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
