# Generated by Django 2.0.2 on 2018-03-29 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManager', '0005_auto_20180329_1144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataexport',
            old_name='contents',
            new_name='sql_contents',
        ),
    ]