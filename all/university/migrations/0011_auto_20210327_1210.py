# Generated by Django 3.1.7 on 2021-03-27 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0010_auto_20210327_0904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='bachelor',
        ),
        migrations.RemoveField(
            model_name='university',
            name='foundation',
        ),
        migrations.RemoveField(
            model_name='university',
            name='intake_number',
        ),
        migrations.RemoveField(
            model_name='university',
            name='map',
        ),
        migrations.RemoveField(
            model_name='university',
            name='masters',
        ),
        migrations.RemoveField(
            model_name='university',
            name='video_banner',
        ),
        migrations.AddField(
            model_name='university',
            name='language',
            field=models.CharField(max_length=200, null=True, verbose_name='Language'),
        ),
        migrations.AddField(
            model_name='university',
            name='year',
            field=models.CharField(max_length=200, null=True, verbose_name='Year founded'),
        ),
    ]