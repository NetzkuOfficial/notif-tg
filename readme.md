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
- Setelah itu, ketik `cd notif-tg` lalu enter, ini akan memasuki folder target.
- Biarkan CMD tetap terbuka, sementara itu ikuti langkah berikut ini


**Edit bagian konfigurasi**
1. Buka web browser dan masuk ke [my.telegram.org](https://my.telegram.org) buat sebuah apps baru, pilih nama bebas, jenis apps nya web apps.
2. Setelah membuat klik Api development tools salin kode api id, api hash lalu tambahkan di file .env
3. Masuk ke telegram, buat bot baru untuk mendapatkan bot token. Ikuti panduan cara buat bot [https://www.youtube.com/watch?v=zTEzsP6EMww](https://www.youtube.com/watch?v=zTEzsP6EMww)
4. Tambahkan lagi kode token bot yang di dapatkan pada file .env
5. Edit kata kunci yang mau di kloning pesan nya tambahkan per baris pada file daftar_id.txt

**Menjalankan bot dan membuat lingkungan virtual**
Untuk mencegah agar tidak konflik bila ingin menjalankan lebih dari satu bot dalam satu sistem yang sama kita wajib menggunakan virtual environment.
Untuk menggunakan virtual environtment, pertama kali banget nih ketika baru install python gitu kamu harus pasang virtual environment Caranya jalankan kode ini di terminal yang sama tadi.
`python -m pip install venv`

!!Warning, installasi virtual env cukup sekali yah pada devices windows yang sama. Setelah installasi python, git, dan venv gak perlu lagi di install dari awal. Kalau program ke hapus cukup lanjutkan pada tahapan git clone doang di atas.

NEXT : Membuat virtual ENV pada windows dan menginstalll depensi. 
Ketik `python venv -m venv nama_lingkungan` lalu enter sampai selesai kelaau sudah selesai.

LANJUT : Menginstall paket depensi ke dalam lingkungan virtual 
Ketik `pip install -r requirements.txt` Tunggu sampai proses installasi selesai yah.

**Menjalankan program**
Ingat pertama kali menjalankan program kamu akan di minta untuk memasukan kode verifikasi yang di kirim oleh telegram ke akun mu. Ini hanya untuk pertama kali saat membuat session telethon yah.
Saat di jalankan kedua kali, kamu tidak akan di minta untuk kode OTP ataupun password.

Untuk menjalankan program, kapanpun dan di manapun pada terminal yang sama. Gunakan perintah 
`python main.py`

Akan di minta memasukan kode verifikasi masukan.
Akan di minta memasukan password telegram masukan.
Done bot running......

Agar bot berjalan terus menerus 24 jam non stop mohon jangan di matikan terminal cmd nya, dan jangan matikan PC/desktop windows yah. 
Atau bisa juga di pasang pada server lain usahakan server yang trusted, kalau mau aman bikin sendiri server nya pake STB bekas buat kantor.

Untuk menghentikan program pada cmd ketik CTRL + C, program akan berhenti.



__Program ini di rancang dengan menggunakan library telegram telethon, 
dan mempunyai 2 sesi aktif di dalamnya yaitu sesi bot dan sesi pengguna. Bagi akun yang memasnag bot ini, maka program dapat melihat semua pesan yang masuk ke akun telegram kamu namun program ini akan mengabaikanya kecuali pesan yang mengandung kode identifikasi._

