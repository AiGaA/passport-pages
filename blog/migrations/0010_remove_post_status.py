# Generated by Django 3.2.20 on 2024-02-04 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]
