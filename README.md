## Nama    :   Dhemas Wicaksono Nugroho
## NPM     :   2206030786
## Kelas   :   PBP E##

Tautan aplikasi adaptable: https://cloudstrifeswords.adaptable.app/main/

### **TUGAS 2**

1. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**

a.  **Membuat sebuah proyek django baru:**
    Pertama, saya membuat repository baru di github dan membuat direktori lokal. Kemudian, saya menghubungkan direktori lokal dengan repository github yang tadi dibuat. Kemudian menyiapkan dependancies dalam berkas requirements.txt, dan menginstall atau memasang dependancies dengan menyalakan virtual environment dan menjalankan perintah 'pip install -r requirements.txt' pada command prompt direktori. Lalu membuat proyek django dengan nama Tugas_2 dengan perintah 'django-admin startproject shopping_list .'
    
b.  **Membuat aplikasi dengan nama main pada proyek tersebut.**
    Saya menambahkan '*' pada ALLOWED_HOSTS di settings.py untuk keperluan deployment dan menambahkan berkas gitignore. Lalu, untuk membuat aplikasi baru bernama main dalam proyek, saya menjalankan perintah 'python manage.py startapp main' pada command prompt.

c.  **Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**
    Mendaftarkan aplikasi main pada proyek dengan cara menambahkan 'main' dalam variabel INSTALLED_APPS pada berkas settings.py

d.  **Membuat model pada aplikasi main.**
    Membuat direktori baru bernama templates di dalam direktori aplikasi main. Kemudian, di dalam direktori templates, membuat berkas baru bernama main.html dan isi berkas dengan model yang saya mau.

e.  **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML.**
    Setelah membuka berkas views.py, saya mengimport render dari django.shortcuts dengan cara 'from django.shortcuts import render'. Lalu menambahkan fungsi show_main di bawah import. Lalu, saya membuat dictionary weapon_data berisi data - data yang saya inginkan dan dictionary context yang berisi 3 keys yaitu name, class, dan weapon_data yang berisi value nama, kelas, dan variabel dictionary weapon_data yang sudah saya buat sebelumnya. Kemudian fungsi show_main mereturn fungsi render, seperti ini:\
    ...
    return render(request, "main.html", context)
    ...
    Ini berguna untuk me-render tampilan main.html dengan menggunakan fungsi render. Fungsi render mengambil tiga argumen:
    request     :   Ini adalah objek permintaan HTTP yang dikirim oleh pengguna.
    main.html   :   Ini adalah nama berkas template yang akan digunakan untuk me-render tampilan.
    context     :   Ini adalah dictionary yang berisi data yang akan diteruskan ke tampilan untuk digunakan dalam penampilan dinamis.

    Kemudian, saya memodifikasi template di berkas main.html di direktori templates dengan mengubah kode yang sebelumnya dibuat secara statis menjadi kode django yang sesuai.

f.  **Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**
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

g.  **Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat.**
    Melakukan deployment dengan cara memilih new app dan hubungkan adaptable dengan repository yang sudah dibuat tadi. Kemudian, memilih Python App Template sebagai template deployment dan PostgreSQL sebagai tipe basis data yang akan digunakan. Lalu, sesuaikan versi python dengan spesifikasi aplikasi dan pada bagian start command, memasukkan perintah Pada bagian Start Command memasukkan 'perintah python manage.py migrate && gunicorn Tugas_2.wsgi'. Kemudian mencentang bagian HTTP Listener on PORT dan klik Deploy App untuk memulai proses deployment aplikasi.

2. **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html!**

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

3. **Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
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

4. **Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya!**
--> MVC, MVT, dan MVVM adalah tiga pola desain arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi perangkat lunak. Mereka memiliki beberapa persamaan dalam konsep arsitektur, tetapi ada perbedaan kunci dalam cara mereka diimplementasikan. Di bawah ini adalah penjelasan singkat tentang ketiganya beserta perbedaannya:

**MVC (Model-View-Controller):**

