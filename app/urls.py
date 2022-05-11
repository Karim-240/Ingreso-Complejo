from django.urls import path, include
from .views import home,dashboard, galeria, contacto, LQR, EQR, logOutReedirect, logIn, getUrl, newQR,getQR, showLectorQR


urlpatterns = [
    path('', logIn, name='logIn'),
    path('LQR/', LQR, name='LQR'),
    path('EQR/', EQR, name='EQR'),
    path('home/', home, name='home'),
    path('galeria/', galeria, name='galeria'),
    path('contacto/', contacto, name='contacto'),
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logOutReedirect, name='logOutReedirect'),
    path('newQR/', newQR.as_view(), name='newQR'),
    path('getQR/', getQR.as_view(), name='getQR'),
    path('showLectorQR/',showLectorQR, name='showLectorQR'),
]