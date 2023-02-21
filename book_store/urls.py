"""book_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from products import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    
    path('category/<str:category_slug>',views.viewBookAsCategory,name='viewBookAsCategory'),
    

    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),




    path('api/search_results/<int:books_per_page>/<int:page>' ,views.SearchResultsApi.as_view()),
    path('api/view_book_as_category/<str:category_slug>/<int:books_per_page>/<int:page>',views.ViewBookAsCategoryApi.as_view()),
    path('api/view_categories' , views.ViewCategoriesApi.as_view()),
    path('api/view_category/<str:category_slug>' , views.ViewCategoryApi.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
