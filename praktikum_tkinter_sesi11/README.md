Aplikasi Pendaftaran Kegiatan Mahasiswa
Aplikasi desktop sederhana berbasis Python Tkinter untuk mengisi dan
menampilkan data pendaftaran kegiatan mahasiswa. Program ini dibuat
sebagai contoh penggunaan komponen antarmuka (widget) dan penanganan
event (event handling) pada Tkinter.
Fitur
- Form data mahasiswa
  - Input nama mahasiswa.
  - Pilihan program studi melalui Combobox.
  - Pilihan jenis kelamin melalui Radiobutton.
- Pilihan kegiatan
  - Memilih kegiatan menggunakan Checkbutton.
  - Memilih kegiatan menggunakan Listbox dengan mode pilihan
    ganda.
  - Pilihan dari kedua komponen digabungkan dan duplikasi
    dihilangkan.
- Alasan mengikuti kegiatan
  - Mengisi alasan melalui komponen Text.
- Validasi formulir
  - Nama wajib diisi.
  - Program studi wajib dipilih.
  - Jenis kelamin wajib dipilih.
  - Minimal satu kegiatan harus dipilih.
- Ringkasan pendaftaran
  - Menampilkan data yang telah diisi pada area informasi.
  - Menampilkan pesan ketika validasi gagal atau pendaftaran
    berhasil.
- Menu aplikasi
  - File > Reset Form untuk mengosongkan formulir.
  - File > Exit/Keluar untuk menutup aplikasi.
  - Bantuan > About untuk menampilkan informasi aplikasi.
- Event keyboard
  - Tombol Enter menjalankan proses Submit.
Teknologi
- Bahasa pemrograman: Python 3
- GUI: Tkinter
- Komponen tambahan: ttk, messagebox
Tkinter umumnya sudah disertakan dalam instalasi Python. Pada beberapa
distribusi Linux, paket Tkinter mungkin perlu dipasang terpisah.
Persyaratan
- Python 3
- Tkinter tersedia pada instalasi Python
Cara Menjalankan
1. Simpan kode program ke dalam file, misalnya
   pendaftaran_mahasiswa.py.
2. Buka Terminal atau Command Prompt pada folder tempat file disimpan.
3. Jalankan perintah:
   python pendaftaran_mahasiswa.py
   Jika perintah python tidak dikenali pada Windows, coba:
   py pendaftaran_mahasiswa.py
4. Jendela Pendaftaran Kegiatan Mahasiswa akan terbuka.
Cara Menggunakan
1. Masukkan nama mahasiswa.
2. Pilih program studi.
3. Pilih jenis kelamin.
4. Pilih satu atau lebih kegiatan melalui Checkbutton dan/atau Listbox.
5. Isi alasan mengikuti kegiatan jika diperlukan.
6. Tekan tombol Submit atau tombol Enter.
7. Jika data wajib belum lengkap, aplikasi akan menampilkan pesan
   validasi.
8. Jika validasi berhasil, ringkasan pendaftaran akan muncul pada
   bagian Area Informasi.
9. Gunakan tombol Reset atau menu File > Reset Form untuk
   mengosongkan formulir.
Daftar Kegiatan
Pilihan kegiatan yang tersedia pada program:
- Seminar
- Workshop
- Bakti Sosial
- Lomba
Pilihan program studi yang tersedia:
- Teknik Informatika
- Sistem Informasi
- Manajemen
- Akuntansi
Struktur Program
  Bagian/Kelas/Metode                 Fungsi
  PendaftaranMahasiswa              Kelas utama yang mengatur jendela
dan seluruh fungsi aplikasi.

  __init__()                        Menginisialisasi jendela, variabel
input, menu, antarmuka, dan event
Enter.

  buat_menu()                       Membuat menu File dan Bantuan.

  buat_antarmuka()                  Membuat seluruh komponen formulir
dan area informasi.

  ambil_kegiatan()                  Mengambil pilihan Checkbutton dan
Listbox, lalu menggabungkannya
tanpa duplikasi.

  submit()                          Memvalidasi input dan menampilkan
ringkasan pendaftaran.

  reset()                           Mengosongkan seluruh input dan
mengembalikan tampilan awal.
tampilkan_about()                 Membuka jendela informasi aplikasi
menggunakan Toplevel.
Catatan
Program ini merupakan contoh aplikasi GUI sederhana. Data pendaftaran
hanya ditampilkan pada area informasi selama aplikasi berjalan.
Program belum menyimpan data ke file atau database, sehingga data
tidak menjadi arsip permanen setelah aplikasi ditutup.
Lisensi
Contoh program untuk keperluan pembelajaran dan praktikum Python
Tkinter.