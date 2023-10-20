from django.urls import path

from info import views

urlpatterns = [
    path('', views.site_description, name='site_description'),
    path('info/', views.site_info_about, name='site_info_about'),
    path('collections/', views.read_collections, name='read_collections'),
]