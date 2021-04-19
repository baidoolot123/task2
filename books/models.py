from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    image = models.ImageField(upload_to='book_images', blank=True)

# class Meta:
#         ordering = ('title',)
#         verbose_name = 'Книга'
#         verbose_name_plural = 'Книги'

# def __str__(self):
#     return self.title

def __unicode__(self):
    return self.title + " / " + self.author

