# Generated by Django 2.1 on 2018-11-02 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_tables',
            name='email',
            field=models.EmailField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='user_tables',
            name='name',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='user_tables',
            name='pwd',
            field=models.CharField(max_length=32, null=True),
        ),
    ]