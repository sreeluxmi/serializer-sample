# Generated by Django 4.1.10 on 2023-07-18 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_book_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publish_date',
        ),
    ]
