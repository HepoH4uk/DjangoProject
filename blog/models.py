from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    preview_image = models.ImageField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Дата создания")
    published = models.BooleanField(default=False)
    views_counter = models.PositiveIntegerField(default=0)



    class Meta:
        verbose_name = 'Пост блога'
        verbose_name_plural = 'Посты блога'

    def __str__(self):
        return self.title