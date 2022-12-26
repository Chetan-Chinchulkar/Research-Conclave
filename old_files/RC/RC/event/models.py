from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    pic = models.ImageField(upload_to="event")
    subtitle = models.CharField(max_length=50)
    content = RichTextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Speaker(models.Model):
    name = models.CharField(max_length=50)
    subtitle = RichTextField()
    pic = models.ImageField(upload_to='speakers', height_field=None, width_field=None, max_length=None)
    content = RichTextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class InstituteSpeaker(models.Model):
    name = models.CharField(max_length=150)
    subtitle = RichTextField()
    pic = models.ImageField(upload_to='institute', height_field=None, width_field=None, max_length=None)
    content = RichTextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name