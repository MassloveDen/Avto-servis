# Generated by Django 3.2.3 on 2021-05-30 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dealcent', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Mark',
        ),
        migrations.DeleteModel(
            name='Modl',
        ),
    ]
