harga_satuan = float(input("masukan harga satuan:"))
jumlah = int(input("masukan jumlah barang:"))
persen_diskon = float(input("masukan persen diskon:"))

subtotal = harga_satuan * jumlah
nominal_diskon = subtotal * (persen_diskon / 100)
total = subtotal = nominal_diskon

print("subtotal = ", subtotal)
print("nominal diskon =", nominal_diskon)
print("total = ", total)