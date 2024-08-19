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



**Persyaratan**

Membutuhkan python versi 3.12.3, bisa di pasang untuk windows, linux, maupun Mac Os.

[Download Python](https://www.python.org/downloads/release/python-3123/)

Membutuhkan version control git, digunakan untuk mengkloning project ke folder produksi, atau bisa unduh file zip repositori ini secara manual.

[Download GIT di sini(https://git-scm.com/downloads) lalu install. ( TANPA GIT HARUS DOWNLOAD FILE ZIP )


Checking, pastikan perintah ini bisa di jalankan di terminal setelah installasi.

``python --version
dan perintah
git --version``


Jika baru install Python, wajib menginstall pustaka virtual ENV. Jalankan perintah ini di terminal untuk menginstall env.
``pip install virtualenv``





**Salin file ke folder produksi atau bisa download manual**

``git clone https://github.com/NetzkuOfficial/notif-tg.git``




- Jangan lupa edit bagian daftar_id.txt 
- Tambahkan semua kredensial telegram di file .env


**Cara mendapatkan app_id dan app_has** 

[https://www.youtube.com/watch?v=b3v4iiPHouk](https://www.youtube.com/watch?v=b3v4iiPHouk)

*Cara mendapatkann token telegram baru**

[https://www.youtube.com/watch?v=zTEzsP6EMww](https://www.youtube.com/watch?v=zTEzsP6EMww)


**Pastikan terminal sudah masuk ke folder proyek**

``python -m venv ryan-id``

``ryan-id\Scripts\Activate``

``pip install -r requirements.txt``

``python main.py``

Masukan kode verifikasi yang di kirim ke telegram anda.
Masukan password telegram anda jika ada.
Bot running......
Untuk menghentikan bot telegram, pada terminal ketik CTRL + C...


Untuk menjalankan ulang program:
Masuk ke directory produksi sebelumnya, edit address tambahkann cmd di depan nya lalu enter.


``ryan-id\Scripts\Activate``

``python main.py``


_Program ini di rancang dengan menggunakan library telegram telethon, 
dan mempunyai 2 sesi aktif di dalamnya yaitu sesi bot dan sesi pengguna. Bagi akun yang memasnag bot ini, maka program dapat melihat semua pesan yang masuk ke akun telegram kamu namun program ini akan mengabaikanya kecuali pesan yang mengandung kode identifikasi._

