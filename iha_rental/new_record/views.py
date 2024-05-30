from django.shortcuts import render


iha_liste=[
    {
        "iha_adi":"KIZIL ELMA",
        "resim":"kizilelma2.jpg",
    },
         {
        "iha_adi":"AKINCI",
        "resim":"akinci.jpg",
    },
        {
        "iha_adi":"TB3",
        "resim":"akinci.jpg",
    },
        {
        "iha_adi":"TB'",
        "resim":"akinci.jpg",
    },
        {
        "iha_adi":"KEMANKEŞ 1 MİNİ",
        "resim":"akinci.jpg",
    },
        {
        "iha_adi":"KEMANKEŞ 2 MİNİ",
        "resim":"akinci.jpg",
    },
    {
        "iha_adi":"MİNİ İHA",
        "resim":"akinci.jpg",
    },
    {
        "iha_adi":"DİHA",
        "resim":"akinci.jpg",
    },
]

def home(request):
    data={
        "ihalar": iha_liste
    }
    return render(request,"index.html",data)

def about_us(request):
    return render(request,"about_us.html")

def new_record(request):
    data={
        "ihalar": iha_liste
    }
    return render(request,"new_record.html",data)
