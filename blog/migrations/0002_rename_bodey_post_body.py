# Generated by Django 3.2.9 on 2021-12-05 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='bodey',
            new_name='body',
        ),
    ]
