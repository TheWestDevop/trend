# Generated by Django 2.1 on 2019-04-26 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='pubdate',
            field=models.CharField(max_length=255),
        ),
    ]
