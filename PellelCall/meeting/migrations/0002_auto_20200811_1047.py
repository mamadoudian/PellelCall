# Generated by Django 3.0.8 on 2020-08-11 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conference',
            options={'ordering': ['-beginDate'], 'verbose_name': 'conférence'},
        ),
        migrations.AlterModelOptions(
            name='offer',
            options={'verbose_name': 'offre'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user'], 'verbose_name': 'profil'},
        ),
    ]
