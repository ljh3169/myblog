from django.urls import path, include
from blog import views

app_name = 'blog'

urlpatterns = [
    # 포스트 목록
    path('', views.index, name='index'), #127.0.0.1:8000/blog/
    # 상세 페이지
    path('<int:post_id>/', views.detail, name='detail'),
    # 포스트 쓰기
    path('post/create/', views.post_create, name='post_create'),
]