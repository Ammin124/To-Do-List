from django.db import models
from django.urls import reverse
# Create your models here.

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + "|" + str(self.completed)

    def get_absolute_url(self):
        return reverse('home', args=(str(self.id)))

    class Meta:
        ordering = ['-id']
