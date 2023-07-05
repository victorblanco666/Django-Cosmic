#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('administrador/', views.indexadmin, name='administrador'),
    path('encontrarUsuario/<int:pk>/', views.encontrarUsuario, name='encontrarUsuario'),
    path('encontrarUsuario/', views.encontrarUsuario, name='encontrarUsuario'),
    path('modificarUsuario/', views.modificarUsuario, name='modificarUsuario'),
    path('eliminarUsuario/<str:pk>',views.eliminarUsuario,name='eliminarUsuario'),
    path('agregarUsuario/', views.agregarUsuario, name='agregarUsuario')
]