**Model -->** Ini mewakili data dan logika bisnis aplikasi. Model mengelola data, perubahan pada data, serta logika untuk memanipulasi data tersebut.
**View -->**Ini adalah tampilan atau antarmuka pengguna yang menampilkan informasi dari model kepada pengguna. View bertanggung jawab untuk menampilkan data dengan cara yang sesuai untuk pengguna.
**Controller -->** Ini berfungsi sebagai pengendali antara Model dan View. Controller menangani permintaan pengguna, memproses input, mengubah Model jika diperlukan, dan mengatur tampilan yang akan ditampilkan kepada pengguna.
Perbedaan Utama --> MVC adalah pola arsitektur yang digunakan terutama dalam pengembangan aplikasi berbasis desktop dan web tradisional. Dalam MVC, Controller bertindak sebagai perantara antara Model dan View.

**MVT (Model-View-Template):**

**Model -->** Seperti dalam MVC, Model ini berfungsi untuk mengelola data dan logika bisnis.
**View -->** Ini juga mirip dengan View dalam MVC, bertanggung jawab untuk menampilkan data kepada pengguna.
**Template -->** Ini adalah komponen unik dalam MVT yang mengelola tampilan dan tata letak. Template menghasilkan tampilan yang akhir kepada pengguna berdasarkan data dari Model dan instruksi dari View.
**Perbedaan Utama -->** MVT adalah variasi dari MVC yang ditemukan dalam kerangka kerja Django, yang banyak digunakan untuk pengembangan web berbasis Python. Perbedaan utamanya adalah penggunaan Template untuk menghasilkan tampilan daripada menggunakan View langsung.

**MVVM (Model-View-ViewModel):**

**Model -->**  Seperti dalam MVC dan MVT, Model ini mewakili data dan logika bisnis aplikasi.
**View -->**  View dalam MVVM adalah tampilan yang menampilkan data dan mengirimkan tindakan pengguna ke ViewModel.
**ViewModel -->** Ini adalah komponen unik dalam MVVM yang bertindak sebagai perantara antara Model dan View. ViewModel mengelola logika tampilan, mengonversi data dari Model ke format yang dapat ditampilkan oleh View, dan menangani tindakan pengguna yang diteruskan dari View ke Model.
**Perbedaan Utama -->** MVVM adalah pola arsitektur yang sering digunakan dalam pengembangan aplikasi berbasis klien, terutama dalam pengembangan aplikasi berbasis mobile dan desktop. ViewModel adalah elemen penting dalam MVVM yang memisahkan logika tampilan dari View.




### **TUGAS 3**


1.  **Apa perbedaan antara form POST dan form GET dalam Django?**
    *   **Form POST (HTTP POST Method):**
        - Keamanan 
        Metode POST lebih aman dibandingkan GET. Data dikirimkan sebagai bagian dari permintaan HTTP, yang tidak terlihat dalam URL. Ini berarti data tidak terlihat oleh pengguna yang melihat URL dan tidak mudah terpantau atau disadap oleh pihak ketiga.
        - Jumlah Data 
        Kita dapat mengirimkan data yang lebih besar dengan metode POST. Karena data dikirim sebagai bagian dari body permintaan HTTP, Anda tidak dibatasi oleh panjang URL seperti pada metode GET. Ini berguna ketika Anda perlu mengirimkan data yang sangat besar, misalnya, file upload.
        - Kegunaan 
        Metode POST umumnya digunakan ketika ingin mengirimkan data yang akan mempengaruhi atau mengubah sumber daya di server, seperti ketika kita mengirimkan data formulir untuk membuat, mengedit, atau menghapus sesuatu di aplikasi web. Ini juga digunakan ketika ingin menyimpan data sensitif, seperti kata sandi.
    *   **Form GET (HTTP GET Method):**
        - Visibilitas Data 
        Data yang dikirim dengan metode GET ditampilkan dalam URL sebagai query string. Ini membuat data terlihat di baris alamat browser. Oleh karena itu, metode GET kurang aman jika mengirimkan data sensitif karena data tersebut dapat dilihat oleh semua orang yang melihat URL.
        - Jumlah Data
        Metode GET memiliki batasan panjang URL yang terbatas, sehingga hanya cocok untuk mengirimkan data kecil atau parameter pencarian. Jika kita mencoba mengirimkan data besar dengan metode GET, kita dapat mengalami masalah batasan panjang URL.
        - Kegunaan
        Metode GET biasanya digunakan untuk mengambil data dari server tanpa mempengaruhi sumber daya di server. Ini cocok untuk operasi pencarian atau tautan yang mengarah ke halaman tertentu dengan parameter yang digunakan untuk menyesuaikan konten.Kegunaan: Metode GET biasanya digunakan untuk mengambil data dari server tanpa mempengaruhi sumber daya di server. Ini cocok untuk operasi pencarian atau tautan yang mengarah ke halaman tertentu dengan parameter yang digunakan untuk menyesuaikan konten.
    
