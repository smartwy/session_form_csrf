# Generated by Django 2.1 on 2018-11-04 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20181102_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_tables',
            name='user_type',
            field=models.IntegerField(max_length=2, null=True),
        ),
    ]
