def Menghitung_Total_Belanja(jumlah_barang):
  Total_harga = 0
  for _ in range(jumlah_barang):
    Harga_barang = float(input(f"Masukkan Harga Barang {_+1}:"))
    Total_harga += Harga_barang
  return Total_harga
Jumlah_barang = int(input("Masukkan Jumlah Barang: "))
total_belanja = Menghitung_Total_Belanja(Jumlah_barang)
print(f"Total belanjaan: Rp{total_belanja:.2f}")