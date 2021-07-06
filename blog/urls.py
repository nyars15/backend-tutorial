from django.conf.urls import url
from django.urls import path
from .import views



urlpatterns = [
    url(r'^signup/$',      views.signup, name="signup"),
    path('',               views.post_list, name="post_list"),
    path('post/<int:pk>/', views.post_detail, name="post_detail"),
]


