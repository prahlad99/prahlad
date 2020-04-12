from django.db import models
class FavoriteBook(models.model):
     title=models.CharField(max_length=100)
     amazon_url=models.CharField(max_length=100)
     author=models.CharField(max_length=100)
     genre=models.IntegerField(max_length=10)
     def __str__(self):
           return self.title

