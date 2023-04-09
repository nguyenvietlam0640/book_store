from django.urls import path

from .import views


urlpatterns = [
    path('webhook', views.webhook_view),
    path('api/create_checkout_session', views.create_checkout_session.as_view()),
    path('api/check_order_session', views.check_order_session.as_view())
]
