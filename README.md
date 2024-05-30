- Projenin Amacı : İnsansız Hava Araçları(İHA) kiralayabildiğimiz bir e-ticaret sitesi oluşturmaktır.
- Projede kullanılması için Python, Django, Postgresql ve Rest Framework istenmiştir. 
- Projeye https://github.com/DilaraBetul/iha_kiralama linki ulaşabilrsiniz.
- Kurulumlarda kullanılan versiyonlar aşağıdaki gibidir.
Package         Version
asgiref         3.8.1
Django          5.0.6
pip             24.0
psycopg2-binary 2.9.9
sqlparse        0.5.0
tzdata          2024.1
Python 3.12.3
psycopg2-2.9.9
- Projede PostgresSQL kurulumu sırasında sürümden kaynakla sürekli hata alınmıştır. Kurulum yapmak istediğinizde 16.3 ve 15.7 sürümlerinde hata yaşamansı durumunda benim tercih ettiğim 14.12 sürümünü tercih edebilirsiniz.
- Django ile İHA Kiralama sitesi için ilk olarak Python ve VSCode indirilmesi gerekmektedir. Sonrasında Django sayfasında indirme işlemlerimize devam ediyoruz. VSCode gelerek terminalden python -m pip install django
ile Django kurulumumuzu yapıyoruz.
- Sonrasında django-admin startproject Proje_Adi girerek ilgili projemizi açıyoruz.
- Projemize bağlı kategorileri oluşturmak için django-admin startapp Kategori_Adi belirleyerek projemize ait alt kırılımları belirliyoruz.
- Gerekli ortamlar hazırlandıktan sonra projemize başlayabiliriz.
- settinggs.py içerisinde INSTALLED_APPS de kırılımlarımızı tanımlıyoruz. DB bağlantılarını yine bu sayfada ayarlıyoruz.
- Projemize başlıyoruz.
- Daha önce Python programlama ve SQL ile çalışmalarım olsada Django kullanarak yaptığım ilk projeydi. Benim için keyifli bir süreç oldu. Farklı çalışmalardan uyarlayarak elimden gelenin en iyisini sizlere sunmaya çalıştım. Kurulumlarda ve versiyonlarda yaşadığım sorunlarla vakit kaybettim. İlk deneyime göre çok keyifli bir süreç oldu. Farklı uygulamalardaki kodları inceledim ve kendime nasıl uyarlayabileceğim konusunda fikirler edindim. İha kiralama için görseller seçerken emeği geçen mühendislerden olmayı çok istediğimi fark ettim. Umarım olumlu bir sonuç olur. Projeyi istenilen şekilde yapamadım ama süreç içerisinde elimden geleni yapmaya hazırım. 
