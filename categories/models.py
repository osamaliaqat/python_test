from django.db import models


class Model(models.Model):
    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=36, unique=True)


class sub_category(models.Model):
    parentCategory = models.ForeignKey(Category, blank=True, null=True, related_name='subcategories',
                                       on_delete=models.CASCADE)
    name = models.CharField(max_length=36, unique=True, null=True)


class childern(models.Model):
    parentCategory = models.ForeignKey(sub_category, blank=True, null=True, related_name='subcategories',
                                       on_delete=models.CASCADE)
    name = models.CharField(max_length=36, unique=True, null=True)



