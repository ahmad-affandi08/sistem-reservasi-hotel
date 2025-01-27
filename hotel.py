from pelanggan import Pelanggan
from kamar import Kamar
from reservasi import Reservasi
from pembayaran import Pembayaran
from admin import Admin

class Hotel:
    def __init__(self, nama_hotel):
        self.nama_hotel = nama_hotel
        self.kamar_list = []
        self.reservasi_list = []
        self.admin_list = []

    def tambah_kamar(self, kamar):
        self.kamar_list.append(kamar)

    def tampilkan_kamar(self):
        if not self.kamar_list:
            return "Tidak ada kamar tersedia."
        return "\n".join([kamar.tampilkan_informasi() for kamar in self.kamar_list])

    def tambah_admin(self, admin):
        """
        Menambahkan admin baru ke sistem.
        """
        self.admin_list.append(admin)

    def tampilkan_admin(self):
        """
        Menampilkan daftar admin.
        """
        if not self.admin_list:
            return "Belum ada admin terdaftar."
        return "\n".join([admin.tampilkan_informasi() for admin in self.admin_list])

    def buat_reservasi(self, pelanggan, nomor_kamar, tanggal_checkin, tanggal_checkout, admin):
        """
        Membuat reservasi baru berdasarkan tanggal check-in dan check-out, mencatat admin yang melayani.
        """
        kamar_dipilih = next((kamar for kamar in self.kamar_list if kamar.nomor_kamar == nomor_kamar and kamar.status == "tersedia"), None)
        if not kamar_dipilih:
            return f"Kamar dengan nomor {nomor_kamar} tidak tersedia."
        reservasi_baru = Reservasi(pelanggan, kamar_dipilih, tanggal_checkin, tanggal_checkout, admin)
        self.reservasi_list.append(reservasi_baru)
        return reservasi_baru.konfirmasi_reservasi()

    def tampilkan_reservasi(self):
        if not self.reservasi_list:
            return "Belum ada reservasi yang dilakukan."

        header = f"{'No':<5} {'Nama Pelanggan':<20} {'No. Kamar':<10} {'Check-in':<15} {'Check-out':<15}{'Jumlah Malam':<15} {'Admin':<20} {'Status Pembayaran':<20}"
        garis = "=" * len(header)
        hasil = [header, garis]

        for i, reservasi in enumerate(self.reservasi_list, 1):
            baris = f"{i:<5} {reservasi.pelanggan.nama:<20} {reservasi.kamar.nomor_kamar:<10} {reservasi.tanggal_checkin.strftime('%d-%m-%Y'):<15} {reservasi.tanggal_checkout.strftime('%d-%m-%Y'):<15}  {reservasi.jumlah_malam:<15}{reservasi.admin.nama:<20} {reservasi.status_pembayaran:<20}"
            hasil.append(baris)

        return "\n".join(hasil)

    def proses_pembayaran(self, metode_pembayaran, jumlah, reservasi):
        pembayaran = Pembayaran(metode_pembayaran, jumlah)
        hasil_pembayaran = pembayaran.proses_pembayaran(reservasi.total_harga)

        if "Pembayaran berhasil" in hasil_pembayaran:
            reservasi.status_pembayaran = "sudah"  # Update status pembayaran menjadi sudah dibayar
            return hasil_pembayaran

    def menu_admin(self):
        while True:
            print(f"\n==== Menu Admin {self.nama_hotel} ====")
            print("1. Tambah Kamar")
            print("2. Lihat Daftar Kamar")
            print("3. Tambah Reservasi")
            print("4. Lihat Daftar Reservasi")
            print("5. Tambah Admin")
            print("6. Lihat Daftar Admin")
            print("7. Keluar")
            
            pilihan = input("Pilih opsi (1-7): ")
            
            if pilihan == "1":
                self.menu_tambah_kamar()
            elif pilihan == "2":
                self.menu_lihat_kamar()
            elif pilihan == "3":
                self.menu_tambah_reservasi()
            elif pilihan == "4":
                self.menu_lihat_reservasi()
            elif pilihan == "5":
                self.menu_tambah_admin()
            elif pilihan == "6":
                self.menu_lihat_admin()
            elif pilihan == "7":
                print("Keluar dari menu admin.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def menu_tambah_kamar(self):
        nomor = input("Masukkan nomor kamar: ")
        tipe = input("Masukkan tipe kamar: ")
        harga = int(input("Masukkan harga kamar: "))
        kamar_baru = Kamar(nomor, tipe, harga)
        self.tambah_kamar(kamar_baru)
        print(f"Kamar {nomor} berhasil ditambahkan.")

    def menu_lihat_kamar(self):
        print("\nDaftar Kamar:")
        print(self.tampilkan_kamar())

    def menu_tambah_reservasi(self):
        nama = input("Masukkan nama pelanggan: ")
        email = input("Masukkan email pelanggan: ")
        telepon = input("Masukkan nomor telepon pelanggan: ")
        pelanggan_baru = Pelanggan(nama, email, telepon)
        
        nomor_kamar = input("Masukkan nomor kamar: ")
        tanggal_checkin = input("Masukkan tanggal check-in (DD-MM-YYYY): ")
        tanggal_checkout = input("Masukkan tanggal check-out (DD-MM-YYYY): ")
        
        if not self.admin_list:
            print("Belum ada admin terdaftar. Silakan tambahkan admin terlebih dahulu.")
            return

        print("\nPilih admin yang melayani:")
        for i, admin in enumerate(self.admin_list, 1):
            print(f"{i}. {admin.nama}")
        pilihan_admin = int(input("Masukkan nomor admin: "))
        admin_dipilih = self.admin_list[pilihan_admin - 1]

        hasil_reservasi = self.buat_reservasi(pelanggan_baru, nomor_kamar, tanggal_checkin, tanggal_checkout, admin_dipilih)
        print(hasil_reservasi)
        
        if "Reservasi berhasil" in hasil_reservasi:
            bayar_sekarang = input("Apakah Anda ingin membayar sekarang? (ya/tidak): ").lower()
            if bayar_sekarang == "ya":
                self.menu_proses_pembayaran(self.reservasi_list[-1])
            else:
                print("Anda memilih untuk membayar nanti. Status pembayaran adalah 'belum'.")

    def menu_proses_pembayaran(self, reservasi):
        print(f"\nTotal harga yang harus dibayar: {reservasi.total_harga}")
        metode_pembayaran = input("Pilih metode pembayaran (Tunai/Kartu Kredit): ")
        jumlah = int(input(f"Masukkan jumlah yang harus dibayar: "))

        hasil_pembayaran = self.proses_pembayaran(metode_pembayaran, jumlah, reservasi)
        print(hasil_pembayaran)

    def menu_lihat_reservasi(self):
        print("\nDaftar Reservasi:")
        print(self.tampilkan_reservasi())

    def menu_tambah_admin(self):
        nama = input("Masukkan nama admin: ")
        username = input("Masukkan username admin: ")
        admin_baru = Admin(nama, username)
        self.tambah_admin(admin_baru)
        print(f"Admin {nama} berhasil ditambahkan.")

    def menu_lihat_admin(self):
        print("\nDaftar Admin:")
        print(self.tampilkan_admin())
