def hitung_biaya_hotel(jenis_kamar, durasi_menginap):

    if jenis_kamar == "Standard":
        tarif = 320000
    elif jenis_kamar == "Deluxe":
        tarif = 6500000
    total_biaya = tarif * durasi_menginap
    return total_biaya


jenis_kamar = input("masukkan jenis kamar (Standard/Deluxe): ")
tanggal_check_in = int(input("masukkan tanggal check in: "))
bulan_check_in = input("masukkan bulan: ")
tanggal_check_out = int(input("masukkan tanggal check out: "))
bulan_check_out = input("masukkan bulan: ")

durasi_menginap = tanggal_check_out - tanggal_check_in
hasil = hitung_biaya_hotel(jenis_kamar, durasi_menginap)

print("\n=== DATA PEMESANAN HOTEL ===")
print("Jenis Kamar:", jenis_kamar)
print("Tanggal Check in:", tanggal_check_in, bulan_check_in)
print("Tanggal Check Out:", tanggal_check_out, bulan_check_out)
print("Durasi menginap:", durasi_menginap, "malam")
print("Total Biaya: Rp", hasil)