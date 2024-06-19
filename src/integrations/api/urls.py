from .views import OrderCreationAPIView
from django.urls import path, include

urlpatterns = [
    path('create-order/<str:warehouse>/', OrderCreationAPIView.as_view()),
]