from django.conf.urls import url 
from django.urls import path
from .import views
from home.views import HomeView


app_name = "home"
urlpatterns = [
     path('',HomeView.as_view(), name='home'),
     url(r'^post/(?P<pk>[0-9]+)/$', views.Post_detail, name='Post_detail'),
     url(r'^cmnt/(?P<pk>[0-9]+)/$', views.cmnt, name='cmnt'),
     url(r'^like/$', views.like_post, name='like_post'),
     # path('post/(?P<pk>/d+)', views.post_detail, name = 'post_detail' ),
     # path('cmnt/',views.cmnt, name='cmnt'),
     ]