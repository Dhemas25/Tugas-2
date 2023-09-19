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


 

    