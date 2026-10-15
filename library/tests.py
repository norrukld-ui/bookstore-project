from django.test import TestCase
from django.urls import reverse
from datetime import date
from .models import Author, Tag, Book

class BookQueryOptimizationTest(TestCase):
    def setUp(self):
        # Создаем тестовые данные
        author = Author.objects.create(name="Абай Құнанбайұлы", country="Қазақстан")
        tag = Tag.objects.create(name="поэзия")
        
        for i in range(5):
            book = Book.objects.create(
                title=f"Кітап {i}",
                author=author,
                price=2000,
                pages=100,
                published=date(2020, 1, 1)
            )
            book.tags.add(tag)

    def test_book_list_optimized_queries(self):
        # Проверяем, что сериализация списка книг через API / ORM выполняется за минимальное количество запросов благодаря select_related и prefetch_related
        url = reverse('api-book-list')
        with self.assertNumQueries(2):  # 1 запрос на книги/авторов + 1 запрос на теги (prefetch)
            response = self.client.get(url)
        self.assertEqual(response.status_code, 200)