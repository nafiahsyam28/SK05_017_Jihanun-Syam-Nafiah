# SK05_017_Jihanun-Syam-Nafiah

# Penjelasan Kode Program
Program ini dibuat untuk menghitung biaya pemesanan kamar hotel berdasarkan jenis kamar dan lama menginap, sehingga memudahkan dan dapat membantu resepsionis maupun tamu hotel. Pengguna memasukkan jenis kamar dan tanggal check-in serta check-out. Setelah itu, program menghitung durasi menginap dan menentukan niaya sesuai jenis kamar yang dipilih. Hasil perhitungan kemudian ditampilkan berupa jenis kamar, tanggal menginap, durasi menginap, dan total biaya hotel.

1. Function hitung_biaya_hotel = digunakan untuk membuat function yang menghitung total biaya hotel.
2. if & elif percabangan jenis kamar = untuk menentukan harga kamar berdasarkan jenis kamar yang dipilih. Kamar Standard memiliki tarif Rp320.000 per malam, sedangkan kamar Deluxe memiliki tarif Rp6.500.000 per malam.
3. total_biaya = tarif * durasi_menginap = digunakan untuk menghitung total biaya
4. return = Digunakan untuk mengembalikan hasil total biaya dari function.
5. hasil = hitung_biaya_hotel(jenis_kamar, durasi_menginap) = Digunakan untuk memanggil function hitung_biaya_hotel() dan menyimpan hasil perhitungan ke dalam variabel hasil
6. print("\n=== DATA PEMESANAN HOTEL ===") = Digunakan untuk menampilkan data pemesanan hotel dan total biaya yang harus dibayar oleh pengguna. <br>

 <img width="524" height="64" alt="Screenshot 2026-09-23 120159" src="https://github.com/user-attachments/assets/7989a837-876c-407a-9a4c-b4ad7781a360" />

 Ini adalah hasil output pertama dimana program meminta pengguna untuk memasukkan pilihan jenis kamar yaitu Standard atau Deluxe, setelah itu program meminta pengguna memasukkan tanggal dan bulan check in


 <img width="205" height="50" alt="Screenshot 2026-09-23 120604" src="https://github.com/user-attachments/assets/f0ae808d-ea50-46d0-a63b-4ff211daa1ed" />

Lalu selanjutnya pengguna memasukkan tanggal dan bulan check out agar program bisa menentukan biaya yang dihasilkan. Di dalam output ini pengguna memasukkan tanggal check out yaitu 26 bulan Mei

<img width="250" height="122" alt="Screenshot 2026-09-23 120622" src="https://github.com/user-attachments/assets/9da85dbe-c33e-455a-b7d2-f9f46ad2b4e1" />

Terakhir, setelah pengguna sudah memasukan jenis kamar kemudia tanggal, bulan check in dan check out maka selanjutnya program menampilkan data pemesanan hotal yang sudah di hitung. Hasil tarif akhir yaitu Rp1.300.000 karena tamu memakai jenis kamar deluxe dimana per malam dikenakan tarif Rp650.000
