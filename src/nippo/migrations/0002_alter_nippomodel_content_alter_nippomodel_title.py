# Generated by Django 5.2 on 2025-04-30 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nippo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nippomodel',
            name='content',
            field=models.TextField(max_length=100, verbose_name='日報'),
        ),
        migrations.AlterField(
            model_name='nippomodel',
            name='title',
            field=models.CharField(max_length=100, verbose_name='タイトル'),
        ),
    ]
