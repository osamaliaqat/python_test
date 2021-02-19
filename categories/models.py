from django.db import models

class Model(models.Model):
    class Meta:
        abstract = True


class Category(Model):
    parentCategory = models.ForeignKey('self', blank=True, null=True, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
