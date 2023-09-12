Nama    :   Dhemas Wicaksono Nugroho 
NPM     :   2206030786
Kelas   :   PBP E

Tautan aplikasi adaptable: https://cloudstrifeswords.adaptable.app/main/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
a.  Membuat sebuah proyek django baru:
    Pertama, saya membuat repository baru di github dan membuat direktori lokal. Kemudian, saya menghubungkan direktori lokal dengan repository github yang tadi dibuat. Kemudian menyiapkan dependancies dalam berkas requirements.txt, dan menginstall atau memasang dependancies dengan menyalakan virtual environment dan menjalankan perintah 'pip install -r requirements.txt' pada command prompt direktori. Lalu membuat proyek django dengan nama Tugas_2 dengan perintah 'django-admin startproject shopping_list .'
    
b.  Membuat aplikasi dengan nama main pada proyek tersebut.
    Saya menambahkan '*' pada ALLOWED_HOSTS di settings.py untuk keperluan deployment dan menambahkan berkas gitignore. Lalu, untuk membuat aplikasi baru bernama main dalam proyek, saya menjalankan perintah 'python manage.py startapp main' pada command prompt.

c.  Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    Mendaftarkan aplikasi main pada proyek dengan cara menambahkan 'main' dalam variabel INSTALLED_APPS pada berkas settings.py

d.  Membuat model pada aplikasi main.
    Membuat direktori baru bernama templates di dalam direktori aplikasi main. Kemudian, di dalam direktori templates, membuat berkas baru bernama main.html dan isi berkas dengan model yang saya mau.

e.  Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML.
    Setelah membuka berkas views.py, saya mengimport render dari django.shortcuts dengan cara 'from django.shortcuts import render'. Lalu menambahkan fungsi show_main di bawah import. Lalu, saya membuat dictionary weapon_data berisi data - data yang saya inginkan dan dictionary context yang berisi 3 keys yaitu name, class, dan weapon_data yang berisi value nama, kelas, dan variabel dictionary weapon_data yang sudah saya buat sebelumnya. Kemudian fungsi show_main mereturn fungsi render, seperti ini:\
    ...
    return render(request, "main.html", context)
    ...
    Ini berguna untuk me-render tampilan main.html dengan menggunakan fungsi render. Fungsi render mengambil tiga argumen:
    request     :   Ini adalah objek permintaan HTTP yang dikirim oleh pengguna.
    main.html   :   Ini adalah nama berkas template yang akan digunakan untuk me-render tampilan.
    context     :   Ini adalah dictionary yang berisi data yang akan diteruskan ke tampilan untuk digunakan dalam penampilan dinamis.

    Kemudian, saya memodifikasi template di berkas main.html di direktori templates dengan mengubah kode yang sebelumnya dibuat secara statis menjadi kode django yang sesuai.

f.  Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    Pertama, membuat berkas berkas urls.py di dalam direktori main. dan mengisinya dengan kode:

    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]

    Lalu, membuka berkas urls.py di dalam direktori proyek, bukan yang ada di dalam direktori aplikasi main lalu meng-Impor fungsi include dari django.urls. 
    ...
    from django.urls import path, include
    ...
    Dan menambahkan rute URL seperti berikut untuk mengarahkan ke tampilan main di dalam variabel urlpatterns.
    ...
    path('main/', include('main.urls')),
    ...

g.  Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat.
    Melakukan deployment dengan cara memilih new app dan hubungkan adaptable dengan repository yang sudah dibuat tadi. Kemudian, memilih Python App Template sebagai template deployment dan PostgreSQL sebagai tipe basis data yang akan digunakan. Lalu, sesuaikan versi python dengan spesifikasi aplikasi dan pada bagian start command, memasukkan perintah Pada bagian Start Command memasukkan 'perintah python manage.py migrate && gunicorn Tugas_2.wsgi'. Kemudian mencentang bagian HTTP Listener on PORT dan klik Deploy App untuk memulai proses deployment aplikasi.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html!

Client Request     ----->          Django        
            (HTTP Request)                     Web Server    
                                                        
                            |
                            |
                            v
                                        
                        Django View    
                        (views.py)     
                                        
                            |
                            |
                            v
                                        
                            Model Data     
                        (models.py)   
                                        
                            |
                            |
                            v
                                        
                        HTML Template  
                        (HTML File)    
                                        
                            |
                            |
                            v
                                        
                        Server Response 
                        (HTTP Response) 
                                        
                            |
                            |
                            v
                                        
                        Client Browser

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
--> Virtual environment digunakan untuk mengisolasi proyek Python, sehingga kita dapat mengelola dependensi dan paket Python yang spesifik  untuk proyek tersebut tanpa mengganggu instalasi global Python di sistem. Berikut adalah beberapa alasan mengapa menggunakan virtual environment:
    
