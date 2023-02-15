from rest_framework import serializers

from .models import Category, Book



class CategorySerializers(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = [
                'id',
                'name',
                'get_absolute_url',
                'get_number_of_books',
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
                'unit_price',
                'get_absolute_url',
                'get_image',
            ]