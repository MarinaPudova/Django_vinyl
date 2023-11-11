from django.urls import path

from rest import views

urlpatterns = [
    path('records/', views.RecordListCreateView.as_view(), name='rest-records'),
    path('records/<int:pk>', views.RecordRetrieveUpdateDeleteView.as_view(), name='rest-records-update'),
    path('collections/', views.InfoCollectionListCreateView.as_view(), name='rest-collections'),
    path('collections/<int:pk>', views.InfoCollectionRetrieveUpdateDeleteView.as_view(), name='rest-collections-update'),
  ]
