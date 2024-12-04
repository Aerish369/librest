from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()
router.register('books', views.BookViewSet)
router.register('profile', views.ProfileViewSet)


urlpatterns = router.urls

# urlpatterns = [
#     path('home/', views.BookList.as_view(), name='home'),
#     path('book/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
# ]