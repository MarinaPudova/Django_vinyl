from django.urls import path, include

urlpatterns = [
    path('auth/', include('djoser.urls')),  # djoser
    path('auth/', include('djoser.urls.jwt')),  # djoser
]
