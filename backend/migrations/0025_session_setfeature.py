# Generated by Django 3.2 on 2022-09-21 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0024_practiceidentifysession_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=400, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('set', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='setFeatures', to='backend.set')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(blank=True, max_length=20, null=True)),
                ('height', models.CharField(blank=True, max_length=20, null=True)),
                ('weight', models.CharField(blank=True, max_length=20, null=True)),
                ('armL', models.CharField(blank=True, max_length=20, null=True)),
                ('legL', models.CharField(blank=True, max_length=20, null=True)),
                ('chestG', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('owner_username', models.CharField(max_length=30, null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Session', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
