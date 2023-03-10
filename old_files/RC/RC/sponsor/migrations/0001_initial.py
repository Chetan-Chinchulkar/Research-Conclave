# Generated by Django 3.2.8 on 2021-11-10 12:19

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('pic', models.ImageField(upload_to='sponsor')),
                ('text', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='OurSponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('pic', models.ImageField(default='', upload_to='oursponsor')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sponsor.cat')),
            ],
        ),
    ]
