from django.shortcuts import render, redirect
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Category, Book
from .serializers import BookSerializers,CategorySerializers
from json import JSONDecoder
from rest_framework.views import APIView
from django.http import JsonResponse


class ViewBookAsCategoryApi(APIView):
    def get(self, request, category_slug, format=None):
        try:
            category = Category.objects.get(slug = category_slug)
            books = category.products.all()
            bookSerializer = BookSerializers(books, many=True)
            return Response(bookSerializer.data)
        except:
            return Response({'404': 'category not found'})


class ViewCategoriesApi(APIView):
    def get (self, request, format= None):
        try: 
            categories = Category.objects.all()
            categoriesSerializer = CategorySerializers(categories, many = True)
            return Response(categoriesSerializer.data)
        except:
            return Response({'200': 'categories empty'})

class ViewCategoryApi(APIView):
    def get(self, request, category_slug, format=None):
        try: 
            category = Category.objects.filter(slug =category_slug)
            categorySerializer = CategorySerializers(category, many = True)
            return Response(categorySerializer.data)
        except:
            return Response({'404': 'category not found'})
        
def home(request):
    category_url = Category.objects.order_by("?").first().get_absolute_url()
    return redirect('category'+category_url)

def viewBookAsCategory(request, category_slug):
    print(category_slug)
    return render(request, 'home.html')