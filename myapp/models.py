from django.db import models
from accounts.models import User

# Create your models here.
class Article(models.Model):
  user = models.ForeignKey(
      User,
      on_delete=models.CASCADE, # ユーザー削除時にその人の記事も削除する場合
      null=True, # 既存データがある場合は一時的に True にしてマイグレーション
      blank=True,
      related_name='articles', # 逆参照で user.articles で取得できる
  )
  title = models.CharField(max_length=255)
  article_text = models.CharField(max_length=255)
  article = models.CharField(max_length=255)
  tag = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.title
