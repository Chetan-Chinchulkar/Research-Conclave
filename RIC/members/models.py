from django.db import models
import os
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from ckeditor.fields import RichTextField
# Create your models here.
class Event1(models.Model):
    name = models.CharField(max_length=50)
    fee = models.IntegerField(default=200)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
        
class Event2(models.Model):
    name = models.CharField(max_length=50)
    fee = models.IntegerField(default=200)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Dept(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Workshop(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    name = RichTextField()
    fee = models.IntegerField()
    desc = RichTextField(blank=True, null=True)
    organised_at = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    conducted_by = RichTextField(blank=True, null=True)
    link = models.URLField(max_length=200,default="") 

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s_%s_%s_%s.%s" % (instance.owner.first_name,instance.owner.last_name, instance.dept,instance.institute,instance.event2, ext)
    return os.path.join('abstract', filename)

class Bio(models.Model):
    institute = models.CharField(max_length=50)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE,default=None)
    abstract = models.FileField(upload_to=content_file_name, max_length=100)
    abstractFormat = models.BooleanField(default=True,null=True,blank=True)
    event2 = models.ForeignKey(Event2, on_delete=models.CASCADE,default=3)
    event1 = models.ManyToManyField(Event1, blank=True,null=True)
    number = PhoneNumberField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = RichTextField(blank=True, null=True)
    total = models.IntegerField(default=0,blank=True,null=True)
    selected = models.BooleanField(default=False,null=True,blank=True)
    selected_oral = models.BooleanField(default=False,blank=True, null=True)
    razorpay_payment_id = models.CharField( max_length=100,null=True,blank=True)
    iitg_student = models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return self.owner.email

    def __unicode__(self):
        return self.owner.email

    def setpaymentid(self,id):
        print('test')
        print(id)
        self.razorpay_payment_id = id
        self.save()

class WorkshopBio(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE,default=None)
    workshop = models.ManyToManyField(Workshop, blank=True,null=True)
    number = PhoneNumberField()
    text = RichTextField(blank=True, null=True)
    total = models.IntegerField(default=0,blank=True,null=True)
    razorpay_payment_id = models.CharField( max_length=100,null=True,blank=True)

    def __str__(self):
        return self.owner.email

    def __unicode__(self):
        return self.owner.email

    def setpaymentid(self,id):
        print('test')
        print(id)
        self.razorpay_payment_id = id
        self.save()
