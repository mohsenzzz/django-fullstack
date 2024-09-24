from django.urls import reverse

from django.db import models
from django.utils.text import slugify


# Create your models here.


class User(models.Model):
    userName = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True,blank=True)


    def __str__(self):
        return f'{self.name} - {self.family}'

    def get_absolute_url(self):
        return reverse('user-profile',args=[self.slug] )

    def save(self,*args,**kwargs):
        self.slug = slugify(self.userName)
        super().save(*args,**kwargs)

