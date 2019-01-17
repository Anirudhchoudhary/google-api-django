from django.db import models

# Create your models here.
class Photo(models.Model):
    file  = models.ImageField()
    upload_at  = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'


        