from hotel import Hotel
from kamar import Kamar

# Membuat instance Hotel
hotel_utama = Hotel("Hotel Mewah")

# Menambahkan beberapa kamar awal
hotel_utama.tambah_kamar(Kamar("101", "Deluxe", 500000))
hotel_utama.tambah_kamar(Kamar("102", "Suite", 1000000))
hotel_utama.tambah_kamar(Kamar("103", "Standard", 300000))

# Memulai Menu Admin
hotel_utama.menu_admin()