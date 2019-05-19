from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.category_setting, name='category_setting'),
    path('ca_del<int:pk>', views.category_delete, name='category_delete'),
    path('ca<int:num>', views.post_list, name='post_list'),
    path('ca<int:number>/p<int:pk>', views.post_detail, name='post_detail'),
    path('ca<int:number>/new', views.post_new, name='post_new'),
    path('ca<int:number>/p<int:pk>/edit', views.post_edit, name='post_edit'),
    path('ca<int:number>/p<int:pk>/delete', views.post_delete, name='post_delete'),
    path('ca<int:number>/p<int:post_pk>/comment_del<int:comment_pk>', views.comment_delete, name='comment_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)