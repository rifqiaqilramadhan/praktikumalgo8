def perpangkatan(base, power):
    return 1 if power == 0 else base * perpangkatan(base, power - 1)

angka_number = float(input("Masukkan angka: "))
pangkat_number = int(input("Masukkan pangkat: "))

print(f"Hasil perpangkatan {angka_number}^{pangkat_number} adalah: {perpangkatan(angka_number, pangkat_number)}")
