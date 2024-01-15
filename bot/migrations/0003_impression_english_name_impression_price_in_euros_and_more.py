# Generated by Django 4.2.9 on 2024-01-15 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_impression'),
    ]

    operations = [
        migrations.AddField(
            model_name='impression',
            name='english_name',
            field=models.CharField(default='aaa', max_length=256, verbose_name='Наименование по-английски'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='impression',
            name='price_in_euros',
            field=models.PositiveIntegerField(default=1, verbose_name='Цена в Евро'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='impression',
            name='url_for_english',
            field=models.URLField(blank=True, verbose_name='Url английского описания'),
        ),
        migrations.AlterField(
            model_name='impression',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Наименование по-русски'),
        ),
    ]
