# Generated by Django 4.0 on 2023-06-19 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(max_length=500),
        ),
    ]
