# Generated by Django 5.0.4 on 2024-04-09 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='', max_length=255),
        ),
    ]
