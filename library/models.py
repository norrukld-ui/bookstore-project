from django.db import models
from datetime import date

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Аты-жөні")
    country = models.CharField(max_length=50, verbose_name="Елі")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторлар"


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Тег атауы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Тегтер"


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Кітап атауы")
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name="books", 
        verbose_name="Авторы"
    )
    tags = models.ManyToManyField(
        Tag, 
        related_name="books", 
        verbose_name="Тегтері"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Бағасы")
    pages = models.PositiveIntegerField(verbose_name="Бет саны")
    published = models.DateField(verbose_name="Шыққан күні")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published"]
        verbose_name = "Кітап"
        verbose_name_plural = "Кітаптар"