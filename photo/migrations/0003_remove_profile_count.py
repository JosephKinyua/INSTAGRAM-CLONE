# Generated by Django 3.1.3 on 2021-09-13 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_profile_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='count',
        ),
    ]