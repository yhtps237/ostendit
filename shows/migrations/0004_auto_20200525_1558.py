# Generated by Django 2.2.1 on 2020-05-25 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_auto_20200525_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='animation',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]