from django.db import models


class BookModel(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=128)
    info = models.TextField()
    pages = models.PositiveSmallIntegerField()
    ebook = models.FileField(upload_to='media/ebooks', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
