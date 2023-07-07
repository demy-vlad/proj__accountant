# Generated by Django 4.1.7 on 2023-04-10 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParserConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Короткий опис')),
                ('url', models.URLField(verbose_name='Посилання')),
            ],
        ),
        migrations.CreateModel(
            name='ParserResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата додавання')),
                ('time', models.TimeField(verbose_name='Час додавання')),
                ('url', models.URLField(verbose_name='Посилання')),
            ],
        ),
        migrations.CreateModel(
            name='TelegramConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=100, verbose_name='Посилання на чат')),
                ('token', models.CharField(max_length=100, verbose_name='Токен боту')),
            ],
        ),
    ]