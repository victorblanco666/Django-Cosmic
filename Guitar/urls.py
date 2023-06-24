from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('nivel1',views.nivel1,name='nivel1'),
    path('nivel2',views.nivel2,name='nivel2'),
    path('nivel3',views.nivel3,name='nivel3')
]
   
