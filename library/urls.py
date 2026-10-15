from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookListView, 
    BookDetailView, 
    BookCreateView, 
    BookUpdateView, 
    BookDeleteView,
    BookViewSet,
    AuthorViewSet,
    TagViewSet
)

# Настройка роутера для REST API
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='api-book')
router.register(r'authors', AuthorViewSet, basename='api-author')
router.register(r'tags', TagViewSet, basename='api-tag')

urlpatterns = [
    # Веб-урлы (HTML)
    path('', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/add/', BookCreateView.as_view(), name='book-add'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book-edit'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    
    # REST API урлы (префикс /api/)
    path('api/', include(router.urls)),
]