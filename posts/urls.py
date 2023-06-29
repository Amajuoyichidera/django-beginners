from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='posts_home'),
    path('greet/', views.greet, name='greet'),
    path('posts/', views.return_all_posts, name='all_posts'),
    path('posts/<int:post_id>', views.return_single_post, name='one_post'),
    path('about/', views.about, name='about'),
    path('services/', views.services,name='services'),
    path('createPost/', views.create_post, name='create-post')
]