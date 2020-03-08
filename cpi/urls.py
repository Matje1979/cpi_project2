from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='cpi-naslovna'),
    path('aktuelnosti/', views.aktuelnosti, name='aktuelnosti'),
    path('o_nama/', views.o_nama, name='o-nama'),
    path('o_nama/tim/', views.tim, name='cpi-tim'),
    path('o_nama/partneri/', views.partneri, name='cpi-partneri'),
    path('o_nama/galerija/', views.galerija, name='cpi-galerija'),
    path('o_nama/press/', views.press, name='cpi-press'),
    path('projekti/', views.projekti, name='cpi-projekti'),
    path('istorijske_ture/', views.istorijske_ture, name='cpi-istorijske_ture'),
    path('istorijske_ture/<int:pk>', views.tura_detalji, name='tura-detalji'),
    path('publikacije/', views.publikacije, name='cpi-publikacije'),
    path('pretraga/', views.pretraga, name='cpi-pretraga'),
    path('publikacije/<int:pk>', views.publikacije_detalji, name='cpi-publikacije-detalji'),
    path('o_nama/tim/<int:pk>', views.tim_detalji, name='cpi-tim-detalji'),
    path('o_nama/press/<int:pk>', views.press_detalji, name='cpi-press-detalji'),
    path('istorijske_ture/<int:pk>', views.projekti_detalji, name='cpi-projekti-detalji'),
    path('o_nama/galerija/<int:pk>', views.galerija_detalji, name='cpi-galerija-detalji'),
    path('projekti/', views.galerija_detalji, name='cpi-projekti'),
    path('projekti_detalji/<int:pk>/', views.projekti_detalji, name='cpi-projekti-detalji'), 
    path('projekti_detalji/<int:pk>/galerija', views.projekat_galerija, name='projekat-galerija'),
    path('aktuelnost_detalji/<int:pk>/', views.aktuelnost_detalji, name='cpi-aktuelnost-detalji'),
    path('prijava/', views.prijava, name='cpi-prijava'),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)