# Generated by Django 4.2.7 on 2023-12-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название статьи')),
                ('text', models.CharField(max_length=5000, verbose_name='Текст статьи')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]