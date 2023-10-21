from django.urls import path, include
from blog.api.v1 import views
from django.views.generic import TemplateView


app_name = "api-v1"

urlpatterns = [
    path('post/', views.PostList.as_view(), name='post-list'),
    # path('post/<int:id>/', views.post_detail, name='post-detail'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),

]
