# Generated by Django 5.1.7 on 2025-04-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='bookmark_images/'),
        ),
    ]
