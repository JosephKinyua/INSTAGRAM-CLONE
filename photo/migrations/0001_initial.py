# Generated by Django 3.1.3 on 2021-09-12 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilePic', models.ImageField(blank=True, default='profileimages/test.png', null=True, upload_to='profileimages/')),
                ('fullName', models.CharField(max_length=255, null=True)),
                ('bio', tinymce.models.HTMLField(blank=True, null=True)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='photos/')),
                ('caption', models.CharField(max_length=3000)),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('uploadedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('pic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
