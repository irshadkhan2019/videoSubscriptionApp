# Generated by Django 3.2.5 on 2023-10-31 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_video_video_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_id',
        ),
    ]