# Generated by Django 3.2.8 on 2021-11-17 10:50

from django.db import migrations, models
import members.models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_alter_bio_abstract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='abstract',
            field=models.FileField(upload_to=members.models.content_file_name),
        ),
    ]
