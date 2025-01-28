from django.db import models

# Create your models here.

class List(models.Model):

    title = models.CharField(max_length=120)
    description = models.CharField(max_length=255, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ListItem(models.Model):
    name = models.CharField(max_length=120)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
