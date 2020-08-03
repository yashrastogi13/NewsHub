from django.urls import path
from .views import ArticleListView,ArticleUpdateView,ArticleDetailView,ArticleDeleteView,ArticleCreateView,ArticleView,post_detail
from . import views
urlpatterns=[
    path('<int:pk>/edit/',ArticleUpdateView.as_view(),name='article_edit'),  #article/1/edit
    path('<int:pk>/',ArticleDetailView.as_view(),name='article_detail'),     #article/1/
    path('<int:pk>/view',ArticleView.as_view(),name='article_view'),               #article/1/
    path('<int:pk>/delete/',ArticleDeleteView.as_view(),name='article_delete'),  #article/1/delete
    path('create/',ArticleCreateView.as_view(),name='article_create'),          #article/create
    path('',ArticleListView.as_view(),name='article_list'),
    path('<int:pk>/comment/',views.post_detail,name='post_detail'),

]