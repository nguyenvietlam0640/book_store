from rest_framework import serializers

from .models import Category, Book, Comment


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'get_absolute_url',
            'get_books_total',
        ]


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'des',
            'publisher',
            'published_date',
            'unit_price',
            'get_absolute_url',
            'get_image',
            'get_total_rating_count',
            'get_total_rating_value',
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'created_by',
            'created_for',
            'rating',
            'content',
            'created_at',
        ]
        extra_kwargs = {
            'created_for': {'write_only': True}
        }
