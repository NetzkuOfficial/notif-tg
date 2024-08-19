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


**Install Software ini terlebih dahulu**

- Download python versi 3.12.3 khusus windows [Download di sini](https://www.python.org/downloads/release/python-3123/) Sesuaikan versi os 64 bit atau 32 bit Dan install
- Download Untuk windows [Download Git di sini](https://git-scm.com/downloads) lalu install. ( TANPA GIT HARUS DOWNLOAD FILE ZIP )

**Setelah installasi periksa python dengan perintah berikut**

python --version ( enter ) akan muncul versi python
git --version (enter ) akan muncul versi git

===== JIKA TIDAK MUNCUL VERSION atau PERINTAH TIDAK DI KENALI BERARTI INSTALLSAI GAGAL ATAU TIDAK BENAR ==== 


**Install Pustaka lingkungan virtual pada python desktop, jalankan perintah berikut**
`pip install virtualenv`

Pastikan installasi berhasil, kalau gak berhasil jangan lanjut karena gak akan bisa lanjut tanpa itu.









**Buat akun di my.telegram.org**

Tujuanya untuk mendapatkan app_id dan app_hash, kalau belum paham cara membuat akun di sana bisa refer ke video youtube ini [https://www.youtube.com/watch?v=b3v4iiPHouk](https://www.youtube.com/watch?v=b3v4iiPHouk)
Catat dan simpan app_id dan app_hash, dan jangan sampai tersebar karena orang lain dapat menggunakanya untuk mengendalikan akun telegram anda.
.
.
.
.

**Buat akun bot baru di botfather**

Tujuanya untuk mendapatkan kode bot token, penting bot token di sini. Untuk cara membuatnya bisa lihat video berikut ini [https://www.youtube.com/watch?v=zTEzsP6EMww](https://www.youtube.com/watch?v=zTEzsP6EMww)
Setlah bot jadi jangan lupa kirim pesan /start untuk pertama kali nya ke bot tersebut.

=== DARI HASIL DI ATAS ANDA SUDAH MENDAPATKAN APP_ID, APP_HASH, DAN BOT TOKEN__
Kalau masih belum dapat ke 3 kode yang sangat krusial tersebut sebaiknya jangan lanjut, selesaikan dulu tahapan itu baru lanjut ke tahap berikutnya. 
.
.
.

**Kloning program dan repositori github nya**

Kembali ke CMD tadi kemudian copy paste printah di bawah ini lalu enter.
`git clone https://github.com/NetzkuOfficial/notif-tg.git`

JIKA SUDAH PUNYA FILE ZIP NYA GAK PRELU DI KLONING LAGI.

Pastikan proses kloning berhasil bukan ERROR, kalau error sebaiknya selesaikan dulu proses kloning dan permasalahanya.
Kalau sudah berhasil maka bisa lanjut ke tahap berikutnya.

Arahkan cmd ke folder baru yang sudah di kloning sebelumnya gunakan perintah 
`cd notif-tg` enter untuk menjalankan.
.
.
.


JIKA SUDAH PUNYA FILE NYA...
-Extrax dalam sebuah folder
-Masuk ke Folder tersebut dengan windows explorer
-Habis itu address nya di depan tambahkan teks cmd
.
.
.
.



**Mengedit file penting yang wajib banget**

Pastikan anda menghidupkan tampilkan file tersembunyi pada windows explorer, untuk dapat melihat file .env file ini adalah konfigurasi.
Masukan app_id, app_hash, nomor hp dengan kode negara, serta bot token ke file ini. Saya sudah menepatkan variabel di dalamnya tinggal isi di samping.
Setelah mengisi jangan lupa di simpan ....

Edit kata=kata pada file daftar_id.txt bila lebih dari satu, tambahkan setiap baris untuk membantu susunanya.

.
.
.
.

**Membuat lingkungan virtual baru**

Khusus windows, balik lagi ke terminal cmd yang sudah terbuka sebelumnya. Ketikan perintah berikut lalu enter....
`python -m venv ryan`

Tunggu 10 detik atau 50 detik maka lingkungan virtual baru akan berhasil di baut, jika ada error silakan di periksa dulu  dan perbaiki.
Ingat gak bisa lanjut kalau error. Ganti nama ryan dengan nama lingkungan anda sendiri.

Kemudian jalankan lingkungan tersebut dengan mengetik 
`\ryan\Scripts\Activate`

Pastikan berhasil memasuki lingkungan virtual baru, next selanjutnya install semu defensi pada file requiremets.txt kode installasi berikut ini.
`pip install -r requirements.txt`
.
.
.


==== SELESAI KONFIGURASI BERHASIL DI JALANKAN ====

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


_Program ini di rancang dengan menggunakan library telegram telethon, 
dan mempunyai 2 sesi aktif di dalamnya yaitu sesi bot dan sesi pengguna. Bagi akun yang memasnag bot ini, maka program dapat melihat semua pesan yang masuk ke akun telegram kamu namun program ini akan mengabaikanya kecuali pesan yang mengandung kode identifikasi._

