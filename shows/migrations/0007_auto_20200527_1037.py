# Generated by Django 2.2.1 on 2020-05-27 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0006_auto_20200527_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='slug',
            field=models.SlugField(),
        ),
    ]