2.  **Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?**
    -   Tujuan Utama:
        *   XML (eXtensible Markup Language)
            - XML dirancang untuk mendefinisikan struktur data.
            - Digunakan untuk pertukaran data terstruktur antara aplikasi.
            - XML adalah format dokumen yang dapat diurai oleh manusia dan mesin.
        *   JSON (JavaScript Object Notation)
            - JSON diciptakan untuk pertukaran data antara bahasa pemrograman.
            - Digunakan sebagai format data ringan yang mudah dipahami oleh manusia dan mudah diurai oleh mesin.
            = Sering digunakan dalam pengembangan aplikasi web dan API RESTful.
        *   HTML (HyperText Markup Language):
            - HTML digunakan untuk membangun struktur dan tampilan halaman web.
            - Didesain untuk mengorganisir dan menampilkan konten di browser web.
            - HTML adalah bahasa markup yang terkait erat dengan tampilan dan presentasi.
    -   Tipe Data:
        *   XML
            - Tidak memiliki tipe data bawaan, sehingga Anda harus mendefinisikan tipe data kustom.
        *   JSON
            - Mendukung tipe data dasar seperti string, angka, boolean, array, dan objek.
            - Struktur data yang lebih terstruktur dibandingkan dengan XML.
        *   HTML:
            - Terutama digunakan untuk mengatur dan menampilkan konten, bukan untuk menyimpan data dalam bentuk mentah.
    -   Ukuran Data:
        *   XML
            - Tendensinya memiliki overhead dalam hal ukuran file karena menggunakan tag yang lebih banyak.
        *   JSON
            - Lebih ringan dan memiliki overhead yang lebih rendah dibandingkan dengan XML.
        *   HTML:
            - Terutama digunakan untuk mengatur tampilan dan konten halaman web.

3.  **Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**

    JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena ringan, mudah dibaca oleh manusia, mudah diurai oleh mesin, mendukung struktur data yang terstruktur, memiliki dukungan untuk tipe data dasar, dan terintegrasi dengan teknologi web serta berbagai platform.

