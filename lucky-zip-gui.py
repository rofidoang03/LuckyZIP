import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import threading
from datetime import datetime

def extract_zip():
    zip_filename = file_entry.get()
    wordlist_filename = wordlist_entry.get()

    try:
        with zipfile.ZipFile(zip_filename) as zip_ref:
            with open(wordlist_filename, 'r', encoding='latin-1', errors='ignore') as wordlist:
                passwords = wordlist.readlines()
                for password in passwords:
                    password = password.strip()
                    log_text.insert(tk.END, f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {zip_filename}, {wordlist_filename}, Mencoba mengekstrak dengan kata sandi: {password}...\n")
                    log_text.see(tk.END)
                    root.update_idletasks()
                    try:
                        zip_ref.extractall(pwd=password.encode('latin-1'))
                        result_label.config(text=f"Kata sandi ditemukan: {password}")
                        log_text.insert(tk.END, f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {zip_filename}, {wordlist_filename}, Kata sandi ditemukan: {password}\n")
                        break
                    except Exception as e:
                        pass
                else:
                    result_label.config(text="Kata sandi tidak ditemukan dalam wordlist.")
                    log_text.insert(tk.END, f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {zip_filename}, {wordlist_filename}, Kata sandi tidak ditemukan dalam wordlist.\n")
    except FileNotFoundError:
        result_label.config(text="File tidak ditemukan.")
        log_text.insert(tk.END, f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {zip_filename}, {wordlist_filename}, File tidak ditemukan.\n")
    except Exception as e:
        result_label.config(text="Terjadi kesalahan saat ekstraksi.")
        log_text.insert(tk.END, f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {zip_filename}, {wordlist_filename}, Terjadi kesalahan saat ekstraksi.\n")

def select_file():
    filename = filedialog.askopenfilename(title="Pilih file ZIP")
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filename)

def select_wordlist():
    filename = filedialog.askopenfilename(title="Pilih file wordlist")
    wordlist_entry.delete(0, tk.END)
    wordlist_entry.insert(0, filename)

def start_extraction():
    extract_thread = threading.Thread(target=extract_zip)
    extract_thread.start()

def on_closing():
    log_content = log_text.get("1.0", tk.END)
    log_filename = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.log"
    with open(log_filename, "w") as file:
        file.write(log_content)
    root.destroy()

root = tk.Tk()
root.title("LuckyZip")
app_width = 800
app_height = 400
root.resizable(False, False)
root.configure(bg='black')

main_frame = tk.Frame(root, bg='black')
main_frame.pack(expand=True)

file_label = tk.Label(main_frame, text="Pilih file ZIP:", font=("Arial", 12), fg='red', bg='black')
file_label.grid(row=0, column=0, sticky="w")

file_entry = tk.Entry(main_frame, width=60, font=("Arial", 10), fg='red', bg='black')
file_entry.grid(row=0, column=1, padx=5)

file_button = tk.Button(main_frame, text="Telusuri", command=select_file, fg='black', bg='red', font=("Arial", 10))
file_button.grid(row=0, column=2, padx=5)

wordlist_label = tk.Label(main_frame, text="Pilih file wordlist:", font=("Arial", 12), fg='red', bg='black')
wordlist_label.grid(row=1, column=0, sticky="w")

wordlist_entry = tk.Entry(main_frame, width=60, font=("Arial", 10), fg='red', bg='black')
wordlist_entry.grid(row=1, column=1, padx=5)

wordlist_button = tk.Button(main_frame, text="Telusuri", command=select_wordlist, fg='black', bg='red', font=("Arial", 10))
wordlist_button.grid(row=1, column=2, padx=5)

extract_button = tk.Button(main_frame, text="Ekstrak", command=start_extraction, bg='red', fg='black', font=("Arial", 12))
extract_button.grid(row=2, columnspan=3, pady=10)

result_label = tk.Label(main_frame, text="", font=("Arial", 14), fg='red', bg='black')
result_label.grid(row=3, columnspan=3)

log_frame = tk.Frame(main_frame, bg='black')
log_frame.grid(row=4, columnspan=3, sticky="nsew")

log_label = tk.Label(log_frame, text="Log:", font=("Arial", 12), fg='red', bg='black')
log_label.pack()

log_text = tk.Text(log_frame, height=10, width=60, font=("Arial", 10), fg='red', bg='black')
log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(log_frame, orient=tk.VERTICAL, command=log_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
log_text.config(yscrollcommand=scrollbar.set)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (app_width // 2)
y = (screen_height // 2) - (app_height // 2)
root.geometry(f"{app_width}x{app_height}+{x}+{y}")

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
