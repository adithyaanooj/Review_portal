# Generated by Django 3.0.4 on 2020-03-27 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0002_auto_20200327_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='Rating',
            new_name='Stars',
        ),
        migrations.RenameField(
            model_name='professors',
            old_name='Rating',
            new_name='Stars',
        ),
    ]
