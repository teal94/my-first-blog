from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:num>', views.post_list, name='post_list'),
    path('post/<int:number>/p<int:pk>', views.post_detail, name='post_detail'),
    path('post/<int:number>/new', views.post_new, name='post_new'),
    path('post/<int:number>/p<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/<int:number>/p<int:pk>/delete', views.post_delete, name='post_delete'),
]