from .views import OrderCreationAPIView
from django.urls import path, include

urlpatterns = [
    path('create-order-unateus/', OrderCreationAPIView.as_view()),
]