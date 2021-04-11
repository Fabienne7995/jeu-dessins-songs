from django.urls import path
from . import views

urlpatterns = [
    path('_1/', views.post_list_1, name='post_list_1'),
    path('', views.post_list, name='post_list'),
]
