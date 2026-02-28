from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=255)
  article_text = models.CharField(max_length=255)
  article = models.CharField(max_length=255)
  tag = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.title
