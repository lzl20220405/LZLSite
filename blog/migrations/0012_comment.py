# Generated by Django 4.2 on 2023-07-16 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_user_loved_blog'),
        ('blog', '0011_blog_love'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_comment', models.TextField(blank=True, null=True, verbose_name='子评论')),
                ('text', models.TextField(verbose_name='内容')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment', verbose_name='父评论')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.user', verbose_name='用户')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'ordering': ['c_time'],
            },
        ),
    ]
