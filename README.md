# LuckyZip
LuckyZip adalah alat sederhana berbasis Python yang dirancang khusus untuk membuka kunci pada berkas ZIP yang terkunci. Alat ini menggunakan metode dictionary, yaitu dengan mengandalkan wordlist sebagai kumpulan kata sandi yang telah disiapkan sebelumnya. Dengan bantuan wordlist, LuckyZip mencoba berbagai kombinasi kata sandi secara sistematis untuk membuka kunci berkas ZIP yang terlindungi.


## Fitur
- Buka Kunci Tanpa Repot: Gunakan Wordlist favoritmu untuk membuka berkas ZIP dengan cepat.
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
python lucky-zip.py -f [lokasi/berkas_zip] -w [lokasi/daftar_kata_sandi]

```
Ganti `[lokasi/berkas_zip]` dengan lokasi berkas ZIP Anda dan `[lokasi/daftar_kata_sandi]` dengan lokasi wordlist yang ingin digunakan.
