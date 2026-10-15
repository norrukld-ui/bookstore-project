from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets, permissions
from .models import Book, Author, Tag  # <--- Убедись, что Author и Tag здесь импортированы!
from .forms import BookForm
from .serializers import BookSerializer, AuthorSerializer, TagSerializer

class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'
    
    # Оптимизация против проблемы N+1 (как указано в лекции)
    def get_queryset(self):
        return Book.objects.select_related('author').prefetch_related('tags').all()


class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'

    def get_queryset(self):
        return Book.objects.select_related('author').prefetch_related('tags').all()


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('book-list')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('book-list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    # Оптимизация с select_related и prefetch_related для исключения N+1
    queryset = Book.objects.select_related("author").prefetch_related("tags").all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]