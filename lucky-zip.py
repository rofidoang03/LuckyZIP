import zipfile
import sys
from tqdm import tqdm
import time
import pyfiglet

def display_banner():
    banner = pyfiglet.figlet_format("LuckyZip", font="standard")
    colored_banner = f"\033[1;96m{banner}\033[0m"  # Blue color ANSI escape codes
    print(colored_banner)

def crack_zip(zip_file, wordlist, start_time):
    try:
        with open(wordlist, 'r', encoding='latin-1', errors='ignore') as wordlist_file:
            passwords = wordlist_file.readlines()
    except FileNotFoundError:
        print(f"Error: Wordlist '{wordlist}' not found.")
        return False
    except UnicodeDecodeError:
        print("Error: Unable to read file with Latin-1 encoding.")
        return False
        
    found_password = None
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            for password in tqdm(passwords, desc="Cracking zip file", unit="password"):
                password = password.strip()  # Removing whitespace characters like \n
                
                try:
                    zip_ref.extractall(pwd=password.encode())
                    found_password = password
                    break
                except Exception as e:
                    # Incorrect password, move on to the next password
                    continue
    except FileNotFoundError:
        print(f"Error: Zip file '{zip_file}' not found.")
        return False
    
    end_time = time.time()
    duration = end_time - start_time
    if found_password:
        print(f"\nPassword found: {found_password}")
    else:
        print("\nPassword not found.")
    print(f"\nStart Time: {time.strftime('%H:%M:%S', time.localtime(start_time))}")
    print(f"End Time: {time.strftime('%H:%M:%S', time.localtime(end_time))}")
    print(f"Duration: {duration:.2f} seconds")

def main():
    display_banner()
    print("ZIP Password Cracker")
    print("This tool can be found at: <https://github.com/rofidoang03/LuckyZip>\n")
    if len(sys.argv) != 5 or sys.argv[1] != '-f' or sys.argv[3] != '-w':
        print("Usage: python script.py -f [zip_file] -w [wordlist]")
        return
    
    zip_file = sys.argv[2]
    wordlist = sys.argv[4]
    
    start_time = time.time()
    crack_zip(zip_file, wordlist, start_time)

if __name__ == '__main__':
    main()
