# Generated by Django 5.1.6 on 2025-02-19 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_rename_comment_comment_comment_blog_blog_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_body',
            field=models.TextField(default='Default content'),
        ),
    ]
