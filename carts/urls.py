from django.urls import path
from . import views

urlpatterns = [
    path('users/<int:user_id>/cart', views.CartView.as_view())
]
