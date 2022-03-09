from django.urls import path,include
from .import views 
from django.conf.urls.static import static

urlpatterns = [path('',views.home,name='home.html'),
			   path('about.html',views.about,name='about')



]