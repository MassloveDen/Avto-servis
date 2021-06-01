# Generated by Django 3.2.3 on 2021-05-31 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uslugi', '0003_auto_20210531_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skladzap',
            name='zap',
        ),
        migrations.AddField(
            model_name='zapas',
            name='zapas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='uslugi.skladzap', verbose_name='Запасные части'),
            preserve_default=False,
        ),
    ]
