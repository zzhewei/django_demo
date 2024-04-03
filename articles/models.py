"""
管理會用到的 model，表示資料庫中的 tables。
"""

from django.db import models


class Article(models.Model):
    """
    用于表示 Article 的欄位。

    Attributes:
        id (AutoField): 主鍵，自動產生的整數型欄位。
        title (CharField): 標題，最大長度為 200 的字元欄位。
        image (ImageField): 圖片，上傳到指定目錄的圖像檔案，可以為空。
        author (CharField): 作者，最大長度為 100 的字元欄位。
        content (TextField): 內容，文字欄位。
        created_at (DateTimeField): 建立時間，自動產生的日期時間字段，記錄文章建立的時間。
        updated_at (DateTimeField): 更新時間，自動產生的日期時間字段，記錄文章最後更新的時間。
        objects : 對資料庫執行標準操作，可防止 Unresolved attribute reference 'objects' for class
    """

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="static/", null=True, blank=True)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Attributes:
            managed (bool): 指示是否由 Django 管理資料庫表。
            db_table (str): 資料庫中使用的表名。
        """

        managed = True
        db_table = "Article"

    objects = models.Manager()
