# Generated by Django 3.0.8 on 2020-08-03 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200803_0411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='article_c',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='author_c',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='date',
            new_name='date_c',
        ),
    ]