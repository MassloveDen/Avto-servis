# Generated by Django 3.2.3 on 2021-05-31 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uslugi', '0002_uslugi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skladzap',
            name='zap',
        ),
        migrations.AddField(
            model_name='skladzap',
            name='zap',
            field=models.ManyToManyField(to='uslugi.Zapas', verbose_name='Запасные части'),
        ),
    ]
