# Generated by Django 3.1.3 on 2021-09-13 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
