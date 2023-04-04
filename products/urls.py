from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('category/<str:category_slug>',
         views.ViewBookAsCategory.as_view(), name='viewBookAsCategory'),
     path('api/search_results/<int:books_per_page>/<int:page>',
         views.SearchResults.as_view()),
     path('api/view_book_as_category/<str:category_slug>/<int:books_per_page>/<int:page>',
         views.ViewBookAsCategory.as_view()),
     path('api/view_categories', views.ViewCategories.as_view()),
     path('api/view_category/<str:category_slug>', views.ViewCategory.as_view()),
     path('api/category/<str:category_slug>/<str:book_slug>',
         views.ViewBookDetail.as_view()),
     path('api/view_all_comments/<str:book_slug>',
         views.ViewAllComments.as_view()),
     path('api/post_comment/<str:book_slug>/<int:user_id>', views.PostComment.as_view()),
     path('api/past_orders', views.PastOrders.as_view())
]
