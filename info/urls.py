from django.urls import path

from info import views

urlpatterns = [
    path('', views.site_description, name='site_description'),
    path('info/', views.site_info_about, name='site_info_about'),
    path('collections/', views.CollectionListView.as_view(), name='collection-list'),
    path('collections/<int:pk>', views.CollectionDetailView.as_view(), name='collection-detail'),
    path('collections/create', views.CollectionCreateView.as_view(), name='collection-create'),
    path('collections/<int:pk>/update', views.CollectionUpdateView.as_view(), name='collection-update'),
    path('collections/<int:pk>/delete', views.CollectionDeleteView.as_view(), name='collection-delete'),
]
