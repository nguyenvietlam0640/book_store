




from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/register', views.RegisterApi.as_view()),
    path('api/send_activate_email', views.SendActivateEmailApi.as_view()),
    path('api/activate', views.ActivateApi.as_view()),
    path('api/login',views.LoginApi.as_view()),
    path('api/user', views.UserApi.as_view()),
    path('api/reset_password', views.ResetPassApi.as_view()),
    path('api/change_password', views.ChangePassApi.as_view()),

]






