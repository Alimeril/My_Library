# Generated by Django 5.0.6 on 2024-05-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Author Name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author_surname',
            field=models.CharField(max_length=50, verbose_name='Author Surname'),
        ),
    ]
