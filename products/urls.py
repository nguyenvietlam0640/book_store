from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from .import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('category/<str:category_slug>',views.ViewBookAsCategoryApi.as_view(),name='viewBookAsCategory'),
    path('api/search_results/<int:books_per_page>/<int:page>' ,views.SearchResultsApi.as_view()),
    path('api/view_book_as_category/<str:category_slug>/<int:books_per_page>/<int:page>',views.ViewBookAsCategoryApi.as_view()),
    path('api/view_categories' , views.ViewCategoriesApi.as_view()),
    path('api/view_category/<str:category_slug>' , views.ViewCategoryApi.as_view()),
]
