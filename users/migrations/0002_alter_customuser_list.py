# Generated by Django 5.1.2 on 2024-10-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readlist', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='list',
            field=models.ManyToManyField(related_name='lists', to='readlist.readlist'),
        ),
    ]
