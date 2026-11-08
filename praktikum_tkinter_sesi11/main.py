import tkinter as tk
from tkinter import ttk, messagebox


class PendaftaranMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Pendaftaran Kegiatan Mahasiswa")
        self.root.geometry("760x700")
        self.root.minsize(650, 600)

        # Variabel input
        self.nama_var = tk.StringVar()
        self.prodi_var = tk.StringVar()
        self.gender_var = tk.StringVar(value="")
        self.kegiatan_vars = {
            "Seminar": tk.BooleanVar(value=False),
            "Workshop": tk.BooleanVar(value=False),
            "Bakti Sosial": tk.BooleanVar(value=False),
            "Lomba": tk.BooleanVar(value=False),
        }

        self.buat_menu()
        self.buat_antarmuka()

        # Event keyboard: tombol Enter menjalankan Submit
        self.root.bind("<Return>", self.submit)

    def buat_menu(self):
        menu_bar = tk.Menu(self.root)

        menu_file = tk.Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="Reset Form", command=self.reset)
        menu_file.add_separator()
        menu_file.add_command(label="Exit/Keluar", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=menu_file)

        menu_bantuan = tk.Menu(menu_bar, tearoff=0)
        menu_bantuan.add_command(label="About", command=self.tampilkan_about)
        menu_bar.add_cascade(label="Bantuan", menu=menu_bantuan)

        self.root.config(menu=menu_bar)

    def buat_antarmuka(self):
        # Frame utama
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill="both", expand=True)

        ttk.Label(
            main_frame,
            text="FORM PENDAFTARAN KEGIATAN MAHASISWA",
            font=("Arial", 16, "bold")
        ).pack(pady=(0, 12))

        # Frame data mahasiswa
        data_frame = ttk.LabelFrame(main_frame, text="Data Mahasiswa", padding=10)
        data_frame.pack(fill="x", pady=5)

        ttk.Label(data_frame, text="Nama:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.nama_entry = ttk.Entry(data_frame, textvariable=self.nama_var, width=40)
        self.nama_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        ttk.Label(data_frame, text="Program Studi:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.prodi_combo = ttk.Combobox(
            data_frame,
            textvariable=self.prodi_var,
            values=["Teknik Informatika", "Sistem Informasi", "Manajemen", "Akuntansi"],
            state="readonly",
            width=37
        )
        self.prodi_combo.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        ttk.Label(data_frame, text="Jenis Kelamin:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        gender_frame = ttk.Frame(data_frame)
        gender_frame.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        ttk.Radiobutton(
            gender_frame, text="Laki-laki", variable=self.gender_var, value="Laki-laki"
        ).pack(side="left", padx=(0, 12))
        ttk.Radiobutton(
            gender_frame, text="Perempuan", variable=self.gender_var, value="Perempuan"
        ).pack(side="left")

        data_frame.columnconfigure(1, weight=1)

        # Frame pilihan kegiatan (Checkbutton)
        kegiatan_frame = ttk.LabelFrame(main_frame, text="Pilih Kegiatan (Checkbutton)", padding=10)
        kegiatan_frame.pack(fill="x", pady=5)

        for index, (nama_kegiatan, variable) in enumerate(self.kegiatan_vars.items()):
            ttk.Checkbutton(
                kegiatan_frame, text=nama_kegiatan, variable=variable
            ).grid(row=index // 2, column=index % 2, sticky="w", padx=10, pady=4)

        # Frame alasan
        alasan_frame = ttk.LabelFrame(main_frame, text="Alasan Mengikuti Kegiatan", padding=10)
        alasan_frame.pack(fill="x", pady=5)

        self.alasan_text = tk.Text(alasan_frame, height=4, wrap="word")
        self.alasan_text.pack(fill="x")

        # Listbox pengembangan: daftar kegiatan
        list_frame = ttk.LabelFrame(main_frame, text="Daftar Kegiatan (Listbox)", padding=10)
        list_frame.pack(fill="x", pady=5)

        self.kegiatan_listbox = tk.Listbox(list_frame, height=4, selectmode=tk.MULTIPLE)
        for nama_kegiatan in self.kegiatan_vars:
            self.kegiatan_listbox.insert(tk.END, nama_kegiatan)
        self.kegiatan_listbox.pack(side="left", fill="x", expand=True)

        list_scroll = ttk.Scrollbar(list_frame, orient="vertical", command=self.kegiatan_listbox.yview)
        list_scroll.pack(side="right", fill="y")
        self.kegiatan_listbox.config(yscrollcommand=list_scroll.set)

        ttk.Label(
            main_frame,
            text="Pilih kegiatan melalui Checkbutton atau Listbox. Minimal satu kegiatan.",
            foreground="gray"
        ).pack(anchor="w", pady=(3, 8))

        # Tombol aksi
        tombol_frame = ttk.Frame(main_frame)
        tombol_frame.pack(fill="x", pady=8)

        ttk.Button(tombol_frame, text="Submit", command=self.submit).pack(side="left", padx=5)
        ttk.Button(tombol_frame, text="Reset", command=self.reset).pack(side="left", padx=5)

        # Area informasi hasil
        hasil_frame = ttk.LabelFrame(main_frame, text="Area Informasi", padding=10)
        hasil_frame.pack(fill="both", expand=True, pady=5)

        self.hasil_label = ttk.Label(
            hasil_frame,
            text="Hasil pendaftaran akan ditampilkan di sini.",
            justify="left",
            anchor="nw"
        )
        self.hasil_label.pack(fill="both", expand=True)

    def ambil_kegiatan(self):
        # Ambil pilihan Checkbutton
        pilihan_check = [
            nama for nama, variable in self.kegiatan_vars.items()
            if variable.get()
        ]

        # Ambil pilihan Listbox
        indeks_terpilih = self.kegiatan_listbox.curselection()
        pilihan_list = [
            self.kegiatan_listbox.get(index) for index in indeks_terpilih
        ]

        # Gabungkan tanpa duplikasi
        return list(dict.fromkeys(pilihan_check + pilihan_list))

    def submit(self, event=None):
        nama = self.nama_var.get().strip()
        prodi = self.prodi_var.get().strip()
        gender = self.gender_var.get()
        kegiatan = self.ambil_kegiatan()
        alasan = self.alasan_text.get("1.0", tk.END).strip()

        # Validasi input
        if not nama:
            messagebox.showwarning("Validasi", "Nama tidak boleh kosong.")
            self.nama_entry.focus_set()
            return

        if not prodi:
            messagebox.showwarning("Validasi", "Silakan pilih program studi.")
            self.prodi_combo.focus_set()
            return

        if not gender:
            messagebox.showwarning("Validasi", "Silakan pilih jenis kelamin.")
            return

        if not kegiatan:
            messagebox.showwarning("Validasi", "Pilih minimal satu kegiatan.")
            return

        # Tampilkan hasil pendaftaran
        teks_kegiatan = ", ".join(kegiatan)
        ringkasan = (
            f"Nama: {nama}\n"
            f"Program Studi: {prodi}\n"
            f"Jenis Kelamin: {gender}\n"
            f"Kegiatan: {teks_kegiatan}\n"
            f"Alasan: {alasan if alasan else '-'}"
        )

        self.hasil_label.config(text=ringkasan)
        messagebox.showinfo("Pendaftaran Berhasil", "Data pendaftaran berhasil disimpan.")

    def reset(self):
        # Mengosongkan seluruh input
        self.nama_var.set("")
        self.prodi_var.set("")
        self.gender_var.set("")

        for variable in self.kegiatan_vars.values():
            variable.set(False)

        self.alasan_text.delete("1.0", tk.END)
        self.kegiatan_listbox.selection_clear(0, tk.END)
        self.hasil_label.config(text="Hasil pendaftaran akan ditampilkan di sini.")
        self.nama_entry.focus_set()

    def tampilkan_about(self):
        # Jendela About menggunakan Toplevel
        about_window = tk.Toplevel(self.root)
        about_window.title("About")
        about_window.geometry("350x220")
        about_window.resizable(False, False)
        about_window.transient(self.root)

        frame = ttk.Frame(about_window, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text="Pendaftaran Kegiatan Mahasiswa",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        ttk.Label(
            frame,
            text="Praktikum Python Tkinter\nSesi 11 - Advanced Widgets dan Event Handling\n\n"
                 "Aplikasi contoh untuk pendaftaran kegiatan mahasiswa.",
            justify="center"
        ).pack(pady=5)

        ttk.Button(frame, text="Tutup", command=about_window.destroy).pack(pady=8)


if __name__ == "__main__":
    root = tk.Tk()
    app = PendaftaranMahasiswa(root)
    root.mainloop()
