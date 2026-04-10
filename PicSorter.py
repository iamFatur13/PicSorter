
import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image

class PhotoSorter:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Sorter Pro - Professional Edition")
        self.root.geometry("1100x850")
        
        # Grid Configuration
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Variabel Logika
        self.source_dir = ""
        self.photo_list = []
        self.current_index = 0
        self.history = []
        self.options = ["OK", "LUMAYAN", "MODERAT", "BUANG"]
        self.current_ctk_img = None
        
        self.setup_ui()
        
        # Bind Keyboard
        self.root.bind("1", lambda e: self.sort_photo("OK"))
        self.root.bind("2", lambda e: self.sort_photo("LUMAYAN"))
        self.root.bind("3", lambda e: self.sort_photo("MODERAT"))
        self.root.bind("4", lambda e: self.sort_photo("BUANG"))
        self.root.bind("<KeyRelease-z>", lambda e: self.undo_action())
        self.root.bind("<KeyRelease-Z>", lambda e: self.undo_action())

    def setup_ui(self):
        # --- 1. HEADER ---
        self.top_frame = ctk.CTkFrame(self.root, height=70)
        self.top_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=(15, 0))

        self.load_btn = ctk.CTkButton(self.top_frame, text="📁 BUKA FOLDER", 
                                     command=self.load_folder, width=150, height=40,
                                     font=("Arial", 13, "bold"))
        self.load_btn.pack(side="left", padx=15, pady=10)

        # Tombol Help di Pojok Kanan
        self.help_btn = ctk.CTkButton(self.top_frame, text="❓ HELP", width=80, 
                                     fg_color="#555", hover_color="#777",
                                     command=self.show_help)
        self.help_btn.pack(side="right", padx=15, pady=10)

        self.info_label = ctk.CTkLabel(self.top_frame, text="Pilih Folder...", 
                                      font=("Arial", 14, "bold"))
        self.info_label.pack(side="right", padx=10)

        # --- 2. DISPLAY AREA ---
        self.img_container = ctk.CTkFrame(self.root, fg_color="#121212")
        self.img_container.grid(row=1, column=0, sticky="nsew", padx=20, pady=15)
        
        self.image_display = ctk.CTkLabel(self.img_container, text="Aplikasi Siap Digunakan")
        self.image_display.pack(expand=True, fill="both")

        # --- 3. FOOTER ---
        self.filename_label = ctk.CTkLabel(self.root, text="-", font=("Consolas", 12))
        self.filename_label.grid(row=2, column=0, pady=5)

        self.control_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.control_frame.grid(row=3, column=0, pady=(0, 25))

        colors = {"OK": "#2ecc71", "LUMAYAN": "#3498db", "MODERAT": "#f1c40f", "BUANG": "#e74c3c"}
        for i, opt in enumerate(self.options, 1):
            btn = ctk.CTkButton(self.control_frame, text=f"{opt}\n(Tekan {i})", 
                                fg_color=colors[opt], font=("Arial", 14, "bold"), 
                                width=180, height=60, command=lambda o=opt: self.sort_photo(o))
            btn.grid(row=0, column=i-1, padx=10)

    def show_help(self):
        """Menampilkan jendela instruksi penggunaan."""
        help_win = ctk.CTkToplevel(self.root)
        help_win.title("Panduan Penggunaan")
        help_win.geometry("500x450")
        help_win.attributes("-topmost", True) # Agar jendela tetap di depan

        title = ctk.CTkLabel(help_win, text="Photo Sorter - Quick Guide", font=("Arial", 18, "bold"))
        title.pack(pady=20)

        instructions = (
            "🚀 CARA PENGGUNAAN:\n"
            "1. Klik 'BUKA FOLDER' untuk memilih folder foto.\n"
            "2. Gunakan tombol mouse atau shortcut angka di keyboard.\n"
            "3. Foto akan otomatis pindah ke subfolder di lokasi asli.\n\n"
            "⌨️ SHORTCUT KEYBOARD:\n"
            "• [1] : Masukkan ke folder OK\n"
            "• [2] : Masukkan ke folder LUMAYAN\n"
            "• [3] : Masukkan ke folder MODERAT\n"
            "• [4] : Masukkan ke folder BUANG\n"
            "• [Z] : Batalkan (Undo) sortir terakhir\n\n"
            "💡 TIPS:\n"
            "- Pastikan tidak ada aplikasi lain yang membuka foto.\n"
            "- Gunakan fitur Undo jika salah menekan tombol."
        )

        content = ctk.CTkLabel(help_win, text=instructions, justify="left", font=("Arial", 13))
        content.pack(padx=30, pady=10)

        close_btn = ctk.CTkButton(help_win, text="Mengerti", command=help_win.destroy)
        close_btn.pack(pady=20)

    def load_folder(self):
        selected_path = filedialog.askdirectory()
        if not selected_path: return
        self.source_dir = selected_path
        ext = (".jpg", ".jpeg", ".png", ".bmp", ".webp")
        self.photo_list = [f for f in os.listdir(selected_path) if f.lower().endswith(ext)]
        self.photo_list.sort()
        if not self.photo_list:
            messagebox.showwarning("Kosong", "Tidak ada file foto!")
            return
        self.current_index = 0
        self.history = []
        self.show_photo()

    def show_photo(self):
        if 0 <= self.current_index < len(self.photo_list):
            img_path = os.path.join(self.source_dir, self.photo_list[self.current_index])
            self.info_label.configure(text=f"FOTO: {self.current_index + 1} / {len(self.photo_list)}")
            self.filename_label.configure(text=f"📄 {self.photo_list[self.current_index]}")
            try:
                with Image.open(img_path) as img:
                    img_view = img.copy()
                    self.root.update_idletasks()
                    cw, ch = self.img_container.winfo_width()-40, self.img_container.winfo_height()-40
                    if cw < 100: cw, ch = 800, 500
                    img_view.thumbnail((cw, ch))
                    self.current_ctk_img = ctk.CTkImage(light_image=img_view, dark_image=img_view, size=(img_view.width, img_view.height))
                    self.image_display.configure(image=self.current_ctk_img, text="")
            except Exception as e:
                self.image_display.configure(image=None, text=f"Error: {e}")
        else:
            self.image_display.configure(image=None, text="SELESAI!")

    def sort_photo(self, category):
        if not self.source_dir or not self.photo_list: return
        filename = self.photo_list[self.current_index]
        src, dst = os.path.join(self.source_dir, filename), os.path.join(self.source_dir, category, filename)
        self.image_display.configure(image="")
        self.root.update()
        if not os.path.exists(os.path.dirname(dst)): os.makedirs(os.path.dirname(dst))
        try:
            shutil.move(src, dst)
            self.history.append((dst, src))
            self.photo_list.pop(self.current_index)
            self.show_photo()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.show_photo()

    def undo_action(self):
        if not self.history: return
        last_dst, last_src = self.history.pop()
        try:
            self.image_display.configure(image="")
            self.root.update()
            shutil.move(last_dst, last_src)
            self.photo_list.insert(self.current_index, os.path.basename(last_src))
            self.show_photo()
        except Exception as e:
            messagebox.showerror("Error Undo", str(e))

if __name__ == "__main__":
    root = ctk.CTk()
    app = PhotoSorter(root)
    root.mainloop()
