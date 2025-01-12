class Pembayaran:
    def _init_(self, metode_pembayaran, jumlah):
        self.metode_pembayaran = metode_pembayaran
        self.jumlah = jumlah

    def proses_pembayaran(self, total_harga):
        if self.jumlah >= total_harga:
            kembalian = self.jumlah - total_harga
            return f"Pembayaran berhasil. Kembalian: {kembalian}"
        return "Pembayaran gagal. Jumlah tidak mencukupi."