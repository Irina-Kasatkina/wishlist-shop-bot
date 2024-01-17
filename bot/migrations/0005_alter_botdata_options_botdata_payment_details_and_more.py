# Generated by Django 4.2.9 on 2024-01-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_botdata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='botdata',
            options={'verbose_name': 'бот', 'verbose_name_plural': 'боты'},
        ),
        migrations.AddField(
            model_name='botdata',
            name='payment_details',
            field=models.TextField(default='aaa', verbose_name='Реквизиты для оплаты сертификата'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='botdata',
            name='bot_name',
            field=models.CharField(max_length=256, verbose_name='Название бота'),
        ),
    ]