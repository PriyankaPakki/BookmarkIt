from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("", views.bookmark_list, name="bookmark_list"),
    path("add/", views.bookmark_create, name="bookmark_create"),
    path("<int:pk>/edit/", views.bookmark_edit, name="bookmark_edit"),
    path("<int:pk>/delete/", views.bookmark_delete, name="bookmark_delete"),
]
