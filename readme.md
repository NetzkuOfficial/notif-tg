Sebuah bot telegram simple sederhana untuk meneruskan setiap pesan masuk yang di terima oleh akun telegram kita melalui sebuah bot dengan teknik filtering.
Program ini akan membaca daftar_id.txt dan melihat teks filter yang di simpan per baris, tambahkan teks filer jika ingin menambahkan.
Ketika ada pesan masuk ke akun kita yang mengandung minimal 1 baris id filter maka bot akan meneruskan pesan tersebut ke akun kita.

#Tujuan

Tujuan yang ingin di capai adalah untuk mendapatakn notifikasi alert apabila ada seorang, grup, maupun channel mengirimkan pesan dengan  di sertai ID filter.
Akun telegram kita juga akan menerima notifikasi, serta pesan tersebut melalui bot telegram. 

Cara ini lebih efektif untuk mendapatkan semua jenis pesan masuk yang mengandung sebuah kata daripada harus mencari nya di berbagai obrolan. 
Saat ini telegram merupakan aplikasi dengan jumlah list obrolan terbanyak yang pernah ada, dan ada ribuan pesan per hari di broadcast oleh grup/channel.
Kita yang hanya ingin mengambil/melihat pesan tertentu akan kesulitan mencari nya karena tertimpa oleh pesan lain..

Fitur pencarian telegram masih memungkinkan untuk memfilter dan mencari data yang tepat, akan tetapi keluar masuk setiap obrolan masih menjadi sebuah kerumitan.
Dengan ada nya bot ini, kita hanya perlu mengscroll satu obrolan saja untuk melihat daftar teks mana yang di kirimkan dan berisi ID yang identik.


**Cara memasang khusus windows**
- Download python versi 3.12.3 khusus windows [Download di sini](https://www.python.org/downloads/release/python-3123/) Sesuaikan versi os 64 bit atau 32 bit Dan install
- Download Untuk windows [Download Git di sini](https://git-scm.com/downloads) Dan install
- Masuk ke folder manapun di dekstop PC menggunakan Windows Explorer, misal masuk ke folder Downloads
- Lalu edit address URL tambahkan kata cmd contoh `cmd C:\Users\user\Downloads` Akan terbuka terminal CMD
- Kemudian ketik perintah `git clone https://github.com/NetzkuOfficial/notif-tele.git` dan tunggu sampe proses kloning selesai.
- Setelah itu, ketik `cd notif-tele` lalu enter, ini akan memasuki folder target.
- Perintah selanjutnya ketik `pip install requirements.txt` Tunggu sampai proses installasi selesai yah.
- Biarkan CMD tetap terbuka, sementara itu ikuti langkah berikut ini


**Edit bagian konfigurasi**
1. Buka web browser dan masuk ke [my.telegram.org](https://my.telegram.org) buat sebuah apps baru, pilih nama bebas, jenis apps nya web apps.
2. Setelah membuat klik Api development tools salin kode api id, api hash lalu tambahkan di file .env
3. Masuk ke telegram, buat bot baru untuk mendapatkan bot token. Ikuti panduan cara buat bot [https://www.youtube.com/watch?v=zTEzsP6EMww](https://www.youtube.com/watch?v=zTEzsP6EMww)
4. Tambahkan lagi kode token bot yang di dapatkan pada file .env


