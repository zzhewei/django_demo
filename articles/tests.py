"""
撰寫有關 articles 的測試案例
"""
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Article


class ArticleAPITest(APITestCase):
    """
    Article API測試類別。

    對文章API的各種功能進行了測試，包括取得所有文章、建立文章、取得單一文章、更新文章、部分更新文章和刪除文章。
    """

    def setUp(self):
        """
        設定測試所需的初始資料。

        建立了一個測試使用者和一個測試文章，並認證該使用者以進行API測試。
        """
        # 創建測試用戶
        self.user = User.objects.create_user(
            username="test_user", password="test_password"
        )
        self.client.force_authenticate(user=self.user)

        # 創建測試文章
        self.article = Article.objects.create(
            title="測試標題", author="測試作者", content="測試內容"
        )

    def test_get_all_articles(self):
        """
        測試取得所有文章的 API。

        檢查API端點的回應狀態碼是否為 HTTP 200 OK。
        """
        response = self.client.get("/API/articles/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_article(self):
        """
        測試建立文章的 API。

        提供資料建立新文章，並檢查 API 的回應狀態碼是否為 HTTP 201。
        """
        data = {"title": "新增測試標題", "author": "新增測試作者", "content": "新增測試內容"}
        response = self.client.post("/API/articles/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_single_article(self):
        """
        測試取得單一文章的 API。

        檢查 API 的回應狀態碼是否為 HTTP 200 OK。
        """
        response = self.client.get(f"/API/articles/{self.article.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_article(self):
        """
        測試更新文章的 API。

        提供資料更新文章，並檢查 API 的回應狀態碼是否為 HTTP 200 OK。
        """
        data = {"title": "更新測試標題", "author": "更新測試作者", "content": "更新測試內容"}
        response = self.client.put(f"/API/articles/{self.article.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_article(self):
        """
        測試部分更新文章的 API。

        提供部分資料更新文章，並檢查 API 的回應狀態碼是否為 HTTP 200 OK。
        """
        data = {
            "title": "部分更新測試標題",
        }
        response = self.client.patch(f"/API/articles/{self.article.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_article(self):
        """
        測試刪除文章的 API。

        檢查 API 的回應狀態碼是否為 HTTP 204。
        """
        response = self.client.delete(f"/API/articles/{self.article.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
