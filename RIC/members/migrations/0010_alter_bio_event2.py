# Generated by Django 3.2.8 on 2021-11-17 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_workshop_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='event2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.event2'),
        ),
    ]