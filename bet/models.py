from django.db import models
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    slug = models.SlugField(max_length=100)
    display = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.slug


class Article(models.Model):
    title = models.CharField(max_length=250)
    feature_img = models.CharField(max_length=500)
    desc = models.TextField()
    content = models.TextField()
    pubDate = models.DateField();
    slug = models.SlugField(max_length=250, null=True, blank=True)
    cat = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)
