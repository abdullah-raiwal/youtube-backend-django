# Generated by Django 5.0.3 on 2024-03-13 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="refreshToken",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]