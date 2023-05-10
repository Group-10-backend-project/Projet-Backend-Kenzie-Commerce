from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("users/address/", views.AddressView.as_view()),
    path("users/<int:user_id>/address/", views.AddressDetailView.as_view()),
]
