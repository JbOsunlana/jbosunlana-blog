from django.urls import path
from .views import *

urlpatterns = [
    path('blog/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('delete_post/<int:pk>/', BlogDeleteView.as_view(), name = 'delete_post'),
    path('edit_post/<int:pk>/', BlogUpdateView.as_view(), name = 'edit_post'),
    path('new_post/', BlogCreateView.as_view(), name = 'new_post'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'),
    path('', BlogListView.as_view(), name = 'post_list'),
    
]