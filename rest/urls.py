from rest_framework.routers import DefaultRouter

from rest import views


router = DefaultRouter()
router.register(r'records', views.RecordViewSet, basename='records')
router.register(r'collections', views.InfoCollectionViewSet, basename='collections')

urlpatterns = router.urls