4.  **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
    1.  **Membuat input form untuk menambahkan objek model pada app sebelumnya.**
        Pertama, saya membuat class productForm dalam file baru yaitu forms.py dalam direktori main. Class ini untuk menunjukkan model yang digunakan untuk form dan menunjukkan field dari model Product yang digunakan untuk form. 
        Kemudian saya mengimport class productForm dan fungsi reverse dari django ke file views.py. Lalu, membuat fungsi baru dengan nama create_product yang menerima parameter request dan menghasilkan formulir yang dapat menambahkan data produk secara otomatis ketika data di-submit dari form. 

    2.  **Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.** dan       **Membuat routing URL untuk masing-masing views yang telah ditambahkan.**
        -   fungsi untuk html

            Pertama, saya mengubah sedikit fungsi show_main pada file views.py dengan menambahkan potongan kode 'items = Item.objects.all()' yang berfungsi untuk mengambil seluruh object Product yang tersimpan pada database. Lalu menyimpan variabel items pada dictionary context dengan key "products".
            Lalu, saya mengimport fungsi create_product pada file urls.py yang ada di folder main dan menambahkan path url ke dalam urlpatterns pada urls.py di main untuk mengakses fungsi yang sudah di-import sebelumnya.
            Membuat berkas HTML baru dengan nama create_product.html pada direktori main/templates untuk membuat template form input data.
            Kemudian, memnambahkan kode di main.html untuk menampilkan data produk dalam bentuk table serta tombol "Add New Product" yang akan redirect ke halaman form.
        
        -   fungsi untuk XML dan JSON

            Pertama, saya mengimport django yaitu HttpResponse dan Serializers ke dalam file views.py. Kemudian, membuat fungsi yang menerima parameter request dengan nama show_xml dan show_json dan membuat sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada class Item yang ada pada model. Lalu, menambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML atau JSON dan parameter 'content_type="application/xml"' atau content_type="application/JSON"'. Lalu mengimport fungsi yang sudah dibuat ke dalam urls.py dan menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimport tadi.
        
        -   fungsi untuk XML dan JSON by id

            Pertama, membuka views.py yang ada pada folder main dan membuat sebuah fungsi baru yang menerima parameter request dan id dengan nama show_xml_by_id dan show_json_by_id. Lalu, membuat sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari data dengan id tertentu yang ada pada class Item pada model. Kemudian, membuat return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter content_type dengan value "application/xml" (untuk format XML) atau "application/json" (untuk format JSON).
            <pre>
            '''python
            def show_xml_by_id(request, id):
                data = Product.objects.filter(pk=id)
                return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
            
            def show_xml_by_id(request, id):
                data = Product.objects.filter(pk=id)
                return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
            '''
            </pre>
            Setelah itu, import fungsi yang sudah dibuat ke dalam urls.py dan menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.

