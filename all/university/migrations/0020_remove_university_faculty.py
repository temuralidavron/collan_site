# Generated by Django 3.1.7 on 2021-04-07 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0019_university_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='faculty',
        ),
    ]
