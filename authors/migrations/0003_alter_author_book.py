# Generated by Django 5.1.2 on 2024-10-24 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_alter_author_book'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(related_name='authors', to='books.book'),
        ),
    ]