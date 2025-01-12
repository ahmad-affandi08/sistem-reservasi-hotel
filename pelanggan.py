class Pelanggan:
    def _init_(self, nama, email, no_telepon):
        self.nama = nama
        self.email = email
        self.no_telepon = no_telepon

    def tampilkan_informasi(self):
        return f"Nama: {self.nama}, Email: {self.email}, No Telepon: {self.no_telepon}"