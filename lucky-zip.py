import zipfile
import sys
from tqdm import tqdm
import time
import pyfiglet

def display_banner():
    banner = pyfiglet.figlet_format("LuckyZip", font="standard")
    colored_banner = f"\033[1;96m{banner}\033[0m"  # Kode escape warna biru ANSI
    print(colored_banner)

def crack_zip(zip_file, wordlist, start_time):
    try:
        with open(wordlist, 'r', encoding='latin-1', errors='ignore') as wordlist_file:
            passwords = wordlist_file.readlines()
    except FileNotFoundError:
        print(f"Error: Wordlist '{wordlist}' tidak ditemukan.")
        return False
    except UnicodeDecodeError:
        print("Error: Tidak dapat membaca file dengan encoding Latin-1.")
        return False
        
    found_password = None
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            for password in tqdm(passwords, desc="Mencoba membuka file zip", unit="kata sandi"):
                password = password.strip()  # Menghapus karakter spasi seperti \n
                
                try:
                    zip_ref.extractall(pwd=password.encode())
                    found_password = password
                    break
                except Exception as e:
                    # Kata sandi salah, lanjut ke kata sandi berikutnya
                    continue
    except FileNotFoundError:
        print(f"Error: File zip '{zip_file}' tidak ditemukan.")
        return False
    
    end_time = time.time()
    duration = end_time - start_time
    if found_password:
        print(f"\nKata sandi ditemukan: {found_password}")
    else:
        print("\nKata sandi tidak ditemukan.")
    print(f"\nWaktu Mulai: {time.strftime('%H:%M:%S', time.localtime(start_time))}")
    print(f"Waktu Selesai: {time.strftime('%H:%M:%S', time.localtime(end_time))}")
    print(f"Durasi: {duration:.2f} detik")

def main():
    display_banner()
    print("Pemecah Kata Sandi File Zip")
    print("Alat ini dapat ditemukan di: <https://github.com/rofidoang03/LuckyZip>\n")
    if len(sys.argv) != 5 or sys.argv[1] != '-f' or sys.argv[3] != '-w':
        print("Penggunaan: python script.py -f [file_zip] -w [wordlist]")
        return
    
    zip_file = sys.argv[2]
    wordlist = sys.argv[4]
    
    start_time = time.time()
    crack_zip(zip_file, wordlist, start_time)

if __name__ == '__main__':
    main()
