# Generated by Django 4.2 on 2023-07-30 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='url',
            field=models.URLField(default='https://github.com/', verbose_name='链接'),
        ),
    ]