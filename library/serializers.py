from rest_framework import serializers
from .models import Author, Tag, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'country']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    # Для чтения возвращаем полный объект автора
    author = AuthorSerializer(read_only=True)
    # Для записи принимаем author_id
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source="author", write_only=True
    )
    # Теги через имя (SlugRelatedField)
    tags = serializers.SlugRelatedField(
        many=True, slug_field="name", queryset=Tag.objects.all()
    )

    class Meta:
        model = Book
        fields = ["id", "title", "author", "author_id", "tags", "price", "pages", "published"]