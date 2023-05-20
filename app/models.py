from django.db import models

class Post(models.Model):
    title = models.CharField('title', max_length=50)
    image = models.ImageField(upload_to='images', verbose_name='Image', blank=True, null=True)
    content = models.TextField('text')
    created_at = models.DateTimeField('created at', auto_now_add=True)

    def __str__(self):
        return self.title

