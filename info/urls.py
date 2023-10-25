from django.urls import path

from info import views

urlpatterns = [
    path('', views.site_description, name='site_description'),
    path('info/', views.site_info_about, name='site_info_about'),
    path('collections/', views.CollectionView.as_view(), name='collections'),
    path('collections/<int:id>', views.CollectionView.as_view(), name='collection'),
]