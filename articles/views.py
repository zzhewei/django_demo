"""
熱門文章的新增、修改、刪除及查詢
"""

from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializers import ArticleSerializer


class ArticleList(generics.ListCreateAPIView):
    """
    取得所有文章列表及創建文章的視圖。

    繼承 ListCreateAPIView 並實作 get、post"""

    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    parser_classes = [MultiPartParser, FormParser]


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    取得單一文章列表及更新或刪除文章的視圖。

    繼承 RetrieveUpdateDestroyAPIView 並實作 get、put、patch、delete"""

    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    parser_classes = [MultiPartParser, FormParser]
