# Generated by Django 4.1.5 on 2023-01-10 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("faq", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name="faq",
            name="cat",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="faq.cat"
            ),
        ),
    ]
