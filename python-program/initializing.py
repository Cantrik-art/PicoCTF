import random
import sys
import time
import os
import pyfiglet

# Fungsi untuk menampilkan teks dengan efek ketikan
def typing_effect(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Mengubah warna latar belakang dan teks
def hacker_terminal():
    # Set warna latar belakang hitam dan teks hijau
    print("\033[0;30;42m")  # Background hitam, teks hijau
    typing_effect("Initializing picoCTF Playlist")
    time.sleep(2)  # Delay setelah pesan pertama

    typing_effect("Connecting to picoCTF Server...")
    time.sleep(2)

    typing_effect("Access Granted")
    time.sleep(1)

    typing_effect("Loading Challenges...")
    
    # Efek loading dengan titik
    for _ in range(3):
        typing_effect(".", 0.5)

    # Menampilkan teks besar "hacker terminal"
    ascii_banner = pyfiglet.figlet_format("Cantrik Art")
    print("\033[92m" + ascii_banner)  # Teks hijau besar

    # Efek huruf acak jatuh seperti Matrix
    typing_effect("Starting To picoCTF...")
    time.sleep(1)
    matrix_effect()

# Membuat efek huruf acak yang jatuh seperti di Matrix
def matrix_effect():
    columns = os.get_terminal_size().columns
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    # Membuat efek huruf acak yang jatuh seperti di Matrix
    for _ in range(100):  # Batasi untuk menghentikan setelah 100 baris
        sys.stdout.write("\033[0;30;42m")  # Hijau dengan latar belakang hitam
        for _ in range(columns):
            sys.stdout.write(random.choice(chars))
        sys.stdout.write("\n")
        sys.stdout.flush()
        time.sleep(0.05)

# Mulai efek terminal hacker
hacker_terminal()
