# Generated by Django 3.2 on 2022-01-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_practiceidentifysession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practiceidentifysession',
            name='result',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
