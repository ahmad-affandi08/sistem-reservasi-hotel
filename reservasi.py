from pelanggan import Pelanggan
from kamar import Kamar
from datetime import datetime

class Reservasi:
    def __init__(self, pelanggan, kamar, tanggal_checkin, tanggal_checkout, admin):
        """
        Inisialisasi objek Reservasi.
        """
        self.pelanggan = pelanggan
        self.kamar = kamar
        self.tanggal_checkin = datetime.strptime(tanggal_checkin, "%d-%m-%Y")  # Format: DD-MM-YYYY
        self.tanggal_checkout = datetime.strptime(tanggal_checkout, "%d-%m-%Y")
        self.jumlah_malam = self.hitung_jumlah_malam()
        self.total_harga = self.hitung_total_harga()
        self.status_pembayaran = "belum"  # Status pembayaran awalnya belum dibayar
        self.admin = admin  # Admin yang melayani reservasi

    def hitung_jumlah_malam(self):
        """
        Menghitung jumlah malam berdasarkan tanggal check-in dan check-out.
        """
        delta = self.tanggal_checkout - self.tanggal_checkin
        return delta.days

    def hitung_total_harga(self):
        """
        Menghitung total harga berdasarkan jumlah malam dan harga per malam kamar.
        """
        return self.jumlah_malam * self.kamar.harga_per_malam

    def konfirmasi_reservasi(self):
        """
        Mengonfirmasi reservasi dan mengubah status kamar menjadi 'dipesan' jika tersedia.
        """
        if self.kamar.status == "tersedia":
            self.kamar.ubah_status("dipesan")
            return (
                f"Reservasi berhasil!\n"
                f"Nama Pelanggan: {self.pelanggan.nama}\n"
                f"Kamar: {self.kamar.nomor_kamar} ({self.kamar.tipe_kamar})\n"
                f"Tanggal Check-in: {self.tanggal_checkin.strftime('%d-%m-%Y')}\n"
                f"Tanggal Check-out: {self.tanggal_checkout.strftime('%d-%m-%Y')}\n"
                f"Jumlah Malam: {self.jumlah_malam}\n"
                f"Total Harga: {self.total_harga}\n"
                f"Dilayani oleh: {self.admin.nama}"
            )
        return "Kamar sudah dipesan. Silakan pilih kamar lain."

    def tampilkan_detail_reservasi(self):
        """
        Menampilkan detail lengkap dari reservasi.
        """
        return (
            f"Reservasi oleh {self.pelanggan.nama}, Kamar: {self.kamar.nomor_kamar}, "
            f"Tanggal Check-in: {self.tanggal_checkin.strftime('%d-%m-%Y')}, "
            f"Tanggal Check-out: {self.tanggal_checkout.strftime('%d-%m-%Y')}, "
            f"Jumlah Malam: {self.jumlah_malam}, Total Harga: {self.total_harga}, "
            f"Status Pembayaran: {self.status_pembayaran}, Dilayani oleh: {self.admin.nama}"
        )
