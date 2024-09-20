from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib import admin

router = DefaultRouter()
router.register(r'books', views.BookViewSet)
# router.register(r'books', views.BookViewSet, basename='book')


urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    
    # path('api/books/', views.BookViewSet),
    # path('admin/', admin.site.urls),
]