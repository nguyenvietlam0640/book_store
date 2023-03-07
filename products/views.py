from django.shortcuts import render, redirect
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Category, Book
from .serializers import BookSerializers, CategorySerializers
from json import JSONDecoder
from rest_framework.views import APIView
from django.http import JsonResponse
import json


class ViewBookAsCategoryApi(APIView):
    def get(self, request, category_slug, books_per_page, page, format=None):
        try:
            category = Category.objects.get(slug=category_slug)
            pageTotal = int(category.get_books_total() / books_per_page) if category.get_books_total(
            ) % books_per_page == 0 else int(category.get_books_total() / books_per_page)+1
            if page > 0 and page <= pageTotal:
                books = category.products.annotate()[(
                    books_per_page*(page-1)):books_per_page*page]
                bookSerializer = BookSerializers(books, many=True)
                return Response(bookSerializer.data)
            else:
                return Response({'404': 'page not found'})
        except:
            return Response({'404': 'somthing went wrong'})


class ViewCategoriesApi(APIView):
    def get(self, request, format=None):
        try:
            categories = Category.objects.all()
            categoriesSerializer = CategorySerializers(categories, many=True)
            return Response(categoriesSerializer.data)
        except:
            return Response({'200': 'categories empty'})


class ViewCategoryApi(APIView):
    def get(self, request, category_slug, format=None):
        try:
            category = Category.objects.filter(slug=category_slug)
            categorySerializer = CategorySerializers(category, many=True)
            return Response(categorySerializer.data)
        except:
            return Response({'404': 'category not found'})


class SearchResultsApi(APIView):
    def get(self, request, books_per_page, page, format=None):
        try:
            searchList = []

            try:
                id = int(request.GET['id'])
            except:
                id = request.GET['id']
            keyword = (request.GET['input'])

            if id == 'null':
                books = Book.objects.all()
                bookSerializers = BookSerializers(books, many=True)
                bookdict = json.loads(json.dumps(bookSerializers.data))
                for book in bookdict:
                    if keyword.lower() in book['title'].lower() or keyword in book['author'].lower():
                        searchList.append(book)
                pageTotal = int(len(searchList) / books_per_page) if len(
                    searchList) % books_per_page == 0 else int(len(searchList) / books_per_page)+1
                if page > 0 and page <= pageTotal:
                    return Response([len(searchList),searchList[(
                        books_per_page*(page-1)):books_per_page*page]])
                else:
                    return Response({'404': 'page not found'})
            else:
                category = Category.objects.get(id=id)
                books = category.products.all()
                bookSerializers = BookSerializers(books, many=True)
                bookdict = json.loads(json.dumps(bookSerializers.data))
                for book in bookdict:
                    if keyword.lower() in book['title'].lower() or keyword in book['author'].lower():
                        searchList.append(book)

                pageTotal = int(len(searchList) / books_per_page) if len(
                    searchList) % books_per_page == 0 else int(len(searchList) / books_per_page)+1
                if page > 0 and page <= pageTotal:
                    return Response([len(searchList),searchList[(
                        books_per_page*(page-1)):books_per_page*page]])
                else:
                    return Response({'404': 'page not found'})

        except:
            return Response({'404': 'somthing went wrong'})


