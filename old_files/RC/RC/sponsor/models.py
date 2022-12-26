from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    pic  = models.ImageField(upload_to='sponsor')
    text = RichTextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=50)
  
    def __str__(self):
        return self.name


class OurSponsor(models.Model):
    name = models.CharField(max_length=150)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='oursponsor', height_field=None, width_field=None, max_length=None,default="")


    def __str__(self):
        return self.name