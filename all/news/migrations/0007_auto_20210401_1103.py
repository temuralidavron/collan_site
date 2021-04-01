# Generated by Django 3.1.7 on 2021-04-01 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20210329_0822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': '4.0 Новости', 'verbose_name_plural': '4.0 Новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата добавления контента'),
        ),
        migrations.AlterField(
            model_name='news',
            name='banner',
            field=models.BooleanField(default=True, verbose_name='Активные Новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, upload_to='counrties/images', verbose_name='Для Фото'),
        ),
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Новость'),
        ),
        migrations.AlterField(
            model_name='news',
            name='name_ru',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Новость'),
        ),
        migrations.AlterField(
            model_name='news',
            name='name_uz',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Новость'),
        ),
        migrations.AlterField(
            model_name='news',
            name='time',
            field=models.CharField(max_length=100, null=True, verbose_name='Время чтение'),
        ),
        migrations.AlterField(
            model_name='news',
            name='top_news',
            field=models.BooleanField(default=False, verbose_name='Топ новости'),
        ),
    ]