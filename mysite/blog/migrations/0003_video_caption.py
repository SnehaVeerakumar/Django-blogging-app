# Generated by Django 3.1.3 on 2020-11-11 14:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='caption',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
