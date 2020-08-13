from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # path('', views.home, name='content-home'),
    path('', PostListView.as_view(), name='content-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='content-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='content-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='content-delete'),
    path('post/new/', PostCreateView.as_view(), name='content-create'),
    path('about/', views.about, name='content-about')
]