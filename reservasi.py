from pelanggan import Pelanggan
from kamar import Kamar

class Reservasi:
    def _init_(self, pelanggan, kamar, jumlah_malam):
        self.pelanggan = pelanggan
        self.kamar = kamar
        self.jumlah_malam = jumlah_malam
        self.total_harga = self.hitung_total_harga()

    def hitung_total_harga(self):
        return self.jumlah_malam * self.kamar.harga_per_malam

    def konfirmasi_reservasi(self):
        if self.kamar.status == "tersedia":
            self.kamar.ubah_status("dipesan")
            return f"Reservasi berhasil untuk {self.pelanggan.nama} di kamar {self.kamar.nomor_kamar} selama {self.jumlah_malam} malam."
        return "Kamar sudah dipesan."

    def tampilkan_detail_reservasi(self):
        return f"Reservasi oleh {self.pelanggan.nama}, Kamar: {self.kamar.nomor_kamar}, Jumlah Malam: {self.jumlah_malam}, Total Harga: {self.total_harga}"