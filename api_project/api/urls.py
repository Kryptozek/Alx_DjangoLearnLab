from django.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet  # Import BookList for the existing ListAPIView
from django.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
        
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
]




