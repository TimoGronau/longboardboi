from django.urls import path
from . import views



urlpatterns = [
    path("details/<int:id>", views.user_detail, name="user-detail"),
    path("signup", views.SignUpView.as_view(), name="signup"),
]
