# Generated by Django 5.0.4 on 2024-04-19 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click to Read the blog post', max_length=255),
        ),
    ]
