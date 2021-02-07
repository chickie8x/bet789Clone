from django.urls import path

from bet import views

urlpatterns =[
    path('',views.homePage, name ='homepage'),
    path('<slug:slug>/',views.articleList,name='articleList'),
    path('<slug:categorySlug>/<slug:postSlug>/',views.postDetail,name='postDetail'),
    path('<int:pk>/<slug:postSlug>/',views.postDetail,name='postDetail2'),
]