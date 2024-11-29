import datetime

pesanan = []
id_pesanan = 1

# Data admin
admin_data = {"Risya": "123", "Melly": "321"}  
nama_admin = None  

def tampilkan_nama_toko():
    print("=" * 50)
    print("               SELAMAT DATANG DI")
    print("                 TOKO ARMY")
    print("=" * 50)

# Menampilkan menu
def tampilkan_menu():
    print("\n" + "=" * 50)
    print("                     MENU UTAMA")
    print("=" * 50)
    print(f"Admin: {nama_admin}")  
    print("=" * 50)
    print("1. Tambah Pesanan")
    print("2. Lihat Daftar Pesanan")
    print("3. Perbarui Pesanan")
    print("4. Hapus Pesanan")
    print("5. Keluar")
    print("=" * 50)
    pilihan = input("Pilih menu: ")
    return pilihan

# login admin
def login_admin():
    global nama_admin
    print("\n" + "=" * 50)
    print("                    LOGIN ADMIN")
    print("=" * 50)
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in admin_data and admin_data[username] == password:
        nama_admin = username
        print("\nLogin berhasil. Selamat datang, Admin!")
        return True
    else:
        print("\nUsername atau password salah. Silakan coba lagi.")
        return False

# Menambah pesanan
def tambah_pesanan():
    global id_pesanan
    print("\n" + "=" * 50)
    print("                  TAMBAH PESANAN")
    print("=" * 50)
    nama = input("Masukkan nama pelanggan: ")
    item = input("Masukkan item pesanan: ")

    try:
        jumlah = int(input("Masukkan jumlah: "))
        harga_per_item = float(input("Masukkan harga per item: "))
        if jumlah <= 0 or harga_per_item <= 0:
            print("Jumlah dan harga harus lebih dari 0.")
            return
    except ValueError:
        print("Input tidak valid, masukkan angka.")
        return

    total_harga = jumlah * harga_per_item
    tanggal = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  

    pesanan.append({
        "id": id_pesanan,
        "nama_pelanggan": nama,
        "item": item,
        "jumlah": jumlah,
        "harga_total": total_harga,
        "tanggal_pesanan": tanggal,
        "admin": nama_admin  
    })
    print(f"Pesanan berhasil ditambahkan dengan ID {id_pesanan}")
    id_pesanan += 1

# Daftar pesanan
def lihat_pesanan():
    print("\n" + "=" * 50)
    print("                  DAFTAR PESANAN")
    print("=" * 50)
    if len(pesanan) == 0:
        print("Belum ada pesanan.")
    else:
        for p in pesanan:
            print(f"ID Pesanan       : {p['id']}")
            print(f"Nama Pelanggan   : {p['nama_pelanggan']}")
            print(f"Item             : {p['item']}")
            print(f"Jumlah           : {p['jumlah']}")
            print(f"Harga Total      : Rp {p['harga_total']:.2f}")
            print(f"Tanggal Pesanan  : {p['tanggal_pesanan']}")
            print(f"Admin            : {p['admin']}")
            print("-" * 50)

# Perbarui pesanan
def perbarui_pesanan():
    print("\n" + "=" * 50)
    print("                 PERBARUI PESANAN")
    print("=" * 50)
    try:
        id_update = int(input("Masukkan ID pesanan yang ingin diperbarui: "))
    except ValueError:
        print("ID pesanan harus berupa angka. Silakan coba lagi.")
        return

    for p in pesanan:
        if p['id'] == id_update:
            print("\nPesanan ditemukan:")
            print("=" * 50)
            print(f"ID Pesanan       : {p['id']}")
            print(f"Nama Pelanggan   : {p['nama_pelanggan']}")
            print(f"Item             : {p['item']}")
            print(f"Jumlah           : {p['jumlah']}")
            print(f"Harga Total      : Rp {p['harga_total']:.2f}")
            print(f"Tanggal Pesanan  : {p['tanggal_pesanan']}")
            print(f"Admin            : {p['admin']}")
            print("=" * 50)

            nama_baru = input("Masukkan nama baru (kosongkan untuk tidak mengubah): ")
            item_baru = input("Masukkan item baru (kosongkan untuk tidak mengubah): ")
            jumlah_baru = input("Masukkan jumlah baru (kosongkan untuk tidak mengubah): ")
            harga_per_item_baru = input("Masukkan harga per item baru (kosongkan untuk tidak mengubah): ")

            # Perbarui data 
            p['nama_pelanggan'] = nama_baru or p['nama_pelanggan']
            p['item'] = item_baru or p['item']

            if jumlah_baru:
                try:
                    jumlah_baru = int(jumlah_baru)
                    if jumlah_baru <= 0:
                        print("Jumlah harus lebih dari 0. Perubahan dibatalkan.")
                        return
                    p['jumlah'] = jumlah_baru
                except ValueError:
                    print("Jumlah tidak valid. Perubahan dibatalkan.")
                    return

            if harga_per_item_baru:
                try:
                    harga_per_item_baru = float(harga_per_item_baru)
                    if harga_per_item_baru <= 0:
                        print("Harga per item harus lebih dari 0. Perubahan dibatalkan.")
                        return
                    p['harga_total'] = p['jumlah'] * harga_per_item_baru
                except ValueError:
                    print("Harga per item tidak valid. Perubahan dibatalkan.")
                    return

            print("\nPesanan berhasil diperbarui:")
            print("=" * 50)
            print(f"ID Pesanan       : {p['id']}")
            print(f"Nama Pelanggan   : {p['nama_pelanggan']}")
            print(f"Item             : {p['item']}")
            print(f"Jumlah           : {p['jumlah']}")
            print(f"Harga Total      : Rp {p['harga_total']:.2f}")
            print(f"Tanggal Pesanan  : {p['tanggal_pesanan']}")
            print(f"Admin            : {p['admin']}")
            print("=" * 50)
            return
    print("Pesanan tidak ditemukan.")

# Menghapus Pesanan
def hapus_pesanan():
    print("\n" + "=" * 50)
    print("                   HAPUS PESANAN")
    print("=" * 50)
    try:
        id_hapus = int(input("Masukkan ID pesanan yang ingin dihapus: "))
    except ValueError:
        print("ID pesanan harus berupa angka. Silakan coba lagi.")
        return

    for p in pesanan:
        if p['id'] == id_hapus:
            pesanan.remove(p)
            print("Pesanan berhasil dihapus.")
            return
    print("Pesanan tidak ditemukan.")

tampilkan_nama_toko()

while not login_admin():
    pass  

# Menu utama
while True:
    pilihan = tampilkan_menu()
    if pilihan == "1":
        tambah_pesanan()
    elif pilihan == "2":
        lihat_pesanan()
    elif pilihan == "3":
        perbarui_pesanan()
    elif pilihan == "4":
        hapus_pesanan()
    elif pilihan == "5":
        print("\n" + "=" * 50)
        print("          TERIMA KASIH TELAH MENGGUNAKAN")
        print("                  TOKO ARMY")
        print("=" * 50)
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")