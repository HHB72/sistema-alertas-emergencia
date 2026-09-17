from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sos/', views.sos, name='sos'),
    path('primeros-auxilios/', views.primeros_auxilios, name='primeros_auxilios'),
    path('incidentes/', views.incidentes, name='incidentes'),
    path('contactos/', views.contactos, name='contactos'),
    path('hospitales/', views.hospitales, name='hospitales'),
    
    # Rutas para inicio y cierre de sesión personalizadas
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
]