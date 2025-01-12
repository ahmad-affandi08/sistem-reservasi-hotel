from pelanggan import Pelanggan
from kamar import Kamar
from reservasi import Reservasi
from pembayaran import Pembayaran

class Hotel:
    def __init__(self, nama_hotel):
        self.nama_hotel = nama_hotel
        self.kamar_list = []
        self.reservasi_list = []

    def tambah_kamar(self, kamar):
        self.kamar_list.append(kamar)

    def tampilkan_kamar(self):
        if not self.kamar_list:
            return "Tidak ada kamar tersedia."
        return "\n".join([kamar.tampilkan_informasi() for kamar in self.kamar_list])

    def buat_reservasi(self, pelanggan, nomor_kamar, jumlah_malam):
        kamar_dipilih = next((kamar for kamar in self.kamar_list if kamar.nomor_kamar == nomor_kamar and kamar.status == "tersedia"), None)
        if not kamar_dipilih:
            return f"Kamar dengan nomor {nomor_kamar} tidak tersedia."
        reservasi_baru = Reservasi(pelanggan, kamar_dipilih, jumlah_malam)
        self.reservasi_list.append(reservasi_baru)
        return reservasi_baru.konfirmasi_reservasi()

    def tampilkan_reservasi(self):
        if not self.reservasi_list:
            return "Belum ada reservasi yang dilakukan."
        return "\n".join([reservasi.tampilkan_detail_reservasi() for reservasi in self.reservasi_list])

    def proses_pembayaran(self, metode_pembayaran, jumlah, reservasi):
        pembayaran = Pembayaran(metode_pembayaran, jumlah)
        return pembayaran.proses_pembayaran(reservasi.total_harga)

    # Menu Admin
    def menu_admin(self):
        while True:
            print(f"\n==== Menu Admin {self.nama_hotel} ====")
            print("1. Tambah Kamar")
            print("2. Lihat Daftar Kamar")
            print("3. Tambah Reservasi")
            print("4. Lihat Daftar Reservasi")
            print("5. Keluar")
            
            pilihan = input("Pilih opsi (1-5): ")
            
            if pilihan == "1":
                self.menu_tambah_kamar()
            elif pilihan == "2":
                self.menu_lihat_kamar()
            elif pilihan == "3":
                self.menu_tambah_reservasi()
            elif pilihan == "4":
                self.menu_lihat_reservasi()
            elif pilihan == "5":
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
        jumlah_malam = int(input("Masukkan jumlah malam: "))
        hasil = self.buat_reservasi(pelanggan_baru, nomor_kamar, jumlah_malam)
        print(hasil)

    def menu_lihat_reservasi(self):
        print("\nDaftar Reservasi:")
        print(self.tampilkan_reservasi())
