# Generated by Django 5.0.3 on 2024-06-17 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fruits',
            name='ibsn',
        ),
    ]