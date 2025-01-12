class Kamar:
    def __init__(self, nomor_kamar, tipe_kamar, harga_per_malam):
        self.nomor_kamar = nomor_kamar
        self.tipe_kamar = tipe_kamar
        self.harga_per_malam = harga_per_malam
        self.status = "tersedia"  # Status: tersedia/dipesan

    def tampilkan_informasi(self):
        return f"Nomor Kamar: {self.nomor_kamar}, Tipe: {self.tipe_kamar}, Harga: {self.harga_per_malam}, Status: {self.status}"

    def ubah_status(self, status_baru):
        self.status = status_baru
