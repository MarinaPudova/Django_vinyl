from django.urls import path
from rest_framework.routers import DefaultRouter

from rest import views

urlpatterns = [
    # path('records/', views.RecordListCreateView.as_view(), name='rest-records'),
    # path('records/', views.RecordViewSet.as_view({'get': 'list'}), name='rest-records'),
    # path('records/', views.RecordView.as_view(), name='rest-records'),
    # path('records/<int:pk>', views.RecordRetrieveUpdateDeleteView.as_view(), name='rest-records-update'),
    # path('records/<int:pk>', views.RecordViewSet.as_view({'get': 'retrieve'}), name='rest-record'),
    # path('records/<int:pk>', views.SingleRecordView.as_view(), name='rest-record'),
    # path('collections/', views.InfoCollectionListCreateView.as_view(), name='rest-collections'),
    # path(
    #     'collections/<int:pk>', views.InfoCollectionRetrieveUpdateDeleteView.as_view(), name='rest-collections-update'
    # ),
  ]

router = DefaultRouter()
router.register(r'records', views.RecordViewSet, basename='records')
router.register(r'collections', views.InfoCollectionViewSet, basename='collections')

urlpatterns += router.urls
