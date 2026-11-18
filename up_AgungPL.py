# PROGRAM KASIR KANTIN KAMPUS

jumlah_transaksi = int(input("Masukkan jumlah transaksi: "))

total_belanja = 0

for i in range(jumlah_transaksi):

    print("\nTransaksi ke-", i + 1)

    nama_makanan = input("Masukkan nama makanan: ")
    nama_minuman = input("Masukkan nama minuman: ")
    harga_makanan = int(input("Masukkan harga makanan: "))
    harga_minuman = int(input("Masukkan harga minuman: "))
    jumlah_pembelian_makanan = int(input("Masukkan jumlah pembelian makanan: "))
    jumlah_pembelian_minuman = int(input("Masukkan jumlah pembelian minuman: "))

    total_harga_makanan = harga_makanan * jumlah_pembelian_makanan
    total_harga_minuman = harga_minuman * jumlah_pembelian_minuman


    print("Nama makanan:", nama_makanan)
    print("Total harga makanan:", total_harga_makanan)
    print("Nama minuman:", nama_minuman)
    print("Total harga minuman:", total_harga_minuman)

    total_belanja = total_belanja + total_harga_makanan + total_harga_minuman

if total_belanja > 100000:
    diskon = int (10 / 100 * total_belanja)
    total_pembayaran = int (total_belanja - diskon) 

else:
    diskon = 0
    total_pembayaran = total_belanja

print("\n======= HASIL PEMBAYARAN =======")
print("Total belanja:", total_belanja)
print("Diskon:", diskon)
print("Total pembayaran:", total_pembayaran)
print("\n======= TERIMA KASIH =======")
print("======= KANTIN UMSU TOP   =======")