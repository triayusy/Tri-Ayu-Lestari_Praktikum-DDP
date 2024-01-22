import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class ParkirApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.root.title("Biaya Karcis")
        
        # Warna
        self.bg_color = "cyan"
        self.button_color = "blue"
        self.label_color = "black"

        self.JAM_MASUK = tk.StringVar()
        self.JAM_KELUAR = tk.StringVar()
        self.JENIS_KENDARAAN = tk.StringVar()
        self.SELISIH_JAM_TEXT = tk.StringVar()
        self.BIAYA_TEXT = tk.StringVar()

        # Frame input
        self.input_frame = ttk.Frame(root, style="TFrame")
        self.judul_frame = ttk.Frame(root, style="TFrame")

        # penempatan grid, pack, place
        self.input_frame.pack(padx=10, pady=10, fill="x", expand=True)
        self.judul_frame.pack(padx=20, pady=20, fill="x", expand=True)

        # judul Program
        self.judul_frame_label = ttk.Label(self.input_frame, text="Program Karcis Parkir", font="bold", background=self.bg_color, foreground=self.label_color)
        self.judul_frame_label.pack(padx=10, fill="x", expand=True)
        self.judul_frame_label.configure(anchor="center")

        # Komponen-komponen
        # 1. Label Jenis Kendaraan
        self.jenis_kendaraan_label = ttk.Label(self.input_frame, text="Jenis Kendaraan : ", background=self.bg_color, foreground=self.label_color)
        self.jenis_kendaraan_label.pack(padx=10, fill="x", expand=True)

        # 2. Entry Jenis Kendaraan (Dropdown)
        options = ["mobil", "motor"]  # Pilihan jenis kendaraan
        self.jenis_kendaraan_entry = ttk.Combobox(self.input_frame, textvariable=self.JENIS_KENDARAAN, values=options, background=self.bg_color)
        self.jenis_kendaraan_entry.pack(padx=10, fill="x", expand=True)
        self.jenis_kendaraan_entry.set("Pilih Jenis Kendaraan")  # Nilai default yang ditampilkan

        # 3. Label Jam Masuk
        self.jam_masuk_label = ttk.Label(self.input_frame, text="Jam Masuk : ", background=self.bg_color, foreground=self.label_color)
        self.jam_masuk_label.pack(padx=10, fill="x", expand=True)

        # 4. Entry Jam Masuk
        self.jam_masuk_entry = ttk.Entry(self.input_frame, textvariable=self.JAM_MASUK)
        self.jam_masuk_entry.pack(padx=10, fill="x", expand=True)

        # 5. Label Jam Keluar
        self.jam_keluar_label = ttk.Label(self.input_frame, text="Jam Keluar : ", background=self.bg_color, foreground=self.label_color)
        self.jam_keluar_label.pack(padx=10, fill="x", expand=True)

        # 6. Entry Jam Keluar
        self.jam_keluar_entry = ttk.Entry(self.input_frame, textvariable=self.JAM_KELUAR)
        self.jam_keluar_entry.pack(padx=10, fill="x", expand=True)

        # 7. Tombol
        self.TARIF_PER_JAM_PERTAMA = 3000
        self.TARIF_PER_JAM_BERIKUTNYA = 1000

        self.tombol_sapa = ttk.Button(self.input_frame, text="Hitung Biaya", command=self.tombol_click, style="TButton")
        self.tombol_sapa.pack(fill="x", expand=True, padx=10, pady=10)

        # Menambahkan label untuk menampilkan hasil
        self.hasil_label = ttk.Label(self.input_frame, text="Hasil: ", background=self.bg_color, foreground=self.label_color)
        self.hasil_label.pack(padx=10, fill="x", expand=True)

        # Menambahkan label untuk menampilkan hasil selisih jam
        self.selisih_jam_label = ttk.Label(self.input_frame, textvariable=self.SELISIH_JAM_TEXT, background=self.bg_color, foreground=self.label_color)
        self.selisih_jam_label.pack(padx=10, fill="x", expand=True)

        # Menambahkan label untuk menampilkan hasil biaya
        self.biaya_label = ttk.Label(self.input_frame, textvariable=self.BIAYA_TEXT, background=self.bg_color, foreground=self.label_color)
        self.biaya_label.pack(padx=10, fill="x", expand=True)

    def tombol_click(self):
        jenis_kendaraan = self.jenis_kendaraan_entry.get()
        jam_masuk_str = self.JAM_MASUK.get()
        jam_keluar_str = self.JAM_KELUAR.get()

        try:
            # Pisahkan jam
            jam_masuk = int(jam_masuk_str.split(":")[0])
            jam_keluar = int(jam_keluar_str.split(":")[0])

            # Hitung selisih jam
            selisih_jam = jam_keluar - jam_masuk

            # Hitung biaya berdasarkan selisih jam dan tarif per jam
            if selisih_jam > 0:
                biaya = self.TARIF_PER_JAM_PERTAMA + (selisih_jam - 1) * self.TARIF_PER_JAM_BERIKUTNYA
            else:
                biaya = 0

            # Set nilai variabel StringVar untuk hasil selisih jam dan biaya
            self.SELISIH_JAM_TEXT.set(f"Selisih waktu: {selisih_jam} jam")
            self.BIAYA_TEXT.set(f"Biaya: {biaya} rupiah")

            # Menampilkan jenis kendaraan di alert
            pesan = f"Jenis Kendaraan: {jenis_kendaraan}\nDurasi Parkir : {selisih_jam} jam\nBiaya: {biaya} rupiah"
            showinfo(title="Pembayaran Berhasil!", message=pesan)

        except ValueError:
            showinfo(title="Error", message="Format waktu tidak valid")


if __name__ == "__main__":
    root = tk.Tk()
    app = ParkirApp(root)
    root.mainloop()