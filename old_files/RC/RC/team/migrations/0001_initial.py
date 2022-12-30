# Generated by Django 3.2.8 on 2021-11-01 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('pic', models.ImageField(default='', upload_to='team')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.dept')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.position')),
            ],
        ),
    ]