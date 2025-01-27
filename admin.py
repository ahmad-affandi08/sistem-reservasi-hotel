class Admin:
    def __init__(self, nama, username):
        """
        Inisialisasi objek Admin.
        """
        self.nama = nama
        self.username = username

    def tampilkan_informasi(self):
        """
        Menampilkan informasi admin.
        """
        return f"Admin: {self.nama}, Username: {self.username}"
