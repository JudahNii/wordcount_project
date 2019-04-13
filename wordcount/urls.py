

##from django.contrib import admin
##from django.urls import path

##urlpatterns = [
    ##path('homepage/', admin.site.urls),
##]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('count/', views.count, name='count'),
    path('about_us/', views.about_us, name='about_us'),
]
