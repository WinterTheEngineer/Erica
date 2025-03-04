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
    order = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=120)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.list.ordered:
            if self.order is None:
                last_order = ListItem.objects.filter(list=self.list).aggregate(models.Max('order'))['order__max']
                self.order = 1 if last_order is None else last_order + 1
        else:
            self.order = None

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
