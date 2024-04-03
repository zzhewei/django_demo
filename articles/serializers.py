"""
用来序列化和反序列化 input 和 output。
"""

from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """
    使用 Article 来序列化和反序列化。
    """

    class Meta:
        """
        設定元類

        Attributes:
            model : models.py 裡要序列化和反序列化的 class。
            fields : 序列化時，要用的欄位。
            read_only_fields : 設定欄位為只讀。
        """

        model = Article
        fields = "__all__"
        read_only_fields = ["id"]
