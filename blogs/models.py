from django.db import models
from django.shortcuts import reverse



class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    data_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self): # - генерация уролов для сопостовления дополнительных элементов в урле urls.py
        return reverse('post_detail_url', kwargs={'slug':self.slug})

    def __str__(self):
        return f'{self.title}'
