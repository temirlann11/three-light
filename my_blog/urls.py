from django.urls import path
from . import views
from .views import DeleteComment
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import path
from .views import Register






urlpatterns = [path('', views.PostView.as_view(), name='index'),
               path('<int:pk>/', views.PostDetail.as_view()),
               path('review/<int:pk>', views.AddComments.as_view(), name='add_comments'),
               path('<int:pk>/add_likes/', views.AddLike.as_view(), name='add_like'),
               path('<int:pk>/del_likes/', views.DelLike.as_view(), name='del_likes'),
               path('about/', views.About.as_view(), name='about'),
               path('menu/', views.Menu.as_view(), name='menu'),
               path('service/', views.Service.as_view(), name='service'),
               path('order/', views.Order.as_view(), name='order'),
               path('register/', views.Register.as_view(), name='register'),
               path('delete_comment/<int:comment_id>/', DeleteComment.as_view(), name='delete_comment')]