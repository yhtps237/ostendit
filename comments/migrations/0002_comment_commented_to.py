# Generated by Django 2.2.1 on 2020-05-27 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commented_to',
            field=models.CharField(default='ramil', max_length=100),
        ),
    ]
