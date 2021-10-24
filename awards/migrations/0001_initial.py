# Generated by Django 3.2.8 on 2021-10-24 21:17

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('project_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='images')),
                ('desc', models.TextField(max_length=250)),
                ('url_link', models.URLField(blank=True, max_length=254)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pict', cloudinary.models.CloudinaryField(max_length=255, verbose_name='images')),
                ('bio', models.TextField(blank=True, max_length=250)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.IntegerField(default=0)),
                ('usability', models.IntegerField(default=0)),
                ('creativity', models.IntegerField(default=0)),
                ('comment', models.TextField(max_length=250)),
                ('date_rated', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='awards.post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='awards.profile')),
            ],
        ),
    ]
