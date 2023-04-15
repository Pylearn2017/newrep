from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path("tag/<slug:slug>", views.post_list, name='post_list_by_tag'),
    path("<slug:slug>", views.post_detail, name="post_detail"),
]