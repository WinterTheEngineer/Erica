from django.db import models

# Create your models here.
class ListItem(models.Model):

    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class List(models.Model):

    title = models.CharField(max_length=120)
    description = models.CharField(max_length=255, blank=True)
    listItems = models.ManyToManyField(ListItem, blank=True)
    
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.title