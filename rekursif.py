def penjumlahan_berurutan(jumlah):
    total = 0
    for i in range(jumlah):
        angka = float(input(f"Masukkan angka ke-{i + 1}: "))
        total += angka
    return total

jumlah = int(input("Masukkan Jumlah: "))
hasil_penjumlahan = penjumlahan_berurutan(jumlah)
print(f"Hasil penjumlahan: {hasil_penjumlahan}")
