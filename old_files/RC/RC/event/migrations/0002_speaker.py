# Generated by Django 3.2.8 on 2021-11-21 14:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subtitle', ckeditor.fields.RichTextField()),
                ('pic', models.ImageField(upload_to='speakers')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]