from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view() , name='blog'),
    path('<slug:slug>', PostDetail.as_view(), name='post-detail')

]
