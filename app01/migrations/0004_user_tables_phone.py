# Generated by Django 2.1 on 2018-11-04 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_user_tables_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_tables',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
