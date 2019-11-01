"""Defines URL patterns for Trueblaze"""
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'Trueblaze'


urlpatterns = [
    # Home url
    path('', views.index, name='index'),
    # sign url
    path('sign/', views.sign, name='sign'),
    # about
    path('about/', views.about, name='about'),
    # portfolio
    path('portfolio/', views.portfolio, name='portfolio'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