5.  **Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.**
    -   screenshot html
        [![Screenshot-39.png](https://i.postimg.cc/jdvC9Ffc/Screenshot-39.png)](https://postimg.cc/GH8cTzqT)
    -   screenshot XML
        [![Screenshot-40.png](https://i.postimg.cc/3Nz752KK/Screenshot-40.png)](https://postimg.cc/2LdgnbbJ)
    -   screenshot JSON
        [![Screenshot-41.png](https://i.postimg.cc/4N5k1Ccf/Screenshot-41.png)](https://postimg.cc/2VVKzKTM)
    -   screenshot XML_by_id
        [![Screenshot-42.png](https://i.postimg.cc/7ZFVGhLf/Screenshot-42.png)](https://postimg.cc/4Y1tjJVg)
    -   screenshot JSON-by_id
        [![Screenshot-43.png](https://i.postimg.cc/yNnDqp2s/Screenshot-43.png)](https://postimg.cc/LqY9LDHb)




### **TUGAS 4**

1.  **Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?**

    UserCreationForm adalah salah satu formulir bawaan yang disediakan oleh Django untuk mengelola proses pendaftaran pengguna dalam aplikasi web. Formulir ini digunakan untuk membuat dan mendaftarkan pengguna baru. Ini termasuk dalam modul django.contrib.auth.forms dan biasanya digunakan bersama dengan modul autentikasi Django.

    -   **Kelebihan**
        1.  Mudah Digunakan: UserCreationForm adalah formulir yang sudah terdefinisi dengan baik dan mudah digunakan. 
        2.  Integrasi yang Baik dengan Model Pengguna: Formulir ini terintegrasi dengan model pengguna bawaan Django (User), yang membuatnya lebih mudah untuk menyimpan informasi pengguna dalam database.
        3.  Validasi Bawaan: Formulir ini mencakup validasi bawaan yang memastikan bahwa pengguna memasukkan informasi yang benar dan sesuai, seperti memeriksa apakah nama pengguna sudah digunakan sebelumnya atau memastikan bahwa kata sandi sesuai dengan aturan keamanan.
        4.  Fleksibilitas: Anda dapat memodifikasi formulir ini atau menambahkan bidang tambahan sesuai dengan kebutuhan Anda. Ini memungkinkan Anda untuk mengkustomisasi proses pendaftaran sesuai dengan aplikasi Anda.
    -   **Kekurangan**
        1.  Tampilan Standar: Formulir ini memiliki tampilan standar yang mungkin tidak cocok dengan desain UI khusus aplikasi yang kita buat. Kita perlu menyesuaikan tampilannya agar sesuai dengan gaya aplikasi kita.
        2.  Bahasa Tertentu: Secara bawaan, formulir ini akan menggunakan bahasa yang terkait dengan konfigurasi Django kita. Jika kita ingin tampilan dan pesan kesalahan dalam bahasa lain, kita perlu melakukan pekerjaan tambahan.
        3.  Keamanan: Meskipun formulir ini menyertakan validasi keamanan bawaan, keamanan sepenuhnya aplikasi juga bergantung pada konfigurasi lainnya, seperti penggunaan HTTPS dan praktik keamanan yang tepat di seluruh aplikasi.

2.  **Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**
    1.  **Autentikasi**
        -   **Deskripsi:** Autentikasi adalah proses verifikasi identitas pengguna. Ini mengonfirmasi apakah pengguna yang mencoba mengakses aplikasi adalah mereka yang mereka klaim. Dalam konteks Django, ini sering melibatkan verifikasi bahwa nama pengguna dan kata sandi yang dimasukkan oleh pengguna cocok dengan informasi yang tersimpan di dalam sistem (misalnya, dalam model User bawaan Django).
        -   **Tujuan:** Autentikasi digunakan untuk memastikan bahwa pengguna yang mencoba mengakses aplikasi adalah pengguna yang sah dan memiliki izin untuk mengaksesnya. Ini adalah langkah pertama dalam mengelola akses ke aplikasi.
    2.  **Otorisasi**
        -   **Deskripsi:** Otorisasi adalah proses menentukan apa yang diizinkan atau tidak diizinkan oleh pengguna yang sudah diautentikasi. Ini melibatkan pengecekan hak akses pengguna terhadap berbagai sumber daya atau fitur dalam aplikasi, seperti halaman web, data, atau fungsi tertentu.
        -   **Tujuan:** Otorisasi digunakan untuk mengontrol apa yang dapat dilakukan oleh pengguna yang sudah diautentikasi. Ini memastikan bahwa pengguna hanya memiliki akses ke bagian-bagian aplikasi yang sesuai dengan peran atau izin mereka, dan mencegah pengguna yang tidak sah mengakses sumber daya atau fitur yang tidak seharusnya mereka akses.
    
    Keduanya penting dalam pengembangan aplikasi web karena mereka bekerja sama untuk menjaga keamanan dan privasi aplikasi. Autentikasi memastikan bahwa pengguna yang masuk adalah mereka yang sah, sementara otorisasi memastikan bahwa mereka hanya memiliki akses ke bagian aplikasi yang sesuai dengan peran atau izin mereka.

3.  **Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**

    Cookies adalah sepotong data kecil yang disimpan di sisi klien (browser) saat pengguna mengunjungi sebuah situs web. Cookies digunakan dalam konteks aplikasi web untuk menyimpan informasi di sisi klien yang dapat digunakan oleh server web untuk mengenali pengguna yang kembali ke situs tersebut. 

    Django memiliki dukungan bawaan untuk mengelola cookies dan sesi pengguna melalui modul django.contrib.sessions. Berikut adalah cara Django menggunakan cookies untuk mengelola data sesi pengguna:

    1.  Memulai Sesi Pengguna

        Ketika seorang pengguna pertama kali mengunjungi situs web Django, sesi pengguna baru akan dimulai secara otomatis. Sebuah cookie khusus dengan ID sesi akan dibuat dan dikirimkan ke peramban pengguna.
        
    2.  Menyimpan Data Sesi

        Saat pengguna melakukan interaksi dengan situs web (misalnya, masuk, menambahkan barang ke keranjang belanja, atau mengisi formulir), Django dapat digunakan untuk menyimpan data sesi pengguna dalam bentuk dictionary Python. Data ini akan dikaitkan dengan ID sesi yang sesuai.
    
    3.  Mengirimkan Cookie Kembali

        Setiap kali pengguna membuat permintaan berikutnya ke situs web, web akan mengirimkan cookie sesi (berisi ID sesi) kembali ke server Django. Ini memungkinkan Django untuk mengidentifikasi sesi pengguna yang sesuai.
    
    4.  Mengambil Data Sesi

        Django akan mengambil ID sesi dari cookie, mencocokkannya dengan sesi yang sesuai di server, dan mengembalikan data sesi pengguna ke dalam aplikasi.
    
    5.  Mengambil Data Sesi

        Dapat menghapus atau mengubah data sesi pengguna sesuai kebutuhan. Setelah pengguna keluar atau sesi berakhir, data sesi dapat dihapus.

4.  **Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**

    Penggunaan cookies dalam pengembangan web memiliki risiko potensial yang harus diwaspadai. Cookies memiliki beberapa risiko keamanan yang perlu dipertimbangkan di antaranya adalah pelacakan pengguna, kebocoran data, Cookie Theft, dan Penggunaan untuk Serangan Cross-Site Scripting (XSS).

5.  **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
    1.  **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.**

        Untuk membuat fungsi registrasi, pertama saya  mengimport UserCreationForm dari django.contrib.auth.forms ke file views.py yang berfungsi untuk impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web. Selanjutnya saya membuat fungsi untuk registrasi yang menerima parameter request pada file views.py yang ada pada subdirektori main. Kemudian, saya membuat file register.html dan mengisinya dengan template tampilan form registrasi yang saya inginkan. Lalu, mengimport fungsi yang sudah dibuat dan menambahkan path url ke urlpatterns untuk dapat mengakses fungsi yang sudah diimpor tadi.

        Untuk membuat fungsi login, saya mengimport function authenticate, login dari django.contrib.auth yang digunakan untuk melakukan autentikasi dan login jika autentikasi berhasil ke dalam file views.py. Kemudian, membuat fungsi login_user yang menerima parameter request. Fungsi ini berfungsi untuk mengautentikasi pengguna yang ingin login. Selanjutnya, saya membuat file login.html pada folder template sesuai dengan tampilan halaman login yang saya inginkan. Lalu, saya mengimport fungsi yang sudah dibuat ke urls.py dan menambahkan path ke urlpatterns.

        Untuk membuat fungsi logout, saya mengimport function logout dari django.contrib.auth ke dalam views.py. Kemudian, membuat fungsi logout_user yang menerima parameter request. Lalu menambahkan tombol logout di halaman main.html. Kemudian mengimport fungsi lout_user ke dalam urls.py dan menambahkan path ke urlspatterns.
    
    2.  **Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.**

        -   akun pertama
            [![Screenshot-45.png](https://i.postimg.cc/d3HBCcwX/Screenshot-45.png)](https://postimg.cc/y3Rcq5JX)
        -   akun Kedua
            [![Screenshot-46.png](https://i.postimg.cc/WpHg0n0Q/Screenshot-46.png)](https://postimg.cc/Bt2j02Yg)
        
    3.  **Menghubungkan model Item dengan User.**

        Pertama, membuka models.py dan menambahkan kode from django.contrib.auth.models import User. Lalu, pada class model Item yang sudah dibuat, tambahkan user = models.ForeignKey(User, on_delete=models.CASCADE) yang berfungsi untuk menghubungkan satu produk dengan satu user melalui sebuah relationship, dimana sebuah produk pasti terasosiasikan dengan seorang user. Kemudian, memodifikasi fungsi create_product pada views.py untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database. Hal tersebut memungkinkan kita untuk memodifikasi terlebih dahulu objek tersebut sebelum disimpan ke database. Selanjutnya, memodifikasi fungsi show_main dengan menambahkan products = Item.objects.filter(user=request.user) berfungsi untuk menampilkan objek Item yang terasosiasikan dengan pengguna yang sedang login. Hal tersebut dilakukan dengan menyaring seluruh objek dengan hanya mengambil Item yang dimana field user terisi dengan objek User yang sama dengan pengguna yang sedang login. Kemudian, melakukan migrasi model. 
    
    4.  **Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.**
        
        Untuk menampikan username, saya mengganti value dari 'name' pada context dalam fungsi show_main menjadi Kode request.user.username berfungsi untuk menampilkan username pengguna yang login pada halaman main. Dan untuk menerapkan cookies, pertama saya mengimport datetime, HttpResponseRedirect, dan  reverse pada file views.py. Kemudian, memodifikasi fungsi login_user dengan menambahkan fungsi untuk menambahkan cookie yang bernama last_login untuk melihat kapan terakhir kali pengguna melakukan login. Lalu, menambahkan kode 'last_login': request.COOKIES['last_login'], pada context pada show_main yang berfungsi menambahkan informasi cookie last_login pada response yang akan ditampilkan di halaman web. Kemudian memodifikasi fungsi logout_user untuk menghapus cookie last_login saat pengguna melakukan logout. Selanjutnya menambahkan informasi sesi terakhir login pada template halaman main.



### **TUGAS 5**

1.  **Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.**

    Element selector dalam CSS digunakan untuk memilih elemen HTML tertentu berdasarkan jenis atau nama elemennya. Setiap elemen HTML memiliki elemen selector yang berbeda, dan penggunaannya bergantung pada kebutuhan desain dan struktur halaman web. Berikut adalah beberapa elemen selector yang umum digunakan beserta manfaat dan waktu yang tepat untuk menggunakannya:

    1.  **Universal Selector (*):**
        -   Manfaat: Universal selector memilih semua elemen pada halaman web.
        -   Kapan digunakan: Sebaiknya digunakan dengan hati-hati karena dapat mempengaruhi semua elemen. Dapat berguna dalam situasi khusus    seperti mereset gaya default browser.
    2.  **Type Selector (Element Selector):**
        -   Manfaat: Memilih semua elemen dengan tipe tertentu (misalnya, <p> untuk paragraf atau <h1> untuk judul level 1).
        -   Kapan digunakan: Cocok untuk merubah gaya elemen spesifik dengan tipe tertentu.
    3.  **Class Selector (.classname):**
        -   Manfaat: Memilih semua elemen yang memiliki atribut class dengan nilai tertentu.
        -   Kapan digunakan: Berguna saat ingin mengaplikasikan gaya yang sama pada beberapa elemen dengan class yang sama.
    4.  **ID Selector (#idname):**
        -   Manfaat: Memilih elemen dengan atribut id tertentu.
        -   Kapan digunakan: Dapat digunakan ketika hanya ada satu elemen dengan ID tertentu pada halaman, dan digunakan untuk mengaplikasikan gaya atau perilaku yang unik pada elemen tersebut.
    5.  **Attribute Selector ([attribute=value]):**
        -   Manfaat: Memilih elemen berdasarkan atribut dan nilai atribut yang spesifik.
        -   Kapan digunakan: Berguna saat ingin mengaplikasikan gaya pada elemen dengan atribut tertentu (misalnya, [type="text"] untuk memilih input teks).
    6.  **Pseudo-Class Selector (:pseudo-class):**
        -   Manfaat: Memilih elemen dalam keadaan tertentu, seperti :hover untuk elemen saat kursor diarahkan padanya.
        -   Kapan digunakan: Digunakan untuk mengubah perilaku elemen dalam keadaan tertentu, seperti saat interaksi pengguna.
    7.  **Pseudo-Element Selector (::pseudo-element):**
        -   Manfaat: Memungkinkan untuk memilih dan mengubah bagian tertentu dari elemen, seperti ::before untuk menambahkan konten sebelum elemen.
        -   Kapan digunakan: Digunakan untuk menambahkan elemen tambahan atau mengubah tampilan elemen tertentu.
    8.  **Descendant Selector (ancestor descendant):**
        -   Manfaat: Memilih elemen yang merupakan turunan (child) dari elemen lain.
        -   Kapan digunakan: Berguna saat ingin mengaplikasikan gaya pada elemen-elemen yang berada dalam elemen lain, misalnya, styling untuk elemen-elemen dalam tabel.
    9.  **Child Selector (parent > child):**
        -   Manfaat: Memilih elemen anak yang langsung di dalam elemen induk tertentu.
        -   Kapan digunakan: Digunakan ketika ingin mengaplikasikan gaya atau perilaku pada elemen-elemen anak yang langsung berada di dalam elemen induk tertentu.
    10. **Adjacent Sibling Selector (prev + next):**
        -   Manfaat: Memilih elemen yang berada sejajar dengan elemen lain dan memiliki elemen induk yang sama.
        -   Kapan digunakan: Berguna saat ingin mengaplikasikan gaya atau perilaku pada elemen yang berada sejajar dengan elemen lain dalam dokumen.

2.  **Jelaskan HTML5 Tag yang kamu ketahui.**

    1.  '<header>': Tag ini digunakan untuk mendefinisikan bagian atas (header) dari sebuah halaman web atau bagian dari konten yang mewakili kepala dari sebuah bagian atau artikel.
    2.  '<nav>': Tag ini digunakan untuk mengelompokkan tautan navigasi dalam sebuah elemen, seperti menu navigasi utama atau menu samping.
    3.  '<main>': Tag ini digunakan untuk mengandung konten utama dari halaman web. Biasanya, hanya ada satu elemen <main> dalam satu halaman.
    4.  '<section>': Tag ini digunakan untuk mengelompokkan konten terkait dalam sebuah bagian, seperti artikel dalam sebuah berita.
    5.  '<footer>': Tag ini digunakan untuk mendefinisikan bagian bawah (footer) dari sebuah halaman web atau bagian dari konten yang mewakili penutup dari sebuah bagian atau artikel.
    6.  '<input>' (dengan berbagai jenis, seperti text, password, email, checkbox, dll.): Tag ini digunakan untuk membuat berbagai jenis elemen input dalam formulir.

3.  **Jelaskan perbedaan antara margin dan padding.**

    Margin dan padding adalah dua properti penting dalam CSS yang digunakan untuk mengatur tata letak elemen dalam halaman web. Mereka memiliki perbedaan utama dalam cara mereka memengaruhi ruang di sekitar dan di dalam elemen HTML. Berikut adalah perbedaan antara margin dan padding:

    1.  Margin
        -   Fungsi: Margin adalah jarak antara elemen dan elemen-elemen lain di sekitarnya. Margin menciptakan ruang kosong di luar elemen.
        -   Aplikasi: Margin digunakan untuk mengontrol jarak antara elemen dengan elemen lain yang berdekatan atau dengan tepi elemen induknya.
        -   Pengaruh: Margin mempengaruhi tata letak elemen dengan cara mempengaruhi jarak antara elemen tersebut dan elemen-elemen tetangganya.
    2.  Padding
        -   Fungsi: Padding adalah jarak antara batas elemen dan kontennya. Padding menciptakan ruang kosong di dalam elemen.
        -   Aplikasi: Padding digunakan untuk mengatur jarak antara konten elemen dan batasnya. Ini mempengaruhi tampilan konten dalam elemen tersebut.
        -   Pengaruh: Padding mempengaruhi tampilan elemen dengan cara mempengaruhi jarak antara konten elemen dan batas elemen.

4.  **Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?**

    *   Tailwind CSS:
        -   Pendekatan "utility-first."
        -   Konfigurasi fleksibel.
        -   Memerlukan pemahaman HTML dan CSS yang baik.

    *   Bootstrap:
        -   Komponen UI siap pakai.
        -   Cocok untuk pemula.
        -   Tema bawaan tersedia.

    *   Kapan Menggunakan:
        -   Bootstrap: Cepat, pemula, tema bawaan.
        -   Tailwind CSS: Kontrol desain, pemahaman CSS, fleksibel.

5.  **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
    
    Untuk kustomisasi Login Page, saya menggunakan template dari https://mdbootstrap.com/docs/standard/extended/login/ dan memodifikasinya dengan mengubah warna dan gambar, dan menyesuaikan dengan form login yang dibuat pada tugas sebelumnya. Selanjutnya, saya menambahkan footer untuk semua page. Saya juga menambahkan navbar untuk main page, create product, dan edit product yang berisi nama aplikasi, teks welcome untuk user dan sebuah dropdown yang memiliki menu 'home' untuk kembali ke main page, 'add a new product' untuk menambahkan produk dan 'logout' untuk logout. User juga dapat kembali ke main page saat mengklik nama aplikasi di navbar. Terakhir, saya memodifikasi main page untuk menampilkan list produknya menggunakan pendekatan dengan card.







 

    