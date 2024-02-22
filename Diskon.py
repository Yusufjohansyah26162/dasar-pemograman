def hitung_total_pembayaran(total_belanja):
    diskon = 0
    if total_belanja > 60000:
        diskon = 10000
    total_pembayaran = total_belanja - diskon
    return total_pembayaran

def main():
    total_belanja = float(input("Masukkan total belanja Anda: "))
    total_pembayaran = hitung_total_pembayaran(total_belanja)
    print("Total yang harus dibayar: Rp.", total_pembayaran)

if __name__ == "__main__":
    main()
