Latihan 1: Menentukan Bilangan Terbesar dari 4 Bilangan (Python)
Penjelasan Tugas
Tugas ini bertujuan untuk membuat program Python yang dapat menerima empat buah input bilangan bulat dan menentukan serta mencetak bilangan mana yang memiliki nilai terbesar.
Penjelasan Kode Program:

Input Data: Program meminta 4 bilangan dari user (A, B, C, D)
Perbandingan Berurutan:
if A >= B and A >= C and A >= D: Cek apakah A terbesar
elif B >= A and B >= C and B >= D: Cek apakah B terbesar
elif C >= A and C >= B and C >= D: Cek apakah C terbesar
else: Jika bukan A, B, atau C, maka D pasti terbesar
Output: Menampilkan urutan bilangan mana yang terbesar

Latihan 2: Mengurutkan Data (Python)
Penjelasan Tugas
Tugas ini bertujuan untuk membuat program Python yang dapat mengurutkan data berdasarkan input sejumlah data ( minimal 3 ), kemudian tampilkan hasilnya secara berurutan dari yang terkecil.

penjelasan kode program:
input data: masukan jumlah data yang ingin di tampilkan ( minimal 3)
jika jumlah data < 3, maka output keluar "jumlah data harus minimal 3"
jika tidak
data [] membuat list kosong untuk menyimpan nilai-nilai yang akan dimasukkan
lalu gunakan loop range sebanyak jumlah_data yang di input
i dimulai dari 0 sampai jumlah data - 1
input nilai sesuai banyaknya jumlah data
contoh:
jika input jumlah data 4
maka input nilai data sebanyak 4 kali
contoh:
masukan nilai 1 = 3
masukan nilai 2 = 4
masukan nilai 3 = 7
masukan nilai 4 = 9
data.append(nilai) agar menambahkan nilai yang di ketik di list akhir data
Hasil: setelah loop selesai, data berisi semua angka yang dimasukkan pengguna dalam urutan input
Memanggil metode sort() pada list data
sort() mengurutkan list di tempat dari nilai terkecil ke terbesar secara default
for d in data: iterasi melalui setiap elemen di data (yang sudah terurut)
print(d) menampilkan setiap bilangan di baris baru, sehingga pengguna melihat daftar bilangan dari terkecil ke terbesar.
