# Generated by Django 3.1.7 on 2021-03-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section_One',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='section1/images', verbose_name='Part_1 photo')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
            ],
        ),
    ]