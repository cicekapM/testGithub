from django.db import models

# Create your models here.

class Category (models.Model) :
    title = models.CharField (max_length = 250)
    slug = models.SlugField(prepopulate_from = ['title'] ,unique = True)
    description = models.TextField()


    class Meta :
        verbose_name_plural = "Categories"

    class Admin :
        pass

    def __str__(self) :
        return self.title
