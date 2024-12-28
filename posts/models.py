from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse(
            'posts:detail',
            kwargs={
                'year': self.created_at.year,
                'month': self.created_at.month,
                'day': self.created_at.day,
                'slug': self.slug
            }
        )