from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class About(models.Model):
    title = RichTextField()
    content = RichTextField()
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title



