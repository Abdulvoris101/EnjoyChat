from django.urls import path
from posts.views import index, verification_view,  like_and_get_post, api_all_posts, api_add_comment, post_detail, explore_posts, public_posts, PostDeleteView, post_comment_view

urlpatterns = [
    path('', index, name="home"),
    path('post/<int:pk>', post_detail, name='post_detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/c/<int:pk>/', post_comment_view, name='post-comment'),
    path('public/', public_posts, name='pb_posts'),
    path('add_comment/', api_add_comment, name='add_comment'),
    path('explore_posts/<int:pk>/', explore_posts, name='m_explore'),
    path('api/all_posts/', api_all_posts, name='api_all_posts'),
    path('get/verification/', verification_view, name='verification'),
    
    # api
    path('liked/', like_and_get_post, name="like-post-view"),
]
