# Generated by Django 4.0.4 on 2022-10-28 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='slug', verbose_name='Slug'),
            preserve_default=False,
        ),
    ]