a.  Isolasi Proyek: 
    Dengan virtual environment, kita dapat membuat lingkungan yang terisolasi untuk setiap proyek yang kita kerjakan. Ini membantu mencegah konflik antara dependensi proyek yang berbeda. Setiap proyek dapat memiliki versi yang berbeda dari paket yang sama tanpa masalah.

b.  Manajemen Dependensi: 
    Virtual environment memungkinkan kita menginstal, memperbarui, dan menghapus paket Python dengan mudah hanya untuk proyek tertentu. Ini membuat manajemen dependensi menjadi lebih mudah daripada mengelola semuanya secara global.

c.  Kebersihan: 
    Menggunakan virtual environment membuat sistem lebih bersih dan terorganisir. Kita tidak akan membanjiri instalasi global Python dengan paket yang mungkin hanya diperlukan oleh satu atau dua proyek.

d.  Portabilitas: 
    Kita dapat dengan mudah membagikan atau menggandakan proyek dengan semua dependensinya dalam satu virtual environment. Ini membuatnya lebih mudah untuk bekerja dengan tim atau memindahkan proyek ke lingkungan lain.

Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, dengan menggunakan virtual environment, kita dapat memastikan bahwa setiap proyek Django memiliki lingkungan yang terisolasi dengan dependensi yang sesuai, menjaga kebersihan dan konsistensi instalasi kita. 

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya!
--> MVC, MVT, dan MVVM adalah tiga pola desain arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi perangkat lunak. Mereka memiliki beberapa persamaan dalam konsep arsitektur, tetapi ada perbedaan kunci dalam cara mereka diimplementasikan. Di bawah ini adalah penjelasan singkat tentang ketiganya beserta perbedaannya:

MVC (Model-View-Controller):

Model --> Ini mewakili data dan logika bisnis aplikasi. Model mengelola data, perubahan pada data, serta logika untuk memanipulasi data tersebut.
View --> Ini adalah tampilan atau antarmuka pengguna yang menampilkan informasi dari model kepada pengguna. View bertanggung jawab untuk menampilkan data dengan cara yang sesuai untuk pengguna.
Controller --> Ini berfungsi sebagai pengendali antara Model dan View. Controller menangani permintaan pengguna, memproses input, mengubah Model jika diperlukan, dan mengatur tampilan yang akan ditampilkan kepada pengguna.
Perbedaan Utama --> MVC adalah pola arsitektur yang digunakan terutama dalam pengembangan aplikasi berbasis desktop dan web tradisional. Dalam MVC, Controller bertindak sebagai perantara antara Model dan View.

MVT (Model-View-Template):

Model --> Seperti dalam MVC, Model ini berfungsi untuk mengelola data dan logika bisnis.
View --> Ini juga mirip dengan View dalam MVC, bertanggung jawab untuk menampilkan data kepada pengguna.
Template --> Ini adalah komponen unik dalam MVT yang mengelola tampilan dan tata letak. Template menghasilkan tampilan yang akhir kepada pengguna berdasarkan data dari Model dan instruksi dari View.
Perbedaan Utama --> MVT adalah variasi dari MVC yang ditemukan dalam kerangka kerja Django, yang banyak digunakan untuk pengembangan web berbasis Python. Perbedaan utamanya adalah penggunaan Template untuk menghasilkan tampilan daripada menggunakan View langsung.

MVVM (Model-View-ViewModel):

Model -->  Seperti dalam MVC dan MVT, Model ini mewakili data dan logika bisnis aplikasi.
View -->  View dalam MVVM adalah tampilan yang menampilkan data dan mengirimkan tindakan pengguna ke ViewModel.
ViewModel --> Ini adalah komponen unik dalam MVVM yang bertindak sebagai perantara antara Model dan View. ViewModel mengelola logika tampilan, mengonversi data dari Model ke format yang dapat ditampilkan oleh View, dan menangani tindakan pengguna yang diteruskan dari View ke Model.
Perbedaan Utama --> MVVM adalah pola arsitektur yang sering digunakan dalam pengembangan aplikasi berbasis klien, terutama dalam pengembangan aplikasi berbasis mobile dan desktop. ViewModel adalah elemen penting dalam MVVM yang memisahkan logika tampilan dari View.