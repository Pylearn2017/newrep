from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:rubric_id>/', views.by_rubric, name = 'by_rubric'),
    
]