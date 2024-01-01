# LuckyZip
LuckyZip adalah alat sederhana berbasis Python yang dirancang khusus untuk meng-crack kata sandi file zip. Alat ini menggunakan metode dictionary, yaitu metode yang mengandalkan wordlist sebagai kumpulan kata sandi. Dengan bantuan wordlist, LuckyZip mencoba berbagai kombinasi kata sandi secara sistematis untuk meng-crack kata sandi file zip.


## Fitur
- Crack kata sandi tanpa repot: Gunakan Wordlist favoritmu untuk meng-crack file ZIP dengan cepat.
- Lihat Progresnya: Pantau prosesnya dengan jelas menggunakan tqdm.

## Instalasi
> Pastikan Anda memiliki Python yang terinstal. Untuk memulai, ikuti langkah-langkah berikut:
```
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
Ganti `[lokasi/file_zip]` dengan lokasi file ZIP Anda dan `[lokasi/daftar_wordlist]` dengan lokasi wordlist yang ingin digunakan.
