# Generated by Django 4.2 on 2023-07-12 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(to='blog.tag', verbose_name='标签'),
        ),
    ]
