from django.urls import path
from .views import HomePageView, HomeDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'), #La coma es imortante (Tupla)
    path('agregar/<int:pk>/', HomeDetailView.as_view(), name = 'post_detail'),
]