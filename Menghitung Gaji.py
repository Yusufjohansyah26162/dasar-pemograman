def hitung_gaji(gaji_pokok, hari_transport, hari_makan, jam_lembur):
    uang_transport_harian = 100000
    uang_makan_harian = 50000
    upah_lembur_per_jam = [100000, 150000]  # index 0: 1-2 jam, index 1: jam berikutnya

    total_transport = hari_transport * uang_transport_harian
    total_makan = hari_makan * uang_makan_harian

    total_upah_lembur = 0
    if jam_lembur > 0:
        total_upah_lembur += upah_lembur_per_jam[0]  # upah lembur untuk jam pertama
        if jam_lembur > 2:
            total_upah_lembur += (jam_lembur - 2) * upah_lembur_per_jam[1]  # upah lembur untuk jam berikutnya

    honor = gaji_pokok + total_transport + total_makan + total_upah_lembur
    return honor

def main():
    gaji_pokok = float(input("Masukkan gaji pokok: "))
    hari_transport = int(input("Masukkan jumlah hari transport: "))
    hari_makan = int(input("Masukkan jumlah hari makan: "))
    jam_lembur = int(input("Masukkan jumlah jam lembur: "))

    total_honor = hitung_gaji(gaji_pokok, hari_transport, hari_makan, jam_lembur)
    print("Total honor yang diterima adalah Rp.", total_honor)

if __name__ == "__main__":
    main()

