# Generated by Django 3.2.9 on 2021-11-12 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_auto_20211002_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('currentBlock', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
