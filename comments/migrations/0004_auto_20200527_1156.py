# Generated by Django 2.2.1 on 2020-05-27 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20200527_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commented_to',
            field=models.CharField(max_length=100),
        ),
    ]
