from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.db import models
from django.db.models import CASCADE
from django.urls import reverse
from django.utils.text import slugify


from  users.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=500,null=False)
    created_by = models.ForeignKey(User, verbose_name="user_own",on_delete=CASCADE, related_name="user_own")

    description=models.CharField(max_length=500,null=True)
    asigned_to=models.ManyToManyField(User,related_name="asigned_task",null=True,blank=True)
    expire_time=models.DateTimeField(default=datetime.now() +relativedelta(year=1),null=True,blank=True)
    slug=models.SlugField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="created at")
    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('tasks',args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)

