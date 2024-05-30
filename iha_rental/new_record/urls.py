from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("home",views.home),
    path("new_record",views.new_record),
    path("about_us",views.about_us)

]
