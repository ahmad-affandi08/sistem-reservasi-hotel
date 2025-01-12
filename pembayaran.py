class Pembayaran:
    def __init__(self, metode_pembayaran, jumlah):
        self.metode_pembayaran = metode_pembayaran
        self.jumlah = jumlah

    def proses_pembayaran(self, total_harga):
        if self.jumlah < total_harga:
            return "Pembayaran gagal: Jumlah yang dibayar kurang."
        elif self.jumlah == total_harga:
            return f"Pembayaran berhasil menggunakan {self.metode_pembayaran}. Terima kasih."
        else:
            return "Pembayaran gagal: Jumlah yang dibayar lebih."
