# Generated by Django 3.0.2 on 2020-02-05 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': 'Job', 'verbose_name_plural': 'Jobs'},
        ),
    ]