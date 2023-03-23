from django.urls import path

from .import views


urlpatterns = [
    path('webhook', views.webhook_view),
    path('create_checkout_session', views.create_checkout_session.as_view())
]
