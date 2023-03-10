# Generated by Django 3.2.8 on 2021-11-02 09:12

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fee', models.IntegerField(default=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fee', models.IntegerField(default=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=50)),
                ('abstract', models.FileField(upload_to='abstract')),
                ('abstractFormat', models.BooleanField(blank=True, default=True, null=True)),
                ('selected', models.BooleanField(blank=True, default=False, null=True)),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('text', ckeditor.fields.RichTextField()),
                ('total', models.IntegerField(blank=True, default=0, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.BooleanField(blank=True, default=False, null=True)),
                ('dept', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='members.dept')),
                ('event1', models.ManyToManyField(blank=True, null=True, to='members.Event1')),
                ('event2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='members.event2')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
