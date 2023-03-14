from django.shortcuts import render, redirect
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Category, Book, Comment
from .serializers import BookSerializers, CategorySerializers, CommentSerializer
from json import JSONDecoder
from rest_framework.views import APIView
from django.http import JsonResponse
from authentication.models import User
import json


class ViewBookAsCategory(APIView):
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


class ViewCategories(APIView):
    def get(self, request, format=None):
        try:
            categories = Category.objects.all()
            categoriesSerializer = CategorySerializers(categories, many=True)
            return Response(categoriesSerializer.data)
        except:
            return Response({'200': 'categories empty'})


class ViewCategory(APIView):
    def get(self, request, category_slug, format=None):
        try:
            category = Category.objects.filter(slug=category_slug)
            categorySerializer = CategorySerializers(category, many=True)
            return Response(categorySerializer.data)
        except:
            return Response({'404': 'category not found'}, status=404)


class SearchResults(APIView):
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
                    return Response([len(searchList), searchList[(
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
                    return Response([len(searchList), searchList[(
                        books_per_page*(page-1)):books_per_page*page]])
                else:
                    return Response({'404': 'page not found'})

        except:
            return Response({'404': 'somthing went wrong'})


class ViewBookDetail(APIView):
    def get(self, request, category_slug, book_slug):

        book = Book.objects.filter(slug=book_slug).first()
        if book:
            bookSerializer = BookSerializers(book)
            return Response(bookSerializer.data)
        return Response({'message': 'Book not found'}, status=404)


class ViewAllComments(APIView):
    def get(self, request, book_slug):
        book = Book.objects.filter(slug=book_slug).first()
        if book:
            comments = book.comments.all()
            commentsSerializer = CommentSerializer(comments, many=True)
            for data in commentsSerializer.data:
                data['created_by'] = User.objects.get(
                    id=int(data['created_by'])).full_name
            return Response(commentsSerializer.data)

        return Response({'message': 'Book not found'}, status=404)


class PostComment(APIView):

    def get(self, request, book_slug, user_id):
        book = Book.objects.filter(slug=book_slug).first()
        user = User.objects.filter(id=user_id).first()
        if book and user:
            existed_comment = Comment.objects.filter(
                created_for=book.id, created_by=user.id)
            if existed_comment:
                return Response({'message': False})
            return Response({'message': True})
        return Response({'message': 'book or user not found'}, status=404)

    def post(self, request, book_slug, user_id):

        book = Book.objects.filter(slug=book_slug).first()
        user = User.objects.filter(id=user_id).first()
        if book and user:
            data = request.data
            data['created_for'] = book.id
            data['created_by'] = user.id
            if data['rating']:
                if data['rating'] >= 0 and data['rating'] <= 5:
                    comment = CommentSerializer(data=data)
                    comment.is_valid(raise_exception=True)
                    comment.save()

                    return Response({'message': 'success'})
            return Response({'message': 'rating value must provided'}, status=403)
        return Response({'message': 'book or user not found'}, status=404)
