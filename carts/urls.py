from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartView.as_view()),
    path('users/<int:user_id>/cart/', views.CartDetailView.as_view())
]
