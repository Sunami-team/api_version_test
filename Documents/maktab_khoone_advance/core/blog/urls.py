from django.urls import path, include
from . import views
from django.views.generic import TemplateView


app_name = "blog"

urlpatterns = [
    # path('about/', TemplateView.as_view(template_name='index.html', extra_context={"name":"sina"}), name='fbv-test')
    # path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    path("go-to-maktab/<int:pk>",views.RedirectToMaktab.as_view(pattern_name="blog:cbv-index"),name="redirect-to-maktabkhooneh",),
    path('post/', views.PostList.as_view(), name="post-list"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-datail"),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name="post-edit"),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('api/v1/', include('blog.api.v1.urls')),
]
