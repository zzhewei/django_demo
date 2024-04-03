"""
分配 views.py 裡的視圖 URL
"""

from django.urls import path

from . import views

urlpatterns = [
    path("articles/", views.ArticleList.as_view(), name="article-list"),
    path("articles/<int:pk>/", views.ArticleDetail.as_view(), name="article-detail"),
]
