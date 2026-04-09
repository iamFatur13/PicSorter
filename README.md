# PicSorter
PicSorter adalah aplikasi desktop berbasis Python (CustomTkinter) yang dirancang untuk mempercepat proses pemilihan (culling) foto dalam jumlah besar. Dilengkapi dengan shortcut keyboard, fitur undo, dan penanganan file yang aman untuk alur kerja fotografer maupun dokumentasi industri.

# 📸 PicSorter

**PicSorter** adalah aplikasi desktop ringan yang dibangun dengan Python untuk membantu fotografer, vlogger, dan profesional industri (seperti pertambangan) dalam menyortir ribuan foto dengan cepat dan efisien.

Aplikasi ini memindahkan file secara fisik ke dalam kategori tertentu hanya dengan satu klik atau satu ketukan tombol di keyboard.

## ✨ Fitur Utama
- **Shortcut Keyboard (1-4):** Sortir foto secepat kilat tanpa klik mouse.
- **Fitur Undo (Z):** Salah tekan? Kembalikan file ke posisi semula secara instan.
- **Antarmuka Modern:** Menggunakan CustomTkinter untuk tampilan yang bersih dan gelap (Dark Mode).
- **Optimasi RAM:** Memuat pratinjau gambar secara cerdas agar tidak membebani memori meskipun menangani file resolusi tinggi (4K/Drone).
- **Standalone EXE:** Dapat dijalankan di PC mana pun tanpa perlu instalasi Python.

## ⌨️ Shortcut Keyboard
| Tombol | Aksi |
| :--- | :--- |
| `1` | Pindahkan ke folder **OK** |
| `2` | Pindahkan ke folder **LUMAYAN** |
| `3` | Pindahkan ke folder **MODERAT** |
| `4` | Pindahkan ke folder **BUANG** |
| `Z` | **Undo** (Batalkan aksi terakhir) |

## 🚀 Cara Penggunaan (Versi Script)
1. Pastikan Python 3.x sudah terinstall.
2. Install dependensi:
   
   pip install customtkinter Pillow
   
4. Jalankan Aplikasi
   
   python sorter.py

5. Cara Membuat File EXE

   pyinstaller --noconsole --onefile --add-data "LOKASI_CUSTOMTKINTER;customtkinter/" sorter.py


# 🛠️ Teknologi yang Digunakan
Python 3.10+
CustomTkinter (UI Framework)
Pillow (Image Processing)
Shutil (File Operations)


# Dibuat dengan ❤️ oleh ** iamfatur **
   